import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from datetime import datetime, timedelta, time
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, ColumnDataSource, LinearAxis, Range1d, Toggle, Slider, DatetimeTickFormatter, Select, Tabs, TabPanel, HoverTool, CrosshairTool, Span
from bokeh.layouts import row, column, gridplot, layout
from bokeh.driving import count

archivo = "../data/edificio_este/edificio_este.csv"

nombres= np.genfromtxt(archivo,max_rows=1,dtype="U",delimiter=',')

for i,nombre in enumerate(nombres):
    print(i,nombre)

zones=['N1AU401','N1AU402','N1AU403','N1AU404','N2AU101','N2AU102','N2AU103','N2AU201','N2AU202','N2AU203','N2PASILLO','N2STR','PBADM','PBATENCIONCOFI','PBCOORCOFI','PBCOORDINACION','PBDUCTOCOFI','PBDUCTOSALAS','PBDUCTOSCOM','PBIMP','PBSCOM','PBSJUNTAS','PBSMAESTROS','PBSTR','PBVESTIBULO']
zMAT=range(2,27,1)
zRAH=range(27,52,1)
nombres[0]='time'
nombres[1]='T_out'
for i in range(len(zones)):
    nombres[zMAT[i]]='Ti_'+zones[i]
    nombres[zRAH[i]]='RH_'+zones[i]

def eplus_fileimport(archivo):
    tmp = pd.read_csv(archivo,names=nombres,skiprows=1)
    tmp.time = tmp.time.str.replace('24:00:00','23:59:59')
    tmp.time = '2019 '+ tmp.time
    tmp.time = pd.to_datetime(tmp.time,format='%Y %m/%d %H:%M:%S')
    tmp['datetime']=tmp.time
    tmp.set_index('time',inplace=True)
    return tmp

simulation = eplus_fileimport(archivo)

five_days = simulation.truncate(after='2019-01-03 23:59:59')

ti_zones=nombres[zMAT]
rh_zones=nombres[zRAH]

#Data source 
source=ColumnDataSource(five_days)

#Figura 1 Temperatura al interior
#tooltips=[('Space','$name'),('Temperature','$y °C'),('Date','@x')]
height = Span(dimension="height", line_width=1)
crosshair = CrosshairTool(overlay=height)
p = figure(width=940, height=614,x_axis_type=None)
#p.y_range = Range1d(15.,35.)
p.yaxis.axis_label = "Temperature [°C]"
hover1 = HoverTool(
    tooltips=[
        ('Space','$name'),
        #('Temperature','$y °C'),
        ('Date','@datetime{%H:%M}')
    ]
)
#hover1.tooltips = [('Space','$name'),('Temperature','$y °C'),('Date','@$x')]
hover1.formatters = {'@datetime':'datetime'}
hover1.line_policy = 'nearest'
hover1.mode = 'mouse'
p.add_tools(hover1)
p.add_tools(crosshair)
for zona in zones:
    if 'AU' in zona:
        p.line(y='Ti_'+zona,x='time',source=source,line_color='blue',name=zona)
    else:
        p.line(y='Ti_'+zona,x='time',source=source,line_color='green',name=zona)
#p.legend.click_policy = 'hide'
#p.legend.label_text_font_size = '5pt'
#show(p)

#Figura 2 Humedad Relativa
#tooltips2 =[('Space','$name'),('Relative Humidity','$y %'),('Date','@x')]
p2 = figure(width=940,height=306,x_range=p.x_range,x_axis_type='datetime')
p2.yaxis.axis_label = 'Relative Humidity [%]'
#HoverTool.formatters={}
hover2 = HoverTool(
    tooltips=[
        ('Space','$name'),
        #('Relative Humidity','$y %'),
        ('Date','@datetime{%H:%M}')
    ]
)
#hover1.tooltips = [('Space','$name'),('Temperature','$y °C'),('Date','@$x')]
hover2.formatters = {'@datetime':'datetime'}
p2.add_tools(hover2)
p2.add_tools(crosshair)
for zona in zones:
    if 'AU' in zona:
        p2.line(y='RH_'+zona,x='time',source=source,line_color='blue',name=zona)
    else:
        p2.line(y='RH_'+zona,x='time',source=source,line_color='green',name=zona)
#p2.legend.click_policy='hide'
#p2.legend.label_text_font_size = '5pt'
g1=gridplot([[p],[p2]],toolbar_location='right',merge_tools=True)
