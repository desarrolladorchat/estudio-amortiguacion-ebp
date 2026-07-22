# Estudio de amortiguación EBP / IEC 61897

Aplicación web para reproducir y comparar estudios de vibración eólica de conductores y cables OPGW mediante casos calibrados, referencias IEC 61897/CIGRE y un motor EBP independiente.

## Uso local

La interfaz es estática. Puede abrirse mediante cualquier servidor HTTP:

```bash
python -m http.server 8000
```

Luego abra `http://127.0.0.1:8000/`.

## Contenido principal

- `index.html`: interfaz del simulador.
- `app.js`: cálculos, casos de referencia, gráficos y recomendaciones.
- `catalogo_amortiguadores.json`: catálogo de amortiguadores y separadores.
- `auditoria-ejemplos.html`: matriz de trazabilidad y verificación de los casos.
- `assets/`: imágenes de identificación de accesorios.

## Alcance técnico

Los casos denominados “reproducción calibrada” reconstruyen resultados publicados en los documentos de referencia. Las corridas independientes requieren datos dinámicos medidos del conductor y de los accesorios. La herramienta no reemplaza la revisión de ingeniería ni la aprobación del fabricante.
