import pandas as pd
import numpy as np
#import sweetviz as sv
import matplotlib.pyplot as plt
#import ipywidgets as widgets
#from datetime import datetime, timedelta, time
from bokeh import events
from bokeh.io import output_file, output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, ColumnDataSource, LinearAxis, Range1d, Toggle, Slider, DatetimeTickFormatter, Select, Tabs, TabPanel, HoverTool, CrosshairTool, Span, Div
from bokeh.layouts import row, column, gridplot, layout
#from bokeh.driving import count
# output_file('test.html')  # Render to static HTML, or
# output_notebook()  # Render inline in a Jupyter Notebook
#from icecream import ic
#pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns',None)

archivo = "../data/edificio_este/edificio_este.csv"

nombres= np.genfromtxt(archivo,max_rows=1,dtype="U",delimiter=',')

#for i,nombre in enumerate(nombres):
#    print(i,nombre)
ti_zones=[]
rh_zones=[]
all_zones=['N1AU401','N1AU402','N1AU403','N1AU404','N2AU101','N2AU102','N2AU103','N2AU201','N2AU202','N2AU203','N2PASILLO','N2STR','PBADM','PBATENCIONCOFI','PBCOORCOFI','PBCOORDINACION','PBDUCTOCOFI','PBDUCTOSALAS','PBDUCTOSCOM','PBIMP','PBSCOM','PBSJUNTAS','PBSMAESTROS','PBSTR','PBVESTIBULO']
zones=['N1AU401','N1AU402','N1AU403','N1AU404','N2AU101','N2AU102','N2AU103','N2AU201','N2AU202','N2AU203','PBADM','PBATENCIONCOFI','PBCOORCOFI','PBCOORDINACION','PBSJUNTAS','PBSMAESTROS','PBVESTIBULO']
zMAT=range(2,27,1)
zRAH=range(27,52,1)
nombres[0]='time'
nombres[1]='T_out'
for i in range(len(all_zones)):
    nombres[zMAT[i]]='Ti_'+all_zones[i]
    nombres[zRAH[i]]='RH_'+all_zones[i]
    if all_zones[i] in zones:
        ti_zones.append(nombres[zMAT[i]])
        rh_zones.append(nombres[zRAH[i]])
        
use_cols=[nombres[0],nombres[1]]+ti_zones+rh_zones
def eplus_fileimport(archivo):
    tmp = pd.read_csv(archivo,names=nombres,skiprows=1,usecols=use_cols)
    tmp.time = tmp.time.str.replace('24:00:00','23:59:59')
    tmp.time = '2019 '+ tmp.time
    tmp.time = pd.to_datetime(tmp.time,format='%Y %m/%d %H:%M:%S')
    tmp['datetime']=tmp.time
    tmp.set_index('time',inplace=True)
    return tmp

simulation = eplus_fileimport(archivo)

three_days = simulation.truncate(after='2019-01-03 23:59:59')

three_days['hour']=three_days.index.hour

#Data source 
source=ColumnDataSource(three_days)

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

def display_event(div, attributes=[]):
    """
    Function to build a suitable CustomJS to display the current event
    in the div model.
    """
    style = 'float: left; clear: left; font-size: 20px'
    return CustomJS(args=dict(div=div), code="""
        const attrs = %s;
        const args = [];
        for (let i = 0; i < attrs.length; i++) {
            const val = JSON.stringify(cb_obj[attrs[i]], function(key, val) {
                return val.toFixed ? Number(val.toFixed(2)) : val;
            })
            args.push('Temperature = ' + val)
        }
        const line = "<span style=%r>" + args.join() + "</span>\\n";
        const text = div.text.concat(line);
        const lines = text.split("\\n")
        if (lines.length > 35)
            lines.shift();
        div.text = lines.join("\\n");
    """ % (attributes, style))
line_attributes=['y']

div = Div(width=500)
# <b>" + cb_obj.event_name + "</b>
# p.js_on_event(events.Tap, display_event(div,attributes=line_attributes))
# p.js_on_event(events.MouseEnter, display_event(div, attributes=line_attributes))
# p.js_on_event(events.MouseLeave, display_event(div, attributes=line_attributes))


g1=gridplot([[p,div],[p2]],toolbar_location='right',merge_tools=True)

show(g1)