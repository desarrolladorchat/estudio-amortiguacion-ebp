import math, sys
sys.path.insert(0, '.')
from ebp_vibration import fnc_iec, Conductor, EBPCase

def test_fnc_positive_and_peak():
    vals = [fnc_iec(x) for x in (0.001, 0.01, 0.1, 1.0)]
    assert all(v > 0 for v in vals)
    assert fnc_iec(0.1) > fnc_iec(0.001)

def test_wavelength_tension_only():
    c = Conductor(0.02, 1.0, 10000)
    assert abs(c.wavelength(10) - 10.0) < 1e-12

def test_ebp_root_without_damper():
    c = Conductor(0.02, 1.0, 10000, self_damping_H=1e-4, self_damping_n=0, self_damping_m=2)
    case = EBPCase(100, c)
    y = case.solve_amplitude(10)
    assert math.isfinite(y) and y > 0
    assert abs(case.residual(10, y)) < 1e-6
