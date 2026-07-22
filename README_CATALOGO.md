# Catalogo de accesorios de amortiguacion

Archivos:

- `catalogo_amortiguadores.json`: base estructurada para el programa.
- `catalogo_amortiguadores.csv`: formato para Excel/Power BI.
- `select_damper.py`: consulta por diametro de conductor.
- `build_catalog.py`: script reproducible de digitizacion.

Uso:

```powershell
python select_damper.py 16
python select_damper.py 16 --family amortiguador_SD
```

Familias incluidas:

- separador SP-2;
- separador SP-3;
- separador triple SP-3/3;
- separador-amortiguador SAPREM SPA400DA, SPA450DA, SPA400TA, SPA450TA, SPA400CA y SPA450CA;
- amortiguador Stockbridge SD.

Los datos dimensionales, masas y pares de apriete se transcribieron de las fichas entregadas. La compatibilidad mecanica no demuestra el cumplimiento vibratorio: para el EBP se deben asociar curvas de potencia/impedancia del modelo seleccionado.
