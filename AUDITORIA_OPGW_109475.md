# Auditoria del simulador frente al estudio OPGW 109475

## Conclusion

El simulador web implementa un prototipo EBP, pero no reproduce aun los resultados de TECNOSOFT III con precision suficiente para emitir un estudio de ingenieria. Puede utilizarse para exploracion cualitativa, no para validar una pauta de amortiguacion.

## Datos extraidos del estudio

- OPGW 48G625 / 48G652-AST-80.
- Diametro: 11.8 mm.
- Masa lineal: 0.36 kg/m.
- EDS: 7.25 kN.
- Rigidez EI: 43.68 N m2.
- Exponente de longitud de onda: 4.35.
- Exponente de amplitud: 2.35.
- Coeficiente de amortiguamiento: 11712.82 para 7.25 kN.
- Turbulencia: 2 %; funcion de viento Variable-2.
- Limite: 150 microstrain 0-pico.
- Amortiguador: 4D-20 (ZTT), factor de seguridad 1.5.
- Primera posicion: 0.70 m; posiciones siguientes separadas 0.58 m.

El anexo A sin amortiguadores muestra T=9.66 kN, coeficiente 10147.1 y deformacion maxima 532 microstrain. Esto no coincide con el EDS 7.25 kN del cuerpo principal y debe aclararse con el proveedor.

## Resultados objetivo

| Caso | TECNOSOFT |
|---|---:|
| Sin amortiguadores | 532 microstrain en grapa |
| Vano 80 m, 2 amortiguadores | 41 microstrain en grapa; 47 en grapa de amortiguador |
| Vano 530 m, 6 amortiguadores | 40 microstrain en grapa; 79 en grapa de amortiguador |

## Prueba del simulador actual

Se introdujeron D=11.8 mm, masa=0.36 kg/m, T=9.66 kN, EI=43.68 N m2, H=10147.1, n=4.35, m=2.35 y barrido 10-120 Hz.

| Vano introducido | Resultado web | Diferencia respecto de 532 |
|---:|---:|---:|
| 80 m | 196.1 microstrain | -63.1 % |
| 530 m | 903.6 microstrain | +69.8 % |

La deformacion sin amortiguadores no deberia cambiar de esta forma solamente por modificar el vano cuando las potencias de viento y autoamortiguamiento se expresan y escalan de manera consistente.

## Causas identificadas

1. La web multiplica la potencia eolica por la longitud del vano, pero no escala de la misma manera el autoamortiguamiento del conductor.
2. La deformacion se estima mediante curvatura sinusoidal simple. Los antecedentes usan una expresion con tension, rigidez EI y un factor K dependiente de la longitud de onda y del conductor.
3. La web representa la potencia del amortiguador como `coeficiente * f * U_D^2`. El modelo documentado emplea `P_D = 2*pi^2*f^2*U_D^2*|Z|*cos(psi)` o curvas experimentales equivalentes.
4. No se dispone de la impedancia, fase o curva de potencia del 4D-20. Sin esos datos no pueden reproducirse los resultados 41/47 y 40/79 microstrain.
5. La web no calcula separadamente deformacion en la grapa del apoyo y en cada grapa de amortiguador con la distorsion local de la onda.
6. No esta implementada la funcion de viento `Variable-2` para turbulencia del 2 %; se usa la curva IEC con un multiplicador escalar.
7. No esta aplicado el factor de seguridad 1.5 sobre la potencia medida del amortiguador.
8. El estudio usa amplitudes y deformaciones 0-pico; la web mezcla amplitud pico-pico para el balance con conversiones aproximadas de deformacion.

## Datos necesarios para una replica validable

- Curvas del amortiguador 4D-20: modulo de impedancia y fase frente a frecuencia y velocidad de grapa, o potencia disipada medida.
- Definicion y coeficientes de la funcion de viento TECNOSOFT `Variable-2` al 2 % de turbulencia.
- Convencion de unidades del parametro `Damping (Joules)`.
- Formula o tabla del factor K para transformar amplitud en deformacion de grapa.
- Confirmacion de por que el anexo A usa 9.66 kN y el resto del estudio 7.25 kN.
