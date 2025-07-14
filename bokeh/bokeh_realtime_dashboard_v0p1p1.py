# myplot.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import count
from bokeh.models import ColumnDataSource, Range1d
import random
from datetime import datetime
from iertools.tb import TB
import pandas as pd
from bokeh_realtime_package.functions import *
from bokeh_realtime_package.conditions import *

#Inicia el código

#Declarar figura y data source principal    
p , source = do_plot()

#Definir periodo de la onda
period = define_period('10s')

sel = 0

@count()
def update(var):
    global sel
    global source
    global period
    global correction
    global roll_over

    #Datos en tiempo real    
    actual = realtime(correction,publish_time)
    
    if sel == 0:
        sel=1
        #Datos históricos
        cafe = historical(actual, 5, period, correction, publish_time)
    else:
        cafe=actual

    print(cafe)

    source.stream(cafe,rollover=51)

#Figuras a la gráfica
r1,p1 = line_with_points(p,source)

curdoc().add_root(p) 

##Milisegundos de unidades
curdoc().add_periodic_callback(update, 1000)