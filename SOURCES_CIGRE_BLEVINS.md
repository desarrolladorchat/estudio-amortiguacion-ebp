# Uso de los documentos adicionales

## CIGRE Green Books

Se incorporaron al modelo los conceptos que el documento identifica para el EBP:

- potencia eolica como funcion de amplitud adimensional y frecuencia;
- autoamortiguamiento como ley empirica `Pself/L = k*y0^l*f^p*T^q`;
- numero de Reynolds `Re = V*D/nu`;
- numero de Strouhal `St = f*D/V`;
- numero de Scruton `Sc = delta*m/(rho*D^2)`;
- caracter no lineal de la interaccion conductor-amortiguador;
- necesidad de curvas de impedancia, rigidez dinamica o potencia medidas.

El programa ahora permite incluir en el JSON los campos `cigre_k`, `cigre_l`, `cigre_p` y `cigre_q`. Si `cigre_k` es mayor que cero, se utiliza esa ley; de lo contrario se mantiene la formulacion Mosdorfer anterior.

## Blevins, Flow-Induced Vibration

Se usa como referencia de los calculos aerodinamicos de desprendimiento de vortices y de la relacion entre frecuencia, velocidad, diametro, Reynolds y Strouhal. El programa calcula `wind_speed_m_s` y `reynolds` para cada frecuencia del barrido.

Estos libros no proporcionan por si solos la curva especifica de disipacion de los amortiguadores SD/AMG/SPA. Para cerrar el balance con un amortiguador real siguen siendo necesarios ensayos de potencia o impedancia del fabricante.
