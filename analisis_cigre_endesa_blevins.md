# Análisis de aplicabilidad: CIGRE, ENDESA y Blevins

Fecha de revisión: 22-07-2026

## Dictamen

Los dos libros nuevos son aplicables, pero no deben desplazar al libro *Modelling of Vibrations of Overhead Line Conductors* de CIGRE.

- **CIGRE Green Book:** fuente principal para la arquitectura del cálculo EBP de conductores simples, conductor más amortiguador, haces y oscilación de subvano.
- **ENDESA, Vibraciones de conductores:** referencia complementaria e histórica para comprobaciones de diseño, ubicación de amortiguadores, límites, movimiento de la grapa y factores de seguridad.
- **Blevins, Flow-Induced Vibration:** referencia complementaria para Reynolds, Strouhal, rugosidad, turbulencia, correlación de la estela y *lock-in*. No reemplaza el modelo específico de líneas aéreas de CIGRE.
- **IEC 61897:** norma de ensayo y aceptación del amortiguador. Su función de potencia usa amplitud de antinodo pico a pico.

El simulador debe actualizarse antes de presentarse como una implementación EBP independiente de CIGRE. Los ejemplos PDF actualmente reproducidos pueden conservarse sin cambio porque son casos calibrados contra resultados publicados.

## Jerarquía técnica propuesta

1. CIGRE Green Book: formulación y alcance del EBP.
2. IEC 61897: ensayo, caracterización y aceptación del amortiguador.
3. Datos medidos del conductor y del amortiguador suministrados por fabricante o laboratorio.
4. Informes TECNOSOFT/ATTRA/ESANAM suministrados: validación de casos de referencia.
5. ENDESA: comprobaciones conservadoras y reglas históricas.
6. Blevins: física aerodinámica general y diagnóstico de regímenes.

## Revisión del modelo actual

### Aspectos correctos o aprovechables

- Resuelve el balance de potencia de forma no lineal para cada frecuencia.
- La potencia eólica genérica sigue la forma IEC `Pw = L D^4 f^3 fnc(Y/D)`.
- En esa expresión, `Y` se maneja como amplitud pico a pico, coherente con IEC 61897.
- Calcula velocidad mediante Strouhal y calcula Reynolds.
- La longitud de onda incluye tensión, masa y rigidez a flexión `EI`.
- Considera la posición del amortiguador mediante la amplitud local de la onda.
- Mantiene separados los casos calibrados provenientes de los PDF.

### Brechas frente a CIGRE

| Tema | Situación actual | Exigencia o recomendación de CIGRE | Acción |
|---|---|---|---|
| Modo de cálculo | Se mezclan cálculo genérico y reproducciones calibradas | Debe conocerse la procedencia de cada función y dato | Separar “Reproducción de informe” y “EBP CIGRE independiente” |
| Convención de amplitud | IEC usa pico a pico; otras curvas usan 0-pico | CIGRE expresa normalmente `y0` como 0-pico | Guardar internamente `y_peak` y convertir explícitamente a `Y_pp = 2 y_peak` |
| Potencia del viento | Una sola curva IEC y un factor escalar | CIGRE muestra dispersión entre bases de potencia y sensibilidad elevada | Permitir seleccionar base CIGRE/IEC, documentar procedencia y calcular envolventes |
| Reynolds y Strouhal | `St` y viscosidad son constantes ingresadas o fijas | Reynolds, rugosidad y turbulencia pueden alterar potencia y frecuencia | Incorporar propiedades del aire, régimen de Reynolds y advertencias |
| Autoamortiguamiento | Ley tipo Mosdorfer heredada con `H`, exponentes y longitud de onda | CIGRE usa datos medidos y leyes `P/L = k y0^l f^m T^n` | Añadir modelo CIGRE con `k,l,m,n`, unidades, método PT/ISWR y procedencia |
| Rigidez del conductor | Un único `EI` | CIGRE distingue `EJmin/EJmax` por deslizamiento entre hebras | Admitir intervalo o curva de rigidez y análisis de sensibilidad |
| Deformación | Curvatura ideal del cable en el antinodo | El control de fatiga necesita deformación en grapa/extremo y condiciones de borde | Separar deformación de antinodo, suspensión, amarre y grapa del amortiguador |
| Amortiguador | Coeficiente equivalente escalar `coef·f·A²` | CIGRE requiere impedancia, rigidez dinámica o matriz de transferencia, dependiente de frecuencia y amplitud | Sustituir el coeficiente por tablas/curvas complejas medidas |
| Varios amortiguadores | Suma independiente de potencias locales | CIGRE advierte interacción entre amortiguadores y distorsión de la onda | Implementar solución acoplada o matriz de transferencia |
| Haces y separadores | Los ejemplos usan nubes digitalizadas | CIGRE modela modos del haz, subvanos y matrices de impedancia de separadores | Mantenerlos como calibrados hasta disponer de matrices dinámicas |
| Incertidumbre | Un solo resultado | CIGRE reporta incertidumbres grandes, del orden de ±50–60 % en ciertas condiciones | Mostrar banda inferior/central/superior y trazabilidad de supuestos |

## Aportes de ENDESA que sí conviene incorporar

- Comprobación opcional con `St = 0,185`, sin sustituir globalmente el valor CIGRE/IEC.
- Algoritmo de búsqueda por rangos de vano: sin amortiguador, una unidad, dos unidades y casos especiales.
- Optimización de posición sobre una banda de frecuencias, no para una frecuencia aislada.
- Movimiento máximo de grapa como comprobación histórica: 2 mm bajo 10 Hz y 3 mm sobre 10 Hz para el Stockbridge descrito. Debe ser sustituible por el límite certificado del fabricante.
- Factores conservadores configurables: aumento del viento, batido modal y dispersión de fabricación.
- Verificación explícita de fase: un amortiguador con fuerza casi en fase o en oposición disipa poco; la zona cercana a 90 grados es la más eficaz.

No deben aplicarse automáticamente a todos los proyectos los factores ENDESA de 30 %, 1,5 o 2, ni su límite histórico de 75 microstrain. Deben quedar como un perfil de comprobación, subordinado al criterio contractual, al material y a CIGRE.

## Aportes de Blevins que sí conviene incorporar

- Cálculo del régimen de Reynolds antes de elegir Strouhal.
- Efectos de rugosidad superficial y turbulencia sobre el régimen de desprendimiento.
- Diagnóstico de *lock-in* y advertencia de que la vibración modifica la estela.
- Longitud de correlación de la estela y pérdida de coherencia a lo largo del vano.
- Parámetros adimensionales: velocidad reducida, amortiguamiento reducido y relación de masa.

Blevins no debe utilizarse como sustituto del EBP de CIGRE para conductores trenzados ni como fuente de la potencia disipada por un Stockbridge real. Sus modelos de cilindro son útiles para el módulo aerodinámico y para comprobaciones de coherencia.

## Actualización recomendada

### Prioridad 0 - necesaria para afirmar “EBP CIGRE independiente”

1. Separar formalmente los dos modos: reproducción calibrada y cálculo físico independiente.
2. Normalizar unidades y convenciones de amplitud.
3. Incorporar la ley CIGRE de autoamortiguamiento con coeficientes medidos.
4. Importar curvas de impedancia, rigidez dinámica, fase o potencia del amortiguador.
5. Calcular deformaciones en los puntos de control reales, con condiciones de borde declaradas.
6. Añadir trazabilidad y bandas de incertidumbre.

### Prioridad 1 - mejora técnica importante

1. Propiedades del aire según temperatura, presión y altitud.
2. Strouhal dependiente del régimen, con `0,2` como valor inicial y no como constante universal.
3. Sensibilidad a Reynolds, rugosidad y turbulencia.
4. Límites de movimiento de la grapa y factores de seguridad configurables.
5. Interacción entre varios amortiguadores.

### Prioridad 2 - modelos avanzados

1. Matrices de transferencia para conductor-amortiguador.
2. `EJmin/EJmax` y deslizamiento interhebras.
3. Haces, tensión diferencial, modos acoplados y matrices de separadores.
4. Corrección por correlación espacial y *lock-in* cuando existan datos suficientes.

## Cambios que no se recomiendan

- No reemplazar globalmente `St = 0,2` por `0,185`.
- No aplicar factores ENDESA a los 101 ejemplos ya calibrados.
- No presentar una curva genérica de Blevins como si fuera la función de potencia CIGRE del conductor.
- No estimar la eficiencia de un modelo de amortiguador únicamente por su masa, geometría o fotografía.
- No declarar equivalencia con TECNOSOFT sin matrices dinámicas y ensayos originales.

## Conclusión

Los libros confirman la dirección general del desarrollo, pero también confirman que el cálculo genérico actual es todavía un modelo preliminar. La mejora más importante no es cambiar una constante: es introducir datos dinámicos medidos, convenciones inequívocas y trazabilidad. CIGRE debe gobernar el cálculo; IEC debe gobernar el ensayo; ENDESA y Blevins deben funcionar como capas de comprobación y diagnóstico.
