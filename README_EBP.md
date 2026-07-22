# Simulador EBP de vibración eólica (IEC 61897)

Este programa reproduce el cálculo físico documentado en los estudios TECNOSOFT III: en cada frecuencia busca la amplitud estacionaria que satisface

`P_w = P_self + Σ(P_damper / factor_de_seguridad)`.

La potencia eólica IEC 61897 Annex C se calcula con `P_w = L d^4 f^3 fnc(Y/d)` y el polinomio normativo de nueve coeficientes. `Y` es amplitud pico-a-pico en el vientre (m). La auto-disipación usa la forma de Mosdorfer `P_self = π/2 H f λ^(-n) Y^m`; `H`, `n` y `m` deben obtenerse de ensayos del conductor (los informes adjuntos indican que TECNOSOFT los lee de gráficos/datos del cable). Las curvas de cada amortiguador se importan como CSV de proveedor (`frequency_hz, amplitude_mm, power_w`).

## Uso

Desde `work/`:

```powershell
python run_ebp.py example_case.json --fmin 5 --fmax 100 --step 0.1 --out results.csv
```

Para añadir un amortiguador, agregue al JSON:

```json
"dampers": [{"position_m": 1.02, "curve_csv": "example_damper.csv", "safety_factor": 1.5}]
```

El CSV de salida contiene frecuencia, longitud de onda, amplitud pico-a-pico, potencia eólica, deformación en extremos y banderas de cumplimiento. La deformación se estima con el modo de onda estacionaria `sin(2πx/λ)` y curvatura de una viga/cuerda; debe contrastarse con el modelo detallado del fabricante cuando existan varillas, haces o geometría de herrajes.

## Alcance y datos faltantes

No es posible clonar bit a bit TECNOSOFT III sin sus ficheros propietarios `.dsy`, curvas de autoamortiguamiento, rigidez y curvas de potencia de cada AMG/SPA. Este sustituto es transparente y auditable: permite cargar esas mediciones, reproducir el EBP y hacer análisis de sensibilidad. Para haces dúplex/cuádruplex, modele cada subconductor o extienda la curva de separador con la potencia medida del fabricante.

## Validación IEC

La función `fnc_iec` usa exactamente los coeficientes publicados en IEC 61897:1998, Annex C, y `wavelength()` resuelve la ecuación de dispersión `f²=T/(ρλ²)+4π²EI/(ρλ⁴)` incluida en los antecedentes Wind induced vibrations.
