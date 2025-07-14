# myplot.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import count
from bokeh.models import ColumnDataSource, Range1d
import random
from datetime import datetime,time
from iertools.tb import TB
import pandas as pd
from bokeh_realtime_package.functions import *
from bokeh_realtime_package.conditions import *

#Inicia el código

#Definir periodo de la onda
period = define_period('10s')

#Declarar figura y data source principal    
p , source1, source2, source3, source4, source5 = do_plot()


sel = 0

@count()
def update(var):
    global sel
    global source1,source2,source3,source4,source5
    global period
    global correction
    global roll_over
    global d1,d2,d3,d4,d5
    global indicador

    #Datos en tiempo real    
    actual = realtime(correction,publish_time)
    
    if sel == 0:
        sel=1
        #Datos históricos
        indicador,d1,d2,d3,d4,d5 = historical_mult(actual, 5, period, correction, publish_time,p)
        source2.stream(d2,rollover=11)
        source3.stream(d3,rollover=11)
        source4.stream(d4,rollover=11)
        source5.stream(d5,rollover=11)
        print(d1)
        print(d2)
    else:
        d1=indexing_update(actual,indicador)

    print(indicador)
    indicador=indicador+1

    if indicador == 11:
        indicador = 0
        source5.data = dict(source4.data)
        source4.data = dict(source3.data)
        source3.data = dict(source2.data)
        source1.data,source2.data = last_actual_exchange(source1.data)
        #source1.data = reindexing_update(actual,indicador)
    else:
        source1.stream(d1,rollover=11)

#Figuras a la gráfica
r1,p1 = line_with_points(p,source1)
r2,r3,r4,r5 = mult_lines(p,source2,source3,source4,source5)

curdoc().add_root(p) 

##Milisegundos de unidades
curdoc().add_periodic_callback(update, 1000)