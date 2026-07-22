# Motor EBP CIGRE independiente

## Alcance

La página mantiene dos caminos separados:

1. **Reproducción calibrada del PDF:** conserva las curvas, resultados y pautas de instalación de los casos documentales cargados.
2. **EBP CIGRE independiente:** calcula un conductor o cable simple con datos físicos y ensayos aportados por el usuario. No reutiliza curvas objetivo de los ejemplos.

El modo «IEC/Mosdorfer preliminar» se conserva solo para trazabilidad histórica. No debe emplearse para emitir un dictamen contractual.

## Balance de energía

Para cada frecuencia se resuelve la amplitud pico a pico `Ypp` que satisface:

`Pw(Ypp) = Pc(Ypp) + Σ Pa_i(Ypp)`

- `Pw`: potencia eólica introducida en el vano.
- `Pc`: autoamortiguamiento del conductor.
- `Pa_i`: potencia absorbida por cada amortiguador.

La potencia eólica sigue IEC 61897:1998, Anexo C:

`Pw = L · D⁴ · f³ · fnc(Ypp/D)`

`fnc = 10^z`, `z = Σ a_n · xⁿ`, `x = log10(Ypp/D)`.

Se corrigió el coeficiente lineal a `a₁ = -11.8029`. La implementación reproduce, entre otros, `fnc(0.01)=0.00603` y `fnc(0.10)=0.37087`, coherentes con la gráfica del Anexo C.

El autoamortiguamiento CIGRE usa:

`Pc/L = k · y₀ˡ · fᵐ · Tⁿ`, con `y₀ = Ypp/2`.

Los coeficientes `k, l, m, n` y la unidad de tensión usada por `k` deben proceder de ensayo o de una fuente identificada. El programa no inventa valores genéricos.

## Modelo mecánico y deformación

La longitud de onda incluye tensión, masa lineal y rigidez a flexión `EJ`. Se calcula una envolvente con `EJ mínimo`, `EJ central` y `EJ máximo`, además de las incertidumbres de excitación y disipación ingresadas.

La deformación ideal de antinodo se transforma al punto de control mediante un factor medido. Sin ese factor, la salida se etiqueta **exploratoria** y no se evalúa cumplimiento contractual.

La relación frecuencia-velocidad puede usar un Strouhal fijo o un diagnóstico por Reynolds. Temperatura, altitud y rugosidad participan en este diagnóstico; la turbulencia se informa como advertencia cuando excede el ámbito del EBP estacionario simple.

## Datos dinámicos del amortiguador

Cada accesorio instalado usa la misma superficie dinámica declarada en JSON. Para productos distintos deben ejecutarse estudios separados o suministrarse una caracterización común validada.

Ejemplo mínimo:

```json
[
  {"frequency_hz": 10, "clamp_velocity_m_s": 0.005, "power_w": 0.02},
  {"frequency_hz": 10, "clamp_velocity_m_s": 0.020, "power_w": 0.25},
  {"frequency_hz": 30, "clamp_velocity_m_s": 0.005, "power_w": 0.03},
  {"frequency_hz": 30, "clamp_velocity_m_s": 0.020, "power_w": 0.40}
]
```

La velocidad es el valor pico de la grapa y la potencia es potencia media absorbida. Se interpola primero en velocidad y luego en frecuencia. Fuera del último punto de velocidad se aplica extrapolación cuadrática, que debe ser revisada por el ingeniero responsable.

## Reglas de trazabilidad

Un dictamen solo se habilita cuando existen:

- fuente, revisión y fecha de los datos;
- ley CIGRE medida de autoamortiguamiento;
- factor medido entre antinodo y punto de control;
- curva dinámica medida si se instalaron amortiguadores;
- error de balance menor de 2 %.

La tabla y el CSV incluyen amplitud, envolvente de deformación, potencia eólica, autoamortiguamiento, potencia absorbida, movimiento de grapa y error de balance.

## Decisiones expresamente no adoptadas

- No se usa Blevins como modelo principal del conductor; solo apoya el diagnóstico aerodinámico.
- No se impone `St = 0.185` a todos los casos.
- No se aplican factores ENDESA globales sin que el usuario los declare mediante incertidumbres o factor de viento.
- No se extrapolan propiedades de amortiguadores a partir de masa o dimensiones del catálogo.
- No se calcula un haz múltiple con un modelo equivalente escalar. El modo se bloquea hasta contar con matrices modales y propiedades medidas de separadores.
- No se sustituyen los ejemplos documentales por un ajuste global. Se conservan como banco de regresión separado.

## Limitación profesional

El motor es una herramienta de cálculo y trazabilidad. La aceptación final requiere revisión de datos de ensayo, hipótesis de montaje, límites del fabricante y criterio del ingeniero responsable.
