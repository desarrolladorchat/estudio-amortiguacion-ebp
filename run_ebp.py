#!/usr/bin/env python3
"""Run an IEC 61897 EBP frequency sweep from a JSON case file."""
import argparse, csv, json, math
from ebp_vibration import load_case

def main():
    ap = argparse.ArgumentParser(description="IEC 61897 / EBP aeolian vibration simulator")
    ap.add_argument("case", help="JSON input case")
    ap.add_argument("--fmin", type=float, default=5.0)
    ap.add_argument("--fmax", type=float, default=100.0)
    ap.add_argument("--step", type=float, default=1.0)
    ap.add_argument("--out", default="results.csv")
    args = ap.parse_args()
    case = load_case(args.case)
    freqs = []
    f = args.fmin
    while f <= args.fmax + 1e-12:
        freqs.append(f); f += args.step
    rows = case.sweep(freqs)
    keys = ["frequency_hz", "wavelength_m", "wind_speed_m_s", "reynolds", "amplitude_pp_mm", "wind_power_w", "endpoint_strain_microstrain", "endpoint_ok", "damper_ok"]
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys); w.writeheader()
        for r in rows: w.writerow({k: r[k] for k in keys})
    finite = [r for r in rows if math.isfinite(r["amplitude_pp_mm"])]
    print(json.dumps({"rows": len(rows), "output": args.out, "max_amplitude_mm": max((r["amplitude_pp_mm"] for r in finite), default=None), "endpoint_failures": sum(not r["endpoint_ok"] for r in finite), "damper_failures": sum(not r["damper_ok"] for r in finite)}, indent=2))

if __name__ == "__main__": main()
