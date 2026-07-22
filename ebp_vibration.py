"""IEC 61897 / TECNOSOFT-style aeolian vibration EBP model.

The implementation is intentionally data driven: conductor self damping and
damper dissipation are supplied as fitted coefficients or measured CSV curves.
It reproduces the Energy Balance Principle used in the attached studies:

    P_w(Y,f) = P_self(Y,f) + sum(P_damper(Y_x,f)/safety_factor)

Y is conductor antinode peak-to-peak displacement (m).
"""
from __future__ import annotations

from dataclasses import dataclass, field
import csv
import json
import math
from pathlib import Path
from typing import Callable, Iterable, Sequence


IEC_FNC_COEFFS = (
    -0.491949, 11.8029, -43.5532, -78.5876, -86.1199,
    -58.1808, -23.6082, -5.26705, -0.495885,
)


def fnc_iec(y_over_d: float) -> float:
    """IEC 61897 Annex C wind power input function (dimensionless)."""
    if y_over_d <= 0:
        return 0.0
    x = math.log10(y_over_d)
    z = sum(a * x**n for n, a in enumerate(IEC_FNC_COEFFS))
    return 10.0**z


def linear_interp(x: float, xs: Sequence[float], ys: Sequence[float]) -> float:
    if not xs:
        return 0.0
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    lo, hi = 0, len(xs) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if xs[mid] <= x:
            lo = mid
        else:
            hi = mid
    t = (x - xs[lo]) / (xs[hi] - xs[lo])
    return ys[lo] + t * (ys[hi] - ys[lo])


@dataclass
class DamperCurve:
    """Frequency/amplitude dissipation curve for one damper.

    CSV columns: frequency_hz, amplitude_mm, power_w.  Amplitude is the
    peak-to-peak conductor/damper motion used by the supplied test data.
    """
    frequency_hz: list[float]
    amplitude_m: list[float]
    power_w: list[float]
    name: str = "damper"

    @classmethod
    def from_csv(cls, path: str | Path, name: str | None = None) -> "DamperCurve":
        rows = []
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                f = float(r.get("frequency_hz", r.get("frequency", r.get("f_hz"))))
                a = float(r.get("amplitude_mm", r.get("amplitude", r.get("a_mm")))) / 1000.0
                p = float(r.get("power_w", r.get("power", r.get("P_w"))))
                rows.append((f, a, p))
        if not rows:
            raise ValueError(f"No rows in damper curve: {path}")
        return cls([r[0] for r in rows], [r[1] for r in rows], [r[2] for r in rows], name or Path(path).stem)

    def power(self, frequency_hz: float, amplitude_m: float) -> float:
        # Interpolate in amplitude for each frequency, then between nearest
        # frequency curves. This is robust for sparse supplier test data.
        by_f: dict[float, list[tuple[float, float]]] = {}
        for f, a, p in zip(self.frequency_hz, self.amplitude_m, self.power_w):
            by_f.setdefault(f, []).append((a, p))
        fs = sorted(by_f)
        vals = []
        for f in fs:
            pts = sorted(by_f[f])
            vals.append(linear_interp(amplitude_m, [p[0] for p in pts], [p[1] for p in pts]))
        return linear_interp(frequency_hz, fs, vals)


@dataclass
class Conductor:
    diameter_m: float
    mass_kg_m: float
    tension_n: float
    bending_stiffness_nm2: float = 0.0
    self_damping_H: float = 0.0
    self_damping_n: float = 0.0
    self_damping_m: float = 2.0
    # Optional CIGRE empirical power law: P_self/L = k*y0^l*f^p*T^q.
    # y0 is peak (not peak-to-peak) antinode amplitude.
    cigre_k: float = 0.0
    cigre_l: float = 2.44
    cigre_p: float = 5.63
    cigre_q: float = 2.76

    def wavelength(self, frequency_hz: float) -> float:
        """Solve dispersion f²=T/(rho λ²)+4π²EI/(rho λ⁴)."""
        rho, T, EI = self.mass_kg_m, self.tension_n, self.bending_stiffness_nm2
        if EI <= 0:
            return math.sqrt(T / rho) / frequency_hz
        # q = 1/lambda², solve 4*pi²*EI*q² + T*q - rho*f² = 0
        a = 4 * math.pi**2 * EI
        q = (-T + math.sqrt(T*T + 4*a*rho*frequency_hz**2)) / (2*a)
        return 1.0 / math.sqrt(q)

    def self_power(self, frequency_hz: float, wavelength_m: float, Y_m: float) -> float:
        # Mosdorfer form: P_s = pi/2 H f lambda^-n U^m.
        if self.cigre_k > 0:
            y0 = Y_m / 2.0
            return self.cigre_k * y0**self.cigre_l * frequency_hz**self.cigre_p * self.tension_n**self.cigre_q
        return math.pi / 2.0 * self.self_damping_H * frequency_hz * wavelength_m ** (-self.self_damping_n) * Y_m ** self.self_damping_m


@dataclass
class Damper:
    position_m: float
    curve: DamperCurve
    safety_factor: float = 1.5
    motion_factor: float = 1.0


@dataclass
class EBPCase:
    span_m: float
    conductor: Conductor
    dampers: list[Damper] = field(default_factory=list)
    wind_function: Callable[[float], float] = fnc_iec
    endpoint_limit_microstrain: float = 150.0
    damper_limit_microstrain: float = 75.0
    air_density_kg_m3: float = 1.225
    kinematic_viscosity_m2_s: float = 1.5e-5
    strouhal: float = 0.2
    turbulence_factor: float = 1.0

    def wind_power(self, frequency_hz: float, Y_m: float) -> float:
        return self.turbulence_factor * self.span_m * self.conductor.diameter_m**4 * frequency_hz**3 * self.wind_function(Y_m / self.conductor.diameter_m)

    def wind_speed(self, frequency_hz: float) -> float:
        """Approximate vortex-shedding wind speed from St=fD/V."""
        return frequency_hz * self.conductor.diameter_m / self.strouhal

    def reynolds(self, frequency_hz: float) -> float:
        return self.wind_speed(frequency_hz) * self.conductor.diameter_m / self.kinematic_viscosity_m2_s

    def scruton(self, logarithmic_decrement: float) -> float:
        """Scruton number Sc = delta*m/(rho*D^2), per CIGRE."""
        return logarithmic_decrement * self.conductor.mass_kg_m / (self.air_density_kg_m3 * self.conductor.diameter_m**2)

    def displacement_at(self, x_m: float, frequency_hz: float, Y_m: float) -> float:
        lam = self.conductor.wavelength(frequency_hz)
        # Peak-to-peak amplitude at an antinode; a simply supported standing wave.
        return Y_m * abs(math.sin(2 * math.pi * x_m / lam))

    def strain_micro(self, x_m: float, frequency_hz: float, Y_m: float) -> float:
        lam = self.conductor.wavelength(frequency_hz)
        # curvature amplitude from peak displacement Y/2, converted to microstrain.
        # At a rigid termination the displacement is zero but curvature/strain
        # is not; use the curvature envelope at the two span ends.  Interior
        # points use the standing-wave shape.
        shape = 1.0 if abs(x_m) < 1e-12 or abs(x_m - self.span_m) < 1e-12 else abs(math.sin(2 * math.pi * x_m / lam))
        curvature = (2 * math.pi / lam) ** 2 * (Y_m / 2.0) * shape
        return curvature * self.conductor.diameter_m / 2.0 * 1e6

    def damper_power(self, damper: Damper, frequency_hz: float, Y_m: float) -> float:
        amp = self.displacement_at(damper.position_m, frequency_hz, Y_m) * damper.motion_factor
        return damper.curve.power(frequency_hz, amp) / damper.safety_factor

    def residual(self, frequency_hz: float, Y_m: float) -> float:
        lam = self.conductor.wavelength(frequency_hz)
        return self.wind_power(frequency_hz, Y_m) - self.conductor.self_power(frequency_hz, lam, Y_m) - sum(self.damper_power(d, frequency_hz, Y_m) for d in self.dampers)

    def solve_amplitude(self, frequency_hz: float, ymin_m: float = 1e-9, ymax_m: float | None = None, tol: float = 1e-10) -> float:
        ymax_m = ymax_m or 2.0 * self.conductor.diameter_m
        # Grid search brackets the first positive root; EBP curves can be non-monotonic.
        n = 300
        prev_y, prev_r = ymin_m, self.residual(frequency_hz, ymin_m)
        for i in range(1, n + 1):
            y = ymin_m * (ymax_m / ymin_m) ** (i / n)
            r = self.residual(frequency_hz, y)
            if prev_r == 0 or r == 0 or prev_r * r < 0:
                lo, hi = prev_y, y
                for _ in range(100):
                    mid = 0.5 * (lo + hi)
                    rm = self.residual(frequency_hz, mid)
                    if abs(rm) < tol * max(1.0, self.wind_power(frequency_hz, mid)):
                        return mid
                    if self.residual(frequency_hz, lo) * rm <= 0:
                        hi = mid
                    else:
                        lo = mid
                return 0.5 * (lo + hi)
            prev_y, prev_r = y, r
        return float("nan")

    def sweep(self, frequencies_hz: Iterable[float]) -> list[dict]:
        out = []
        for f in frequencies_hz:
            y = self.solve_amplitude(float(f))
            row = {"frequency_hz": float(f), "amplitude_pp_mm": y * 1000.0 if math.isfinite(y) else float("nan"), "wavelength_m": self.conductor.wavelength(float(f)), "wind_speed_m_s": self.wind_speed(float(f)), "reynolds": self.reynolds(float(f))}
            row["wind_power_w"] = self.wind_power(float(f), y) if math.isfinite(y) else float("nan")
            row["endpoint_strain_microstrain"] = max(self.strain_micro(0.0, float(f), y), self.strain_micro(self.span_m, float(f), y)) if math.isfinite(y) else float("nan")
            row["damper_strains_microstrain"] = [self.strain_micro(d.position_m, float(f), y) for d in self.dampers] if math.isfinite(y) else []
            row["endpoint_ok"] = row["endpoint_strain_microstrain"] <= self.endpoint_limit_microstrain if math.isfinite(y) else False
            row["damper_ok"] = all(s <= self.damper_limit_microstrain for s in row["damper_strains_microstrain"])
            out.append(row)
        return out


def load_case(path: str | Path) -> EBPCase:
    cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    c = Conductor(**cfg["conductor"])
    dampers = [Damper(position_m=d["position_m"], curve=DamperCurve.from_csv(d["curve_csv"], d.get("name")), safety_factor=d.get("safety_factor", cfg.get("damper_safety_factor", 1.5)), motion_factor=d.get("motion_factor", 1.0)) for d in cfg.get("dampers", [])]
    return EBPCase(span_m=cfg["span_m"], conductor=c, dampers=dampers, endpoint_limit_microstrain=cfg.get("endpoint_limit_microstrain", 150.0), damper_limit_microstrain=cfg.get("damper_limit_microstrain", 75.0), air_density_kg_m3=cfg.get("air_density_kg_m3", 1.225), kinematic_viscosity_m2_s=cfg.get("kinematic_viscosity_m2_s", 1.5e-5), strouhal=cfg.get("strouhal", 0.2), turbulence_factor=cfg.get("turbulence_factor", 1.0))
