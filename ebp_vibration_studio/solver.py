"""Auditable Energy Balance Principle solver for aeolian conductor vibration.

The IEC 61897 wind-power function is implemented verbatim.  The conductor
self-damping and Stockbridge characteristic models are deliberately explicit:
they must be calibrated with laboratory data when a contractual study is made.
"""

from __future__ import annotations

import copy
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


IEC_A = (
    -0.491949,
    11.8029,
    -43.5532,
    -78.5876,
    -86.1199,
    -58.1808,
    -23.6082,
    -5.26705,
    -0.495885,
)


def iec_wind_function(y_over_d: float) -> float:
    """IEC 61897:1998 Annex C function fnc(Y/d), Y peak-to-peak."""
    ratio = min(max(float(y_over_d), 1.0e-3), 1.0)
    x = math.log10(ratio)
    z = sum(a * x**n for n, a in enumerate(IEC_A))
    return 10.0**z


def wave_number(frequency_hz: float, tension_n: float, mass_kg_m: float, ei_nm2: float) -> float:
    """Positive flexural-string wavenumber from EI*k^4 + T*k^2 = mu*w^2."""
    omega = 2.0 * math.pi * frequency_hz
    disc = tension_n**2 + 4.0 * ei_nm2 * mass_kg_m * omega**2
    k2 = (-tension_n + math.sqrt(disc)) / (2.0 * ei_nm2)
    return math.sqrt(max(k2, 1.0e-18))


def interpolate_curve(points: Iterable[Iterable[float]], x: float) -> float:
    """Piecewise-linear interpolation with zero power outside the measured band."""
    curve = sorted((float(a), float(b)) for a, b in points)
    if not curve or x < curve[0][0] or x > curve[-1][0]:
        return 0.0
    for (x0, y0), (x1, y1) in zip(curve, curve[1:]):
        if x0 <= x <= x1:
            if x1 == x0:
                return max(y0, y1)
            q = (x - x0) / (x1 - x0)
            return y0 + q * (y1 - y0)
    return curve[-1][1]


def wind_power_per_m(frequency_hz: float, y_pp_m: float, diameter_m: float, wind: dict[str, Any]) -> float:
    strouhal = max(float(wind.get("strouhal", 0.185)), 1.0e-6)
    velocity = frequency_hz * diameter_m / strouhal
    if velocity < float(wind.get("minimum_velocity_m_s", 0.0)):
        return 0.0
    if velocity >= float(wind.get("maximum_velocity_m_s", float("inf"))):
        return 0.0
    reduction = float(wind.get("power_factor", 1.0))
    # Optional transparent turbulence model. A supplied power_factor takes
    # precedence and permits direct calibration to a particular terrain model.
    if "power_factor" not in wind:
        turbulence = max(float(wind.get("turbulence_percent", 0.0)), 0.0) / 100.0
        reduction = math.exp(-2.4 * turbulence)
    if wind.get("frequency_correction"):
        reduction *= interpolate_curve(wind["frequency_correction"], frequency_hz)
    return reduction * frequency_hz**3 * diameter_m**4 * iec_wind_function(y_pp_m / diameter_m)


def self_damping_per_m(
    frequency_hz: float,
    amplitude_peak_m: float,
    wavelength_m: float,
    damping: dict[str, Any],
) -> float:
    """Empirical power-law model documented in the supplied MO/TecnoSoft paper."""
    h_si = float(damping["h_si"])
    n = float(damping.get("wavelength_exp", 4.35))
    m = float(damping.get("amplitude_exp", 2.35))
    return 0.5 * math.pi * h_si * frequency_hz * wavelength_m ** (-n) * amplitude_peak_m**m


def damper_power(
    frequency_hz: float,
    amplitude_peak_m: float,
    wavenumber: float,
    damper: dict[str, Any],
) -> tuple[float, float]:
    """Return dissipated W and damper-clamp peak amplitude.

    IEC 61897 characteristic tests use a controlled clamp velocity.  The input
    curve is therefore scaled quadratically from its reference velocity.
    """
    x_m = float(damper["position_m"])
    coupling = abs(math.sin(wavenumber * x_m))
    foot_amplitude = amplitude_peak_m * coupling
    foot_velocity = 2.0 * math.pi * frequency_hz * foot_amplitude
    reference_velocity = max(float(damper.get("reference_velocity_m_s", 0.1)), 1.0e-9)
    characteristic = interpolate_curve(damper.get("power_curve", []), frequency_hz)
    power = characteristic * (foot_velocity / reference_velocity) ** 2
    power /= max(float(damper.get("safety_factor", 1.5)), 1.0)
    return max(power, 0.0), foot_amplitude


def poffenberger_swart_strain(
    amplitude_peak_m: float,
    wavenumber: float,
    conductor: dict[str, Any],
    termination: dict[str, Any],
) -> float:
    """Return peak microstrain at the clamp using the PS boundary-layer model."""
    p = math.sqrt(float(conductor["tension_n"]) / float(conductor["ei_nm2"]))
    outer_wire = float(conductor.get("outer_wire_diameter_m", conductor["diameter_m"]))
    calibration = float(termination.get("strain_factor", 1.0))
    rods_factor = float(termination.get("armor_rods_factor", 1.0))
    strain = calibration * rods_factor * 0.5 * outer_wire * p * wavenumber * amplitude_peak_m
    return strain * 1.0e6


def _scan_roots(function, low: float, high: float, steps: int = 260) -> list[float]:
    roots: list[float] = []
    log_low, log_high = math.log(low), math.log(high)
    xs = [math.exp(log_low + i * (log_high - log_low) / steps) for i in range(steps + 1)]
    previous_x, previous_y = xs[0], function(xs[0])
    for x in xs[1:]:
        y = function(x)
        if y == 0.0 or previous_y * y < 0.0:
            lo, hi = previous_x, x
            for _ in range(70):
                mid = 0.5 * (lo + hi)
                if function(lo) * function(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
        previous_x, previous_y = x, y
    return roots


def solve_frequency(config: dict[str, Any], frequency_hz: float) -> dict[str, float | str | bool]:
    conductor = config["conductor"]
    termination = config.get("termination", {})
    diameter = float(conductor["diameter_m"])
    span = float(config["span_m"])
    k = wave_number(
        frequency_hz,
        float(conductor["tension_n"]),
        float(conductor["mass_kg_m"]),
        float(conductor["ei_nm2"]),
    )
    wavelength = 2.0 * math.pi / k
    dampers = config.get("dampers", []) if config.get("dampers_enabled", True) else []

    def balance(amplitude: float) -> float:
        y_pp = 2.0 * amplitude
        p_w = wind_power_per_m(frequency_hz, y_pp, diameter, config.get("wind", {})) * span
        p_s = self_damping_per_m(frequency_hz, amplitude, wavelength, config["self_damping"]) * span
        p_d = sum(damper_power(frequency_hz, amplitude, k, item)[0] for item in dampers)
        return p_w - p_s - p_d

    lower_bound, upper_bound = diameter * 5.0e-4, diameter * 10.0
    roots = _scan_roots(balance, lower_bound, upper_bound)
    if roots:
        # The upper crossing is the stable energy equilibrium: a small amplitude
        # increase then makes dissipation exceed input. The lower crossing is the
        # unstable threshold and is retained only implicitly in the root scan.
        amplitude = roots[-1]
        status = "equilibrium"
    else:
        candidates = [lower_bound * ((upper_bound / lower_bound) ** (i / 180.0)) for i in range(181)]
        values = [balance(item) for item in candidates]
        if max(values) <= 0.0:
            amplitude = 0.0
            status = "suppressed"
        else:
            amplitude = min(candidates, key=lambda a: abs(balance(a)))
            status = "bounded-no-root"

    y_pp = 2.0 * amplitude
    p_w_m = wind_power_per_m(frequency_hz, y_pp, diameter, config.get("wind", {}))
    p_s_m = self_damping_per_m(frequency_hz, amplitude, wavelength, config["self_damping"])
    damper_values = [damper_power(frequency_hz, amplitude, k, item) for item in dampers]
    p_d = sum(value[0] for value in damper_values)
    max_foot = max((value[1] for value in damper_values), default=0.0)
    clamp_strain = poffenberger_swart_strain(amplitude, k, conductor, termination)
    damper_strain = clamp_strain * float(termination.get("damper_clamp_ratio", 0.35))
    clamp_limit = float(config.get("limits", {}).get("clamp_microstrain", 150.0))
    damper_limit = float(config.get("limits", {}).get("damper_microstrain", 75.0))
    residual = p_w_m * span - p_s_m * span - p_d
    strouhal = max(float(config.get("wind", {}).get("strouhal", 0.185)), 1.0e-6)
    return {
        "frequency_hz": frequency_hz,
        "wind_velocity_m_s": frequency_hz * diameter / strouhal,
        "wavelength_m": wavelength,
        "amplitude_peak_mm": amplitude * 1000.0,
        "amplitude_pp_over_d": y_pp / diameter,
        "clamp_microstrain": clamp_strain,
        "damper_microstrain": damper_strain,
        "damper_amplitude_peak_mm": max_foot * 1000.0,
        "wind_power_w": p_w_m * span,
        "conductor_power_w": p_s_m * span,
        "damper_power_w": p_d,
        "balance_residual_w": residual,
        "safe": clamp_strain <= clamp_limit and damper_strain <= damper_limit,
        "status": status,
    }


def solve_spectrum(config: dict[str, Any]) -> dict[str, Any]:
    start = float(config.get("frequency", {}).get("start_hz", 5.0))
    stop = float(config.get("frequency", {}).get("stop_hz", 80.0))
    step = max(float(config.get("frequency", {}).get("step_hz", 1.0)), 0.05)
    count = int(round((stop - start) / step))
    rows = [solve_frequency(config, start + i * step) for i in range(count + 1)]
    worst = max(rows, key=lambda row: float(row["clamp_microstrain"]))
    unsafe = [row for row in rows if not row["safe"]]
    return {
        "rows": rows,
        "summary": {
            "max_clamp_microstrain": worst["clamp_microstrain"],
            "critical_frequency_hz": worst["frequency_hz"],
            "critical_wind_velocity_m_s": worst["wind_velocity_m_s"],
            "unsafe_points": len(unsafe),
            "safe": not unsafe,
            "model": "EBP-IEC 61897 Annex C / Poffenberger-Swart",
        },
    }


def optimize_positions(config: dict[str, Any], minimum_m: float = 0.4, maximum_m: float = 2.0, step_m: float = 0.05) -> dict[str, Any]:
    if not config.get("dampers"):
        raise ValueError("At least one damper is required for position optimization")
    candidates = []
    count = int(round((maximum_m - minimum_m) / step_m))
    for i in range(count + 1):
        position = minimum_m + i * step_m
        trial = copy.deepcopy(config)
        for damper in trial["dampers"]:
            damper["position_m"] = position
        result = solve_spectrum(trial)
        candidates.append({
            "position_m": position,
            "max_clamp_microstrain": result["summary"]["max_clamp_microstrain"],
            "unsafe_points": result["summary"]["unsafe_points"],
        })
    best = min(candidates, key=lambda item: (item["unsafe_points"], item["max_clamp_microstrain"]))
    return {"best": best, "candidates": candidates}


def load_presets() -> dict[str, Any]:
    path = Path(__file__).with_name("presets.json")
    return json.loads(path.read_text(encoding="utf-8"))
