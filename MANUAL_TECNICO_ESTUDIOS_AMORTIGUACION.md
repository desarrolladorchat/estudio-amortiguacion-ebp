# Manual técnico para estudios de amortiguación de conductores y cables de guardia

## Vibración eólica, principio de balance de energía, selección de amortiguadores y revisión de ingeniería

**Versión:** 1.0  
**Fecha:** 23-07-2026  
**Ámbito:** conductores simples, OPGW, cables de guardia y, con restricciones, conductores en haz  
**Jerarquía técnica principal:** CIGRE - IEC - datos de ensayo - experiencia de proyecto

> **Advertencia profesional**
>
> Este manual explica cómo preparar, calcular y revisar un estudio de amortiguación. No sustituye la especificación contractual, los certificados de ensayo, las curvas dinámicas del fabricante ni la aprobación del ingeniero responsable. Un catálogo que solo informa masa, dimensiones y rango de grapa no permite calcular la potencia disipada por un amortiguador.

---

## Índice

1. [Objeto y alcance](#1-objeto-y-alcance)
2. [Jerarquía de documentos y criterios](#2-jerarquía-de-documentos-y-criterios)
3. [Fenómenos inducidos por viento](#3-fenómenos-inducidos-por-viento)
4. [Nomenclatura y convenciones](#4-nomenclatura-y-convenciones)
5. [Parámetros aerodinámicos y climáticos](#5-parámetros-aerodinámicos-y-climáticos)
6. [Parámetros mecánicos del cable](#6-parámetros-mecánicos-del-cable)
7. [Modelo de onda y frecuencias](#7-modelo-de-onda-y-frecuencias)
8. [Principio de balance de energía](#8-principio-de-balance-de-energía)
9. [Autoamortiguamiento del conductor](#9-autoamortiguamiento-del-conductor)
10. [Amortiguadores Stockbridge](#10-amortiguadores-stockbridge)
11. [Separadores y separadores-amortiguadores](#11-separadores-y-separadores-amortiguadores)
12. [Deformación, fatiga y límites](#12-deformación-fatiga-y-límites)
13. [Tensión de diseño, EDS y parámetro H/w](#13-tensión-de-diseño-eds-y-parámetro-hw)
14. [Posición y cantidad de amortiguadores](#14-posición-y-cantidad-de-amortiguadores)
15. [Procedimiento completo de cálculo](#15-procedimiento-completo-de-cálculo)
16. [Datos mínimos de entrada](#16-datos-mínimos-de-entrada)
17. [Interpretación de gráficos y resultados](#17-interpretación-de-gráficos-y-resultados)
18. [Ejemplos calculados](#18-ejemplos-calculados)
19. [Lecciones de los estudios suministrados](#19-lecciones-de-los-estudios-suministrados)
20. [Criterios de revisión de ingeniería](#20-criterios-de-revisión-de-ingeniería)
21. [Errores frecuentes](#21-errores-frecuentes)
22. [Estructura recomendada de un informe](#22-estructura-recomendada-de-un-informe)
23. [Referencias](#23-referencias)
24. [Anexos](#24-anexos)

---

## 1. Objeto y alcance

El propósito de un estudio de amortiguación es establecer, para cada vano o familia de vanos:

- si el conductor puede operar sin amortiguamiento exterior;
- qué tipo de amortiguador o separador-amortiguador es adecuado;
- cuántas unidades deben instalarse;
- en qué extremos y a qué distancias;
- qué niveles de deformación, amplitud y movimiento de grapa resultan;
- qué margen existe respecto de los límites de fatiga y del accesorio;
- bajo qué tensión, temperatura, clima y configuración es válida la pauta.

El método principal tratado es el **Principio de Balance de Energía**, EBP por *Energy Balance Principle*. El EBP es especialmente aplicable a vibración eólica de pequeña amplitud y frecuencia relativamente alta.

Este manual no debe usar un único modelo para fenómenos diferentes:

| Fenómeno | Frecuencia típica orientativa | Amplitud | Mecanismo dominante | Tratamiento |
|---|---:|---:|---|---|
| Vibración eólica | aproximadamente 3 a 150 Hz | fracciones de diámetro a aproximadamente 1 diámetro | desprendimiento alternado de vórtices | EBP, Stockbridge, autoamortiguamiento |
| Oscilación de subvano | aproximadamente 0,5 a 10 Hz | varios diámetros | estela de subconductores de barlovento | modelo modal de haz y separadores |
| Galope | aproximadamente 0,1 a 3 Hz | metros | inestabilidad aerodinámica con hielo o sección asimétrica | estudio aeroelástico específico |

Los rangos son orientativos. No constituyen límites normativos universales.

---

## 2. Jerarquía de documentos y criterios

Cuando dos fuentes difieran, se recomienda la siguiente prioridad:

1. Requisitos contractuales y normativa vigente del proyecto.
2. **CIGRE Green Book, *Modelling of Vibrations of Overhead Line Conductors*** para arquitectura física y limitaciones del EBP.
3. **IEC 61897** para requisitos y ensayos de amortiguadores de vibración eólica.
4. **IEC 62567** para ensayo del autoamortiguamiento del conductor.
5. Datos medidos del conductor, amortiguador, separador y herrajes.
6. CIGRE TB 273 para tensión segura respecto de vibración eólica.
7. Estudios TECNOSOFT, ATTRA, ESANAM y otros informes aportados, como banco de comparación.
8. ENDESA y Mosdorfer para criterios históricos y comprobaciones complementarias.
9. Blevins para aerodinámica general, Reynolds, Strouhal, turbulencia y *lock-in*.

### 2.1 Qué regula IEC 61897

IEC 61897 cubre requisitos y ensayos de amortiguadores, entre ellos:

- dimensiones, materiales, masa y acabado;
- galvanizado y calidad de fabricación;
- par de instalación y deslizamiento de grapa;
- fijación entre grapa y cable mensajero;
- corona y radiointerferencia cuando corresponde;
- impedancia, fase y potencia disipada;
- eficacia del sistema;
- fatiga del amortiguador.

IEC 61897 **no es por sí sola un manual completo de diseño EBP**. Para OPGW, la edición vigente permite que comprador y proveedor acuerden la aplicación y los detalles técnicos.

### 2.2 Ediciones

- IEC 61897:1998 fue usada por muchos informes históricos y contiene una función de potencia eólica en su Anexo C.
- IEC 61897:2020 reemplazó la edición de 1998.
- Un informe nuevo debe declarar la edición contractual.
- Si se conserva el Anexo C de 1998 para reproducir un cálculo histórico, debe indicarse expresamente.

---

## 3. Fenómenos inducidos por viento

### 3.1 Formación de vórtices

El flujo transversal alrededor de un cable produce desprendimiento alternado de vórtices. La fuerza transversal periódica puede excitar modos propios del vano.

La frecuencia de desprendimiento se aproxima mediante:

$$
f_s = St\frac{V_\perp}{D}
$$

donde:

- $f_s$: frecuencia de desprendimiento, Hz;
- $St$: número de Strouhal;
- $V_\perp$: velocidad de viento perpendicular al vano, m/s;
- $D$: diámetro exterior efectivo, m.

De forma inversa:

$$
V_\perp = \frac{f_s D}{St}
$$

En documentación histórica ENDESA se usa con frecuencia $St=0{,}185$. En análisis modernos no debe imponerse como constante universal: conviene comprobar Reynolds, rugosidad, turbulencia y datos del proyecto. Valores del orden de 0,18 a 0,22 son habituales en el régimen subcrítico de cilindros, pero el valor definitivo debe trazarse.

### 3.2 Condición de resonancia

La vibración aumenta cuando la frecuencia de desprendimiento coincide con una frecuencia modal del vano. El sistema real tiene muchos modos, por lo que el análisis se realiza sobre una banda de frecuencias y no en un único punto.

### 3.3 Daño

La falla no depende solo del máximo instantáneo. Es un problema de fatiga acumulada:

$$
D_f=\sum_i \frac{n_i}{N_i}
$$

donde $n_i$ es el número de ciclos aplicado a un nivel y $N_i$ el número de ciclos hasta falla en la curva S-N correspondiente. La regla de Miner suele considerar falla acumulativa cuando $D_f$ se aproxima a 1, pero existe dispersión importante.

Los puntos más sensibles son:

- salida de grapas de suspensión;
- salida de amarres o retenciones;
- borde de varillas de protección;
- grapas de amortiguadores;
- grapas de separadores;
- puntos con fretting entre alambres.

---

## 4. Nomenclatura y convenciones

### 4.1 Variables principales

| Símbolo | Variable | Unidad SI |
|---|---|---:|
| $L$ | longitud del vano | m |
| $D$ | diámetro exterior del cable | m |
| $m$ | masa lineal | kg/m |
| $w=mg$ | peso lineal | N/m |
| $T$ o $H$ | tensión horizontal inicial | N |
| RTS o UTS | carga de rotura | N |
| $EJ$ o $EI$ | rigidez a flexión | N m² |
| $f$ | frecuencia | Hz |
| $\omega=2\pi f$ | frecuencia angular | rad/s |
| $\lambda$ | longitud de onda | m |
| $y_0$ | amplitud 0-pico de antinodo | m |
| $Y_{pp}=2y_0$ | amplitud pico a pico | m |
| $\varepsilon$ | deformación unitaria | microstrain o adimensional |
| $P_w$ | potencia suministrada por el viento | W |
| $P_c$ | potencia disipada por el conductor | W |
| $P_d$ | potencia disipada por amortiguador | W |
| $Z=F/V$ | impedancia mecánica traslacional | N s/m |
| $\phi$ | fase entre fuerza y velocidad | grados o rad |
| $\rho$ | densidad del aire | kg/m³ |
| $\mu$ | viscosidad dinámica | Pa s |
| $\nu=\mu/\rho$ | viscosidad cinemática | m²/s |

### 4.2 Convenciones de amplitud

Este es uno de los errores más frecuentes.

| Convención | Símbolo recomendado | Relación |
|---|---|---|
| 0-pico | $y_0$ | valor máximo desde el eje |
| Pico a pico | $Y_{pp}$ | $Y_{pp}=2y_0$ |
| RMS sinusoidal | $y_{rms}$ | $y_{rms}=y_0/\sqrt{2}$ |

IEC 61897:1998 usa en la función de potencia del viento una amplitud de antinodo **pico a pico** $Y$. CIGRE expresa con frecuencia $y_0$ como 0-pico. Toda entrada y todo gráfico deben indicar la convención.

### 4.3 Deformación

$$
1\ \text{microstrain}=1\ \mu\varepsilon=10^{-6}
$$

Los informes suministrados usan normalmente valores 0-pico. No deben compararse directamente con un límite pico a pico sin convertir.

---

## 5. Parámetros aerodinámicos y climáticos

### 5.1 Número de Reynolds

$$
Re=\frac{\rho V_\perp D}{\mu}=\frac{V_\perp D}{\nu}
$$

Interpretación:

- relaciona fuerzas inerciales y viscosas;
- afecta Strouhal, estela y potencia eólica;
- depende de diámetro, velocidad, temperatura, presión y altitud;
- la rugosidad de alambres y varillas puede modificar la transición.

No debe escribirse $Re=vD/\mu$ si $v$ es velocidad y $\mu$ es viscosidad dinámica sin incluir densidad. La forma $VD/\nu$ usa viscosidad cinemática.

### 5.2 Propiedades del aire

Para aire seco:

$$
\rho=\frac{p}{R_a T_a}
$$

con $R_a\approx287{,}05\ \text{J/(kg K)}$ y temperatura absoluta $T_a$.

La viscosidad puede estimarse mediante Sutherland:

$$
\mu(T)=\mu_0\left(\frac{T}{T_0}\right)^{3/2}\frac{T_0+S}{T+S}
$$

Valores de referencia alrededor de 15 °C y nivel del mar:

- $\rho\approx1{,}225\ \text{kg/m}^3$;
- $\mu\approx1{,}81\times10^{-5}\ \text{Pa s}$;
- $\nu\approx1{,}48\times10^{-5}\ \text{m}^2/\text{s}$.

La altitud reduce la densidad. Usar siempre temperatura y presión del sitio cuando se requiera una evaluación independiente.

### 5.3 Turbulencia

$$
I_t=\frac{\sigma_V}{\overline V}
$$

El EBP estacionario simple suele representar una condición casi laminar y entrega una envolvente máxima. CIGRE advierte que la turbulencia, la variación espacial y temporal del viento y la correlación de la estela generan incertidumbre.

Valores típicos de CIGRE TB 273, medidos a 10 m durante vientos fuertes:

| Terreno | $I_t$ típico |
|---|---:|
| Mar abierto o grandes superficies de agua | 0,11 |
| Campo abierto con pocos obstáculos bajos | 0,18 |
| Baja densidad urbana, suburbio o bosque abierto | 0,25 |
| Centro urbano, terreno quebrado con árboles altos | 0,35 |

Para los vientos ligeros asociados a vibración eólica, CIGRE informa dispersión mucho mayor. En terreno rural se han observado aproximadamente 0,07 a 0,50.

Los valores de 2 % o 7 % utilizados por algunos archivos TECNOSOFT deben interpretarse como parámetros de una función específica del software, no automáticamente como equivalentes directos a la intensidad de turbulencia meteorológica de TB 273.

### 5.4 Ángulo de ataque

Solo la componente perpendicular al vano excita directamente:

$$
V_\perp=V\lvert\sin\theta\rvert
$$

Un estudio de clima debe considerar distribución de dirección, no solo velocidad total.

### 5.5 Rugosidad, hielo y contaminación

- Alambres trenzados, varillas y depósitos alteran la rugosidad.
- Hielo o escarcha puede desplazar el problema hacia galope.
- Contaminación y corrosión pueden modificar fricción entre hebras, autoamortiguamiento y fatiga.
- Balizas esféricas y accesorios introducen nuevos puntos de concentración y cambian masa y aerodinámica.

Si se añaden balizas, el estudio original normalmente deja de ser aplicable.

---

## 6. Parámetros mecánicos del cable

### 6.1 Diámetro $D$

Afecta:

- relación frecuencia-viento;
- Reynolds;
- potencia eólica, que escala con $D^4$ en la formulación IEC;
- curvatura y deformación;
- selección de grapa.

Debe distinguirse:

- diámetro del cable desnudo;
- diámetro sobre varillas de protección;
- diámetro efectivo dentro de la grapa;
- diámetro aerodinámico si existen accesorios continuos.

### 6.2 Masa lineal $m$

Afecta velocidad de onda, frecuencia modal y parámetro de tensión:

$$
c\approx\sqrt{\frac{T}{m}}
$$

Debe incluir la masa real del cable. Para modelos locales pueden requerirse masas añadidas de varillas, grapas, separadores y amortiguadores.

### 6.3 Tensión

El valor utilizado en numerosos estudios es:

- tensión **inicial**;
- antes de creep;
- sin viento ni hielo;
- a la temperatura media del mes más frío o a la temperatura mínima contractualmente definida.

Debe informarse en kN. Si la tabla está en daN:

$$
1\ \text{daN}=10\ \text{N}
$$

La relación EDS o tensión porcentual:

$$
\text{EDS}(\%)=100\frac{T}{RTS}
$$

No basta con EDS. CIGRE recomienda comprobar también $H/w$.

### 6.4 Rigidez a flexión $EJ$

Un cable trenzado no tiene un único $EJ$ constante:

- $EJ_{max}$: sin deslizamiento entre hebras;
- $EJ_{min}$: deslizamiento interhebras desarrollado;
- el valor efectivo depende de amplitud, frecuencia, tensión, construcción y condición del cable.

El cálculo serio debe usar:

- curva medida, o
- intervalo $EJ_{min}$ a $EJ_{max}$ con análisis de sensibilidad.

No es adecuado calcular $EJ$ como el de una barra maciza del diámetro exterior.

### 6.5 Construcción y materiales

Registrar:

- tipo AAC, AAAC, ACAR, ACSR, acero, Alumoweld u OPGW;
- número, diámetro y material de alambres por capa;
- sentido de cableado;
- módulo elástico y coeficiente térmico;
- sección metálica;
- núcleo o tubo óptico;
- RTS;
- temperatura máxima;
- creep y pretensado.

### 6.6 Particularidades del OPGW

Además de la fatiga mecánica deben comprobarse:

- presión y ovalización bajo la grapa;
- atenuación óptica durante instalación y ensayo;
- radio de curvatura;
- temperatura de cortocircuito;
- compatibilidad galvánica;
- instalación sobre varillas adecuadas;
- sentido de cableado del OPGW y de los preformados;
- rango de deslizamiento y par de apriete.

---

## 7. Modelo de onda y frecuencias

### 7.1 Cuerda ideal

Para una cuerda sin rigidez:

$$
\lambda_0=\frac{1}{f}\sqrt{\frac{T}{m}}
$$

Las frecuencias naturales aproximadas de un vano de longitud $L$ son:

$$
f_n\approx\frac{n}{2L}\sqrt{\frac{T}{m}}
$$

### 7.2 Corrección por rigidez a flexión

La relación de dispersión de una cuerda-viga es:

$$
\omega^2=\frac{T}{m}k^2+\frac{EJ}{m}k^4
$$

con:

$$
k=\frac{2\pi}{\lambda},\qquad \omega=2\pi f
$$

Forma equivalente:

$$
f^2=\frac{T}{m\lambda^2}+\frac{4\pi^2EJ}{m\lambda^4}
$$

Definiendo $s=1/\lambda^2$:

$$
s=\frac{-T+\sqrt{T^2+16\pi^2EJmf^2}}{8\pi^2EJ}
$$

$$
\lambda=\frac{1}{\sqrt{s}}
$$

La rigidez es más importante a alta frecuencia y cerca de las grapas.

### 7.3 Forma ideal

Lejos de accesorios:

$$
y(x,t)=y_0\sin(kx)\sin(\omega t)
$$

Con amortiguadores la forma local se distorsiona. La aproximación sinusoidal sirve para exploración, pero no reemplaza una solución acoplada conductor-amortiguador cerca de la grapa.

---

## 8. Principio de balance de energía

En régimen estacionario, para cada frecuencia:

$$
P_w=P_c+\sum_i P_{d,i}+P_{otros}
$$

donde:

- $P_w$: potencia aerodinámica introducida;
- $P_c$: autoamortiguamiento del cable;
- $P_{d,i}$: potencia disipada por cada amortiguador;
- $P_{otros}$: terminaciones, separadores u otros elementos modelados.

El cálculo busca la amplitud que hace cero el residuo:

$$
R(Y)=P_w(Y)-P_c(Y)-\sum_iP_{d,i}(Y)
$$

Una solución numérica debe informar:

$$
\text{error relativo}=
\frac{|R|}{\max(P_w,P_c+\sum P_d,\epsilon)}
$$

Como criterio de control interno puede exigirse error menor que 2 %, sin convertir este valor en requisito normativo si el contrato no lo establece.

### 8.1 Potencia eólica IEC

IEC 61897:1998, Anexo C:

$$
P_w=L D^4 f^3\,fnc\left(\frac{Y_{pp}}{D}\right)
$$

La función reducida:

$$
fnc(r)=10^z
$$

$$
z=\sum_{n=0}^{8}a_nX^n,\qquad X=\log_{10}(r),\qquad r=\frac{Y_{pp}}{D}
$$

Coeficientes:

| $n$ | $a_n$ |
|---:|---:|
| 0 | -0,491949 |
| 1 | -11,8029 |
| 2 | -43,5532 |
| 3 | -78,5876 |
| 4 | -86,1199 |
| 5 | -58,1808 |
| 6 | -23,6082 |
| 7 | -5,26705 |
| 8 | -0,495885 |

> **Control de transcripción:** algunas extracciones OCR pierden el signo negativo de $a_1$. Con $a_1=-11{,}8029$ se obtienen, por ejemplo, $fnc(0{,}01)\approx0{,}00603$ y $fnc(0{,}10)\approx0{,}37087$.

### 8.2 Limitaciones

- La potencia es una función empírica.
- Existe dispersión entre túneles de viento y bases CIGRE.
- Reynolds, rugosidad, turbulencia y efectos tridimensionales influyen.
- El EBP calcula una respuesta estacionaria máxima; el viento real puede no mantener la condición el tiempo suficiente.
- CIGRE informa que la incertidumbre combinada de potencia eólica y autoamortiguamiento puede producir aproximadamente ±50 a ±60 % de variación en amplitud en ciertas condiciones.

Por ello deben calcularse envolventes, no solo una curva central.

---

## 9. Autoamortiguamiento del conductor

### 9.1 Origen físico

En cables trenzados, la disipación procede principalmente de:

- microdeslizamiento y fricción entre hebras;
- histéresis estructural;
- contribuciones aerodinámicas;
- efectos de terminación en ensayos cortos.

Aumentar la tensión normalmente reduce el autoamortiguamiento.

### 9.2 Ley empírica CIGRE

Una forma general:

$$
\frac{P_c}{L}=k\,y_0^{\,l}f^{\,m}T^{\,q}
$$

$q$ debe conservar el signo definido por la fuente. Muchas formulaciones escriben $T^{-n}$ con $n>0$:

$$
\frac{P_c}{L}=k\,y_0^{\,l}f^{\,m}T^{-n}
$$

Los coeficientes dependen de unidades y método de ensayo. No son transferibles entre SI, kgf, mm y m sin conversión completa.

Rangos observados en la literatura CIGRE, no valores genéricos de diseño:

| Método | Exponente de amplitud $l$ | Exponente de frecuencia $m$ |
|---|---:|---:|
| Power Test con extremos rígidos | cercano a 2,0 | cercano a 4,0 |
| ISWR o Power Test con extremos pivotados | aproximadamente 2,4 a 2,5 | aproximadamente 5,4 a 5,7 |

Las diferencias pueden cambiar la potencia calculada en un orden de magnitud.

### 9.3 Métodos IEC 62567

| Método | Medición | Ventaja | Riesgo |
|---|---|---|---|
| Power Method | fuerza, velocidad, fase en excitador | simple | incluye pérdidas parásitas y extremos |
| ISWR | amplitudes de nodo y antinodo | mide disipación del tramo | nodos muy pequeños son difíciles de medir |
| Decay Method | decaimiento libre | rápido y cubre amplitudes | puede incluir pérdidas del sistema |

Buenas prácticas:

- vano interior sin corrientes de aire;
- variación de temperatura controlada;
- tensión constante;
- preestirado de 12 a 48 h según el procedimiento;
- *running-in* para estabilizar el cable nuevo;
- calibración de transductores;
- al menos diez frecuencias o las definidas por el programa;
- corrección de pérdidas aerodinámicas y de terminación.

### 9.4 Dato TECNOSOFT “Damping (Joules)”

Los ejemplos muestran valores como 10.147,1; 14.088,06 o 29.427,15 junto con exponentes 4,35 y 2,35. Sin la definición de unidades y ecuación interna no debe tratarse ese número como energía física directamente comparable entre cables. Debe solicitarse:

- ecuación completa;
- convención de amplitud;
- unidades de tensión, longitud y masa;
- método de ensayo;
- rango de validez.

---

## 10. Amortiguadores Stockbridge

### 10.1 Componentes

- grapa;
- cable mensajero;
- masa grande;
- masa pequeña;
- tornillo, tuerca y arandelas;
- protección superficial.

La asimetría de masas y longitudes permite varias resonancias. Los modelos denominados “cuatro resonancias” buscan ampliar la banda útil.

### 10.2 Parámetros de catálogo

| Parámetro | Uso |
|---|---|
| Modelo y revisión | trazabilidad |
| Rango de grapa | compatibilidad con diámetro efectivo |
| Masa total | carga local, no eficiencia por sí sola |
| Masas y brazos | frecuencias modales |
| Diámetro y construcción del mensajero | rigidez, fatiga y disipación |
| L1 y L2 | geometría asimétrica |
| Par de apriete | seguridad frente a deslizamiento y daño |
| Temperatura | validez de materiales |
| Curva $Z(f,V)$ o $P(f,V)$ | cálculo EBP |
| Dispersión de fabricación | factor de diseño |
| Ensayos de fatiga y deslizamiento | aceptación |

Ejemplos del catálogo suministrado:

| Modelo | Grapa | Rango nominal | Masa | Mensajero | Par de referencia |
|---|---|---:|---:|---:|---:|
| AMG-030513 | G-13 | 7-13 mm | 1,225 kg | 7,8 mm | 30 N m |
| AMG-050926 | G-26 | 18-26 mm | 2,015 kg | 7,8 mm | 35 N m |
| AMG-091526 | G-26 | 18-26 mm | 3,125 kg | 9,3 mm | 35 N m |
| AMG-091534 | G-34 | 28-34 mm | 3,155 kg | 9,3 mm | 35 N m |
| AMG-152429 | G-29 | 21,5-29,5 mm | 4,565 kg | 11,9 mm | 35 N m |
| AMG-152440 | G-40 | 34-40 mm | 4,800 kg | 11,9 mm | 35 N m |

Los valores deben confirmarse con la revisión vigente del plano.

### 10.3 Impedancia y potencia

Con velocidad pico de grapa $V_d$:

$$
Z(f,V_d)=\frac{F}{V_d}
$$

$$
P_d=\frac{1}{2}F_{pk}V_{pk}\cos\phi
$$

$$
P_d=\frac{1}{2}V_{pk}^2\operatorname{Re}(Z)
=\frac{1}{2}V_{pk}^2|Z|\cos\phi
$$

Si se usa desplazamiento pico $U_d$:

$$
V_{pk}=2\pi fU_d
$$

$$
P_d=2\pi^2f^2U_d^2|Z|\cos\phi
$$

La fuerza alta no garantiza disipación. Si $\cos\phi$ es pequeño, la potencia real es baja.

### 10.4 Ensayo de características

IEC 61897:1998 especifica, salvo acuerdo diferente:

$$
f_{min}=\frac{0{,}18}{D},\qquad
f_{max}=\frac{1{,}4}{D}
$$

con $D$ en metros, y velocidad de grapa 0,1 m/s 0-pico para la caracterización de referencia.

Se obtienen:

- impedancia;
- fase;
- potencia disipada;
- frecuencias y potencias de resonancia.

En ensayo por muestra, la edición 1998 utiliza bandas alrededor de las resonancias y potencia mínima respecto del ensayo de tipo. La aceptación definitiva debe seguir la edición contractual vigente.

### 10.5 No linealidad y dispersión

CIGRE muestra que:

- la rigidez dinámica cambia con la velocidad de grapa;
- las resonancias se desplazan con amplitud;
- unidades del mismo modelo presentan dispersión;
- el amortiguador distorsiona localmente la onda;
- un modelo traslacional simple puede omitir fuerzas y momentos de rotación.

Por eso no debe estimarse $P_d$ desde masa, dimensiones o fotografía.

### 10.6 Factor de seguridad

Una forma conservadora de acreditar potencia:

$$
P_{d,diseño}=\frac{P_{d,medida}}{\gamma_d}
$$

Los estudios suministrados usan con frecuencia $\gamma_d=1{,}5$. No es un valor universal; debe justificarse por contrato, dispersión de ensayo y experiencia.

### 10.7 Movimiento de grapa

ENDESA registra como comprobación histórica para ciertos Stockbridge:

- máximo 2 mm 0-pico bajo 10 Hz;
- máximo 3 mm 0-pico sobre 10 Hz.

Estos valores no deben reemplazar el límite certificado del fabricante del modelo actual.

---

## 11. Separadores y separadores-amortiguadores

### 11.1 Separador rígido

Controla geometría del haz y esfuerzos de cortocircuito, pero puede no aportar disipación significativa.

### 11.2 Separador-amortiguador

Combina:

- control geométrico;
- articulaciones elastoméricas;
- rigidez y amortiguamiento traslacional y rotacional;
- disipación para vibración eólica y oscilación de subvano.

### 11.3 Datos requeridos

- número y disposición de subconductores;
- separación del haz;
- diámetro, masa y tensión de cada subconductor;
- tensión diferencial;
- longitudes de subvano;
- posición escalonada de separadores;
- matrices de rigidez, amortiguamiento o impedancia;
- propiedades de articulaciones;
- temperatura y envejecimiento;
- fuerzas de cortocircuito;
- aerodinámica de estela.

Un haz no debe reemplazarse por una masa y diámetro equivalentes escalares.

### 11.4 Parámetro de aplicabilidad CIGRE

CIGRE TB 273 utiliza:

$$
\frac{LD}{m}
$$

con unidades m³/kg, como parte de sus recomendaciones para haces con separadores. Varias reglas de TB 273 se limitan a:

$$
\frac{LD}{m}<15\ \text{m}^3/\text{kg}
$$

Debe verificarse la definición exacta de $m$ y el sistema de haz según la tabla aplicable.

### 11.5 Catálogo suministrado

El catálogo JSON actualmente utilizado por la aplicación contiene 178 registros, entre ellos:

- SP2: 26;
- SP3: 15;
- SP3-3: 10;
- familias SPA400/450 DA, TA y CA: 60;
- amortiguadores SD: 13;
- amortiguadores SAPREM AMG: 21;
- amortiguadores PLP VORTX: 21;
- PLP SVD: 2;
- Salvi 4M: 2;
- familias 4D, FR, FR3, FRY, Mosdorfer 9305 y separadores especiales.

La compatibilidad dimensional del separador no demuestra su comportamiento dinámico.

---

## 12. Deformación, fatiga y límites

### 12.1 Curvatura ideal

Para onda sinusoidal:

$$
\kappa_{max}=\left(\frac{2\pi}{\lambda}\right)^2y_0
$$

La deformación ideal de fibra exterior:

$$
\varepsilon_{ideal}=
\frac{D}{2}\left(\frac{2\pi}{\lambda}\right)^2y_0
$$

Esta expresión es útil lejos de grapas. Cerca de una condición de borde deben aplicarse modelos o factores medidos.

### 12.2 Punto de medición

La práctica histórica usa medición a 89 mm, equivalente a 3,5 pulgadas, desde el último punto de contacto de la grapa de suspensión. También deben distinguirse:

- deformación en el apoyo;
- deformación en la grapa del amortiguador;
- amplitud de antinodo;
- movimiento de grapa.

ENDESA muestra factores $K_1$, $K_2$ y $K_3$ para transformar amplitud ideal en deformación real considerando deslizamiento y borde. Estos factores deben proceder de ensayo, no fijarse arbitrariamente.

### 12.3 Varillas de protección

Los antecedentes históricos indican que las varillas pueden reducir significativamente la deformación local sin aumentar necesariamente la disipación total. Por tanto:

- no deben contarse automáticamente como amortiguador;
- cambian rigidez y condición de borde;
- modifican el diámetro de agarre;
- obligan a usar la geometría real en posición y compatibilidad.

### 12.4 Límites observados en los informes

| Capa exterior o criterio | Límite usado en ejemplos | Observación |
|---|---:|---|
| Aluminio o combinación con aluminio exterior | 150 microstrain 0-pico | frecuente en informes TECNOSOFT suministrados |
| Acero o ACS exterior | 225 microstrain 0-pico | usado en EA26-071314 y otros |
| Criterio histórico ENDESA conservador | 75 microstrain 0-pico | incluye factor de seguridad 2 |

Estos valores son criterios de proyecto observados, no límites universales de IEC.

### 12.5 Precaución con IEC 61897

IEC 61897:1998 lleva el conductor de ensayo a 150 microstrain 0-pico para evaluar eficacia. La norma aclara que ese valor es solo para el ensayo y **no está directamente relacionado con la esperanza de vida**. No debe justificarse un límite de fatiga diciendo solamente “IEC usa 150 microstrain”.

### 12.6 Criterio de aceptación

Un estudio debe comprobar por frecuencia:

$$
\varepsilon_{apoyo}(f)\leq\varepsilon_{lim,apoyo}
$$

$$
\varepsilon_{grapa,d}(f)\leq\varepsilon_{lim,grapa}
$$

$$
U_d(f)\leq U_{lim,fabricante}(f)
$$

Además:

- fatiga del mensajero;
- fuerza de grapa;
- deslizamiento;
- óptica en OPGW;
- dispersión e incertidumbre.

---

## 13. Tensión de diseño, EDS y parámetro H/w

### 13.1 Limitación de EDS

El criterio antiguo de 18 % RTS para ACSR no evitó todas las fallas. CIGRE TB 273 indica que la tensión porcentual por sí sola no refleja:

- peso lineal;
- terreno y turbulencia;
- vano;
- tipo de protección;
- fatiga acumulada;
- autoamortiguamiento.

### 13.2 Parámetro H/w

$$
\frac{H}{w}=\frac{H}{mg}
$$

La unidad es metro. Representa una medida mecánica de severidad de tensión.

### 13.3 CIGRE TB 273 para conductor simple sin protección

Tensión horizontal inicial, antes de creep, a la temperatura media del mes más frío:

| Categoría | Terreno | $(H/w)_{adm}$ |
|---:|---|---:|
| 1 | abierto, plano, sin obstáculos, nieve, agua extensa o desierto plano | 1000 m |
| 2 | abierto y plano, sin obstáculos ni nieve | 1125 m |
| 3 | abierto o suavemente ondulado, pocos obstáculos | 1225 m |
| 4 | urbano, arbolado, bosque o campos pequeños con barreras | 1425 m |

Si existen dudas se debe elegir la categoría más severa.

Estas recomendaciones no sustituyen el EBP cuando se instalan amortiguadores. Situaciones especiales requieren estudio:

- vanos extralargos;
- hielo o escarcha;
- alta temperatura;
- contaminación;
- accesorios o balizas;
- conductores no convencionales.

### 13.4 Sistemas amortiguados

Para conductor simple con amortiguadores Stockbridge en los extremos, TB 273 presenta:

$$
\frac{H}{w}<\frac{C_t}{(LD/m)^{0{,}12}}
$$

con:

$$
\frac{LD}{m}<15\ \text{m}^3/\text{kg}
$$

| Categoría de terreno | $C_t$ |
|---:|---:|
| 1 | 2615 |
| 2 | 2780 |
| 3 | 2860 |
| 4 | 3030 |

Ejemplo: para un conductor con $L=300$ m, $D=0{,}02$ m y $m=0{,}65$ kg/m:

$$
\frac{LD}{m}=\frac{300(0{,}02)}{0{,}65}=9{,}23\ \text{m}^3/\text{kg}
$$

En terreno categoría 2:

$$
\left(\frac{H}{w}\right)_{adm}
<
\frac{2780}{9{,}23^{0{,}12}}
\approx2130\ \text{m}
$$

La fórmula es una guía de tensión segura, no una selección automática del modelo, cantidad o posición del Stockbridge.

TB 273 también entrega límites específicos para haces:

| Sistema | Cat. 1 | Cat. 2 | Cat. 3 | Cat. 4 |
|---|---:|---:|---:|---:|
| Dúplex con separadores no amortiguantes | 1725 m | 1925 m | 2100 m | 2450 m |
| Dúplex con separadores-amortiguadores | 1900 m | 2200 m | 2500 m | 2500 m |
| Tríplex o cuádruplex con separadores no amortiguantes | 1850 m | 2100 m | 2275 m | 2500 m |
| Tríplex o cuádruplex con separadores-amortiguadores | 2500 m | 2500 m | 2500 m | 2500 m |

Para combinaciones de separadores no amortiguantes más Stockbridge existen reglas por tramos en función de $LD/m$. Debe consultarse la tabla completa del sistema; no es correcto aplicar el límite de conductor simple sin protección a un haz amortiguado.

---

## 14. Posición y cantidad de amortiguadores

### 14.1 Amplitud local aproximada

Para una onda no perturbada:

$$
U_d(f,x)\approx y_0(f)\left|\sin\left(\frac{2\pi x}{\lambda(f)}\right)\right|
$$

La posición óptima cambia con frecuencia. Por eso se busca un compromiso sobre toda la banda.

### 14.2 Estrategia por vanos

1. Calcular el conductor sin amortiguador.
2. Encontrar la longitud máxima que cumple por autoamortiguamiento.
3. Probar una unidad y optimizar distancia.
4. Aumentar el vano hasta perder cumplimiento.
5. Probar una unidad por extremo.
6. Para vanos largos, probar dos o más por extremo con solución acoplada.
7. Confirmar movimiento y fatiga del propio amortiguador.

La regla histórica “dos amortiguadores sirven para el doble de vano” es solo una aproximación inicial.

### 14.3 Referencias físicas de distancia

La pauta debe definir el origen:

- centro de grapa de suspensión;
- borde de grapa;
- extremo de varilla;
- final de retención preformada;
- eje de la grapa del amortiguador;
- distancia entre ejes.

No basta escribir “posición 0,60 m”.

### 14.4 Amarres preformados

Un amarre no tiene un empotramiento puntual idéntico al del modelo. Puede existir un pseudoempotramiento dependiente de frecuencia. Algunos informes SAPREM:

- modelan una unidad efectiva;
- añaden una segunda unidad a 80 mm del final de la retención;
- buscan garantizar que al menos una trabaje eficientemente.

Este criterio puede ser conservador, pero debe documentarse con:

- sensibilidad de posición;
- ensayo;
- experiencia de campo;
- o modelación equivalente de la retención y las dos unidades.

### 14.5 Tolerancia

Los ejemplos SAPREM especifican normalmente ±10 mm para Stockbridge. La tolerancia real debe proceder del plano vigente. En separadores, las tolerancias pueden ser del orden de decímetros y dependen del proyecto.

---

## 15. Procedimiento completo de cálculo

### Paso 1 - Clasificar el problema

- conductor simple, OPGW o haz;
- suspensión, amarre o combinación;
- con o sin varillas;
- balizas o accesorios;
- vibración eólica o subvano.

### Paso 2 - Validar entradas

Comprobar unidades, revisión documental, tensiones, longitudes y correspondencia exacta del cable.

### Paso 3 - Definir clima

- altitud, temperatura y presión;
- rugosidad y terreno;
- turbulencia;
- dirección del viento;
- intervalo de velocidad;
- hielo o contaminación.

### Paso 4 - Definir banda de frecuencia

Desde la banda de viento:

$$
f_{min}=St\frac{V_{min}}{D},\qquad
f_{max}=St\frac{V_{max}}{D}
$$

Comprobar además el intervalo de ensayo del amortiguador $0{,}18/D$ a $1{,}4/D$ cuando sea aplicable.

### Paso 5 - Caso sin amortiguadores

Resolver:

$$
P_w(Y)=P_c(Y)
$$

Obtener:

- amplitud;
- deformación;
- frecuencias peligrosas;
- velocidad y Reynolds;
- sensibilidad a $EJ$ y autoamortiguamiento.

### Paso 6 - Selección preliminar

Filtrar por:

- diámetro efectivo;
- conductor y material;
- frecuencia;
- temperatura;
- par;
- disponibilidad de curva dinámica.

### Paso 7 - Posición

Optimizar la distancia sobre toda la banda y todas las combinaciones de incertidumbre.

### Paso 8 - Caso amortiguado

Resolver:

$$
P_w=P_c+\sum_i\frac{P_{d,i}}{\gamma_{d,i}}
$$

Cuando existan varios amortiguadores cercanos debe usarse un modelo acoplado o una caracterización de conjunto.

### Paso 9 - Comprobaciones

- deformación en cada apoyo;
- deformación en cada grapa;
- movimiento de grapa;
- potencia y error de balance;
- fuerza y deslizamiento;
- fatiga del amortiguador;
- tensión y temperatura;
- óptica del OPGW;
- tolerancia de posición.

### Paso 10 - Sensibilidades mínimas

| Variable | Variación recomendada |
|---|---|
| $EJ$ | mínimo, central y máximo |
| autoamortiguamiento | curva baja, central y alta |
| potencia eólica | curvas o factores acordados |
| tensión | máxima inicial y casos relevantes |
| posición | tolerancia de montaje y pseudoempotramiento |
| amortiguador | dispersión de muestras |
| temperatura/aire | extremos de servicio relevantes |

### Paso 11 - Pauta por vano

La salida debe identificar cada vano real, no solo un rango genérico.

### Paso 12 - Control de campo

- instalación inmediata después del tendido y engrapado;
- par calibrado;
- posición medida;
- fotografía y registro;
- verificación de orientación;
- inspección posterior;
- medición de vibración en vanos críticos cuando corresponda.

---

## 16. Datos mínimos de entrada

### 16.1 Cable

- fabricante, modelo y revisión;
- diámetro y masa;
- RTS;
- construcción por capas;
- módulo y coeficiente térmico;
- sentido de cableado;
- $EJ_{min}$ y $EJ_{max}$;
- curva de autoamortiguamiento;
- límite de deformación y fuente;
- temperatura máxima;
- datos ópticos si es OPGW.

### 16.2 Vano

- torres inicial y final;
- longitud real;
- desnivel;
- tipo de apoyo A y B;
- tensión inicial por temperatura;
- ruling span;
- creep;
- varillas y herrajes;
- balizas;
- vano especial o cruce.

### 16.3 Clima

- elevación;
- temperatura;
- presión;
- terreno;
- turbulencia;
- velocidades y direcciones;
- hielo;
- contaminación.

### 16.4 Amortiguador

- referencia y revisión;
- rango de grapa;
- par;
- masa y geometría;
- mensajero;
- curva $Z(f,V)$, fase o $P(f,V)$;
- dispersión;
- límites de movimiento;
- fatiga y deslizamiento;
- temperatura.

### 16.5 Separadores

- modelo;
- matriz dinámica;
- posiciones;
- subvanos;
- rigidez y amortiguamiento;
- temperatura;
- cortocircuito.

---

## 17. Interpretación de gráficos y resultados

Un gráfico TECNOSOFT típico puede mostrar:

- negro: deformación máxima en apoyos;
- verde: deformación en grapa de amortiguador;
- rojo: movimiento de grapa, normalmente en eje derecho;
- azul: amplitud de antinodo o puntos equivalentes de velocidad.

Antes de aprobar:

1. Confirmar unidades de ambos ejes.
2. Confirmar 0-pico o pico a pico.
3. Identificar frecuencia del máximo.
4. Traducir frecuencia a viento.
5. Revisar toda la banda, no solo el máximo.
6. Verificar que la cantidad y posición impresas coincidan con el plano.
7. Comparar vano simulado y vano contractual.
8. Comprobar tensión, masa, diámetro y $EJ$ impresos.
9. Exigir tabla numérica si la escala oculta valores pequeños.
10. No interpretar una línea sobre el eje como cero físico exacto.

### 17.1 Tres niveles de validez

| Nivel | Descripción | Uso |
|---|---|---|
| Reproducción calibrada | digitaliza la curva del PDF | comparación y capacitación |
| Cálculo preliminar | usa fórmulas físicas con datos incompletos | sensibilidad, no contrato |
| EBP independiente validado | usa ensayos trazables y modelo verificado | diseño sujeto a revisión profesional |

---

## 18. Ejemplos calculados

### 18.1 OPGW 13,4 mm - EA26-071314

Datos:

- $D=0{,}0134$ m;
- $m=0{,}536$ kg/m;
- $T=15{,}42$ kN;
- RTS = 79,4 kN;
- $EJ=215{,}53$ N m²;
- máximo sin amortiguador a 40 Hz.

EDS:

$$
\text{EDS}=100\frac{15{,}42}{79{,}4}=19{,}42\%
$$

Con $St=0{,}185$:

$$
V=\frac{40(0{,}0134)}{0{,}185}=2{,}90\ \text{m/s}
$$

Con $\nu=1{,}5\times10^{-5}$ m²/s:

$$
Re=\frac{2{,}90(0{,}0134)}{1{,}5\times10^{-5}}\approx2588
$$

Longitud de onda con rigidez:

$$
\lambda\approx4{,}30\ \text{m}
$$

Parámetro de tensión:

$$
\frac{H}{w}=
\frac{15420}{0{,}536(9{,}80665)}
\approx2934\ \text{m}
$$

Este valor supera ampliamente 1000-1425 m para conductor simple sin protección de TB 273, confirmando la necesidad de protección o estudio específico.

Resultados del informe:

- sin amortiguadores: 263 microstrain a 14 Hz y 841 a 40 Hz;
- con AMG-050926: máximo aproximadamente 100 microstrain;
- límite adoptado: 225 microstrain.

Observación: la corrida usa 210 m y una unidad a 0,45 m por extremo; el plano instala dos por extremo a 0,08 y 0,53 m desde la retención.

### 18.2 OPGW 16,4 mm - EA26-071313

Datos:

- $D=16{,}4$ mm;
- $m=0{,}740$ kg/m;
- $T=20{,}91$ kN;
- $EJ=293{,}96$ N m²;
- límite 150 microstrain.

$$
\frac{H}{w}\approx2881\ \text{m}
$$

Resultados:

- 306 microstrain a 12 Hz;
- máximo 1055 a 39 Hz;
- sobre 150 hasta aproximadamente 118 Hz;
- con AMG-091526: máximo aproximadamente 104 en apoyo y 87 en grapa.

La grapa G-26 nominal es 18-26 mm. El cable desnudo tiene 16,4 mm; la compatibilidad depende del diámetro efectivo sobre varillas y debe demostrarse.

### 18.3 AAAC Cairo - documento 109475

Datos principales usados en los estudios:

- $D=19{,}88$ mm;
- $m\approx0{,}6502$ kg/m;
- $T=14{,}15$ kN;
- $EJ=190{,}73$ N m².

Pautas:

- vano 300 m: dos FR-2, uno por extremo;
- vano 550 m: cuatro FR-2, dos por extremo;
- primera unidad cerca de 1,30 m en suspensión y separación adicional aproximadamente 1,20 m.

Resultados publicados:

- aproximadamente 90 microstrain en apoyo;
- aproximadamente 35 microstrain en grapa del amortiguador.

La reproducción de estas curvas no permite recalcular otra posición sin la curva dinámica FR-2.

### 18.4 OPGW 11,8 mm con 4D-20

El documento 109475 presenta:

- $D=11{,}8$ mm;
- $m=0{,}36$ kg/m;
- $EJ=43{,}68$ N m²;
- límite 150 microstrain;
- primera posición 0,70 m y separación 0,58 m.

Existe una inconsistencia:

- cuerpo principal: tensión 7,25 kN;
- anexo sin amortiguadores: 9,66 kN.

Resultados:

- sin amortiguadores: 532 microstrain;
- vano 80 m con dos 4D-20: 41 en apoyo y 47 en grapa;
- vano 530 m con seis 4D-20: 40 en apoyo y 79 en grapa.

El estudio no debe aprobarse sin resolver qué tensión gobierna.

### 18.5 Conductor dúplex AAAC 1400 MCM - EA26-071311

- separadores sin Stockbridge: envolvente cercana a 510 microstrain;
- sistema SPA400DA35 + AMG-152440: aproximadamente 30 en apoyo y 13 en grapa de separador;
- el modelo de haz requiere matrices modales y dinámicas, no un conductor equivalente.

### 18.6 Cable Alumoweld 7 No. 8 - EA26-071312

- deformación máxima digitalizada aproximadamente 8 microstrain;
- no requiere amortiguamiento exterior para el caso simulado;
- la recomendación opcional de amortiguador debe distinguirse de una exigencia del cálculo.

---

## 19. Lecciones de los estudios suministrados

Los PDF revisados muestran patrones recurrentes:

| Lección | Ejemplo | Acción |
|---|---|---|
| tensión del texto y anexo puede diferir | OPGW 109475 | exigir una tabla maestra de entradas |
| vano contractual puede redondearse | EA26-071314: 207,3 vs 210 m | declarar y justificar |
| corrida y plano pueden tener distinta cantidad | EA26-071313/14 | modelar o justificar unidades adicionales |
| vano corto declarado sin amortiguador puede aparecer con unidades obligatorias | EA26-071313/14 | separar obligatorio de opcional |
| diámetro desnudo puede quedar fuera del rango de grapa | AMG sobre OPGW | comprobar diámetro sobre varillas |
| límite 150/225 depende del material y criterio | OPGW mixto vs ACS | citar fuente y convención |
| separadores solos pueden no controlar vibración | EA26-071311 | comprobar Stockbridge y dinámica del haz |
| masas del catálogo no definen eficiencia | todas las familias | solicitar $Z$, fase o potencia |
| gráficos digitalizados reproducen, no recalculan | banco web | etiquetar el modo |

---

## 20. Criterios de revisión de ingeniería

### 20.1 Hallazgos que impiden aprobación

- cable o tensión no coincide con tablas de tendido;
- no se identifica vano y apoyo;
- curvas sin cantidad o posición del amortiguador;
- pauta fuera del rango de vano simulado;
- deformación sobre límite;
- grapa incompatible;
- ausencia de justificación dinámica del modelo;
- unidades o amplitudes ambiguas;
- contradicción entre texto, tabla y plano;
- haz calculado como conductor escalar sin validación.

### 20.2 Hallazgos mayores

- falta de curva medida de autoamortiguamiento;
- falta de potencia/impedancia del amortiguador;
- edición normativa no indicada;
- clima y turbulencia no justificados;
- un solo $EJ$ sin sensibilidad;
- factores de seguridad no explicados;
- unidades adicionales no simuladas;
- vano redondeado sin análisis.

### 20.3 Hallazgos menores

- errores de nomenclatura;
- falta de tabla numérica;
- baja resolución gráfica;
- par de apriete solo indicado como “recomendado”;
- tolerancia no repetida en el plano.

### 20.4 Dictámenes sugeridos

| Dictamen | Condición |
|---|---|
| Conforme | datos, cálculo, plano y certificados consistentes |
| Aprobable con observaciones | correcciones documentales sin cambio de solución |
| Aprobable con observaciones mayores | solución plausible, pero falta trazabilidad o existe contradicción constructiva |
| Requiere recálculo | cambió cable, tensión, vano, herraje, clima o amortiguador |
| Rechazado | no cumple límites o no puede demostrarse |

---

## 21. Errores frecuentes

1. Usar kg/m como peso N/m.
2. Mezclar kgf, daN y kN.
3. Confundir diámetro desnudo con diámetro sobre varillas.
4. Introducir $EJ$ en N mm² cuando el programa espera N m².
5. Mezclar 0-pico y pico a pico.
6. Usar 150 microstrain de IEC como vida de fatiga universal.
7. Fijar $St=0{,}185$ sin revisar régimen.
8. Multiplicar potencia eólica por $L$ pero no autoamortiguamiento por longitud.
9. Acreditar potencia de amortiguador con masa o coeficiente arbitrario.
10. Sumar potencias de varios amortiguadores sin interacción.
11. Omitir el factor de seguridad sobre potencia.
12. Optimizar para una frecuencia aislada.
13. No modelar amarres, varillas o pseudoempotramiento.
14. Aplicar una pauta a vanos mayores que el máximo simulado.
15. Mantener una curva calibrada después de cambiar entradas y llamarla recálculo.
16. No revisar balizas y otros accesorios.
17. Aplicar un modelo simple a haz dúplex o cuádruplex.
18. No comprobar movimiento y fatiga del propio amortiguador.

---

## 22. Estructura recomendada de un informe

1. Portada, revisión y responsables.
2. Objeto y alcance.
3. Normas y fuentes.
4. Línea y tabla de vanos.
5. Cable y certificado.
6. Tensiones por vano y temperatura.
7. Clima, terreno y turbulencia.
8. Herrajes, varillas y balizas.
9. Amortiguador y certificados dinámicos.
10. Método de cálculo y convenciones.
11. Incertidumbres y factores de seguridad.
12. Caso sin amortiguamiento.
13. Optimización.
14. Casos amortiguados.
15. Tabla numérica de máximos.
16. Pauta por vano y por apoyo.
17. Plano con distancias, origen y tolerancia.
18. Par y procedimiento de instalación.
19. Limitaciones y condiciones que obligan a recalcular.
20. Anexos de ensayo y archivos de cálculo.

### 22.1 Tabla mínima de resultados

| Vano | f crítica | Viento | Re | $\varepsilon_A$ | $\varepsilon_B$ | $\varepsilon_d$ | $U_d$ | Cantidad | Posiciones | Estado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

---

## 23. Referencias

### 23.1 Principales

1. Giorgio Diana (ed.), *Modelling of Vibrations of Overhead Line Conductors*, CIGRE Green Books, 2018.
2. CIGRE Technical Brochure 273, *Overhead Conductor Safe Design Tension with Respect to Aeolian Vibrations*.
3. IEC 61897:1998, *Overhead lines - Requirements and tests for Stockbridge type aeolian vibration dampers*.
4. [IEC 61897:2020](https://webstore.iec.ch/en/publication/31840), *Overhead lines - Requirements and tests for Aeolian vibration dampers*.
5. [IEC 62567:2013](https://webstore.iec.ch/en/publication/7212), *Overhead lines - Methods for testing self-damping characteristics of conductors*.
6. Robert D. Blevins, *Flow-Induced Vibration*, 2nd ed.
7. ENDESA, *Vibraciones de conductores*, secciones 203-232.
8. Mosdorfer, *Wind-Induced Vibrations on High-Voltage Overhead Lines*.

### 23.2 Estudios usados como ejemplos

- EA26-071311, AAAC 1400 MCM dúplex.
- EA26-071312, Alumoweld 7 No. 8.
- EA26-071313, OPGW DNO-150172 de 16,4 mm.
- EA26-071314, OPGW ZTT de 13,4 mm.
- Anexo B EA16-042811.
- EA16-111644 / código interno EA16-111611.
- EA15-121816, ACAR 1000 MCM.
- EA15-1211818, OPGW.
- EC-90.0011, EC-90.0013, EC-90.0014 y EC-90.0016.
- Damping Scheme y Anti-Vibration Schedule 109475.
- Estudios AAAC Cairo, AAAC Flint, AAAC Greeley, ACAR 900 MCM y OPGW 11,8/12,8/13,6 mm.
- TR-739-E, TR-743-E, TR 792 y DOC No. 1058.
- Estudios LCHC, LAB, Mosdorfer y SAPREM suministrados.

---

## 24. Anexos

### Anexo A - Conversiones

| Magnitud | Conversión |
|---|---|
| 1 daN | 10 N |
| 1 kgf | 9,80665 N |
| 1 N m² | $10^6$ N mm² |
| 1 mm | $10^{-3}$ m |
| 1 microstrain | $10^{-6}$ |
| pico a pico | 2 x 0-pico |
| RMS sinusoidal | 0-pico / $\sqrt{2}$ |

### Anexo B - Ejemplo de archivo dinámico

```json
[
  {
    "frequency_hz": 10,
    "clamp_velocity_peak_m_s": 0.005,
    "power_mean_w": 0.02
  },
  {
    "frequency_hz": 10,
    "clamp_velocity_peak_m_s": 0.020,
    "power_mean_w": 0.25
  },
  {
    "frequency_hz": 30,
    "clamp_velocity_peak_m_s": 0.005,
    "power_mean_w": 0.03
  },
  {
    "frequency_hz": 30,
    "clamp_velocity_peak_m_s": 0.020,
    "power_mean_w": 0.40
  }
]
```

Debe acompañarse de:

- modelo y número de serie;
- método y laboratorio;
- temperatura;
- convención pico/RMS;
- incertidumbre;
- curva de fase;
- rango de frecuencia y velocidad;
- revisión y fecha.

### Anexo C - Lista rápida para terreno

- [ ] Modelo correcto.
- [ ] Grapa compatible con diámetro efectivo.
- [ ] Varillas correctas.
- [ ] Sentido y orientación correctos.
- [ ] Posición desde el origen definido.
- [ ] Separación entre ejes.
- [ ] Tolerancia cumplida.
- [ ] Par aplicado con herramienta calibrada.
- [ ] Sin daño en alambres ni cubierta.
- [ ] Registro fotográfico.
- [ ] Identificación de vano y apoyo.
- [ ] Instalación inmediata después de tendido.

### Anexo D - Regla de oro

> Un resultado de amortiguación solo es válido para la combinación de cable, tensión, vano, clima, herrajes, varillas, amortiguador, posición y función dinámica que fue realmente calculada o ensayada.

### Anexo E - Trazabilidad del corpus documental

La información de este manual se consolidó por función:

| Grupo documental | Uso en el manual |
|---|---|
| CIGRE Green Book | formulación EBP, incertidumbre, interacción conductor-amortiguador, haces y subvanos |
| CIGRE TB 273 | tensión segura, terreno, $H/w$ y $LD/m$ |
| IEC 61897 | caracterización, eficacia, deslizamiento, fatiga y potencia eólica |
| IEC 62567 | autoamortiguamiento, métodos Power, ISWR y Decay |
| Blevins | Reynolds, Strouhal, turbulencia, velocidad reducida y estela |
| ENDESA 203-232 | criterios históricos de posición, deformación, desplazamiento y seguridad |
| Mosdorfer Wind Induced Vibrations 001/002 | longitud de onda, balance, absorción y diseño de banda ancha |
| TECNOSOFT/SAPREM | entradas reales, límites, curvas y pautas de obra |
| ZTT, PLP, Mosdorfer, Salvi y otros fabricantes | familias de amortiguadores, programas de instalación y ensayos |
| Estudios de conductores simples, OPGW y cables de guardia | verificación de casos sin y con amortiguadores |
| Estudios AAAC/ACAR dúplex y cuádruplex | separadores, separadores-amortiguadores y limitaciones del modelo de haz |

Los informes particulares se usan como **casos de experiencia y regresión**, no como fuente normativa general. Cuando un informe no publica la función dinámica o el archivo original de cálculo, el manual conserva el resultado como referencia, pero no lo presenta como validación independiente.
