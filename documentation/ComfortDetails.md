#tesis/dashboard/comfort 
# Detalles de la pestaña de Confort térmico

En este documento se detallarán los bloques de la pestaña de confort térmico.
Este debe tener un criterio para que como primera gráfica aparezca un espacio aleatorio cada vez.

## Bloque 1 [[DashboardTabsDetails#^f3964f|Link]]
### Título: Gráfica temperatura vs. tiempo completa

### Concepto:
Esta gráfica tiene como objetivo mostrar el comportamiento térmico de distintos espacios en una misma gráfica.
Los espacios se muestran por tipo mediante un selector:
**Tipos:**
- Laboratorios
- Oficinas
- Aulas
(Checar coloreado de espacios)

### Parámetros
x-axis: Tiempo (datetime)
y-axis: Temperatura (°C)
period: 2/3 días (dato actual - 1/2 días)

### Componentes del bloque:
#### - Gráfica de temperatura
Hacer esta gráfica
Componentes:
1. La gráfica de temperatura muestra la temperatura al interior en cada uno de los espacios.
2. Cada espacio o cada tipo tiene un color en específico.
3. Leyenda con todos los tipos o espacios y su color particular (checar con el resaltado y coloreado).
4. Temperatura de referencia (sug. max y min instantáneas).
5. Líneas de confort con modelo adaptativo (seleccionar modelo).
6. Se coloca a la derecha del selector. [[#- Selector de tipo de espacios.|Selector]]
7. 

La gráfica muestra el comportamiento de la temperatura durante el periodo de análisis en todos los espacios. Al acercar el cursor muestra el valor del dato de temperatura y el nombre del espacio. 

#### - Gráfica de ventanas y ventilas
Detallar métricas
Ventilas únicamente en salones ('AU') - Ángulo de apertura traducir a área
Ventanas en salones ('AU') y oficinas - Distancia de apertura traducir a área

#### - Evaporativo
Detallar métricas

#### - Selector de tipo de espacios.
1. El selector tiene 3 opciones: Laboratorios, Aulas y Oficinas.
2. Se coloca del lado izquierdo de la gráfica principal. [[#- Gráfica de temperatura|Gráfica]]
3. 

El tipo de selector está en decisión ([RadioButtonGroup](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#radiobuttongroup),[RadioGroup](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#radiogroup),[Select](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#select),[CheckButtonGroup](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html#checkboxbuttongroup))
El selector se marca y se muestran los espacios correspondientes a cada tipo.

## Bloque 2 [[DashboardTabsDetails#^768a5a|Link]]
