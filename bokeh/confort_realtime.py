from bokeh.plotting import curdoc
from bokeh.driving import count
from bokeh.models import Button
from bokeh.layouts import gridplot
from datetime import datetime,time
import pandas as pd
from bokeh_realtime_packagev1.functions import *
from bokeh_realtime_packagev1.conditions import *

p,p2,source1 = do_plots(zones)
data = historical(pd.Timedelta('1.2m'),correction,publish_time,sensors)
source1.data = data
dates = source1.data['ts']
date_min=dates[0]
date_max_p=dates[0]+pd.Timedelta('2.4m')
date_max=date_max_p.to_numpy()
p.x_range.start = date_min
p.x_range.end = date_max
print('Inicio')


@count()
def update(var):
    global source1,maxs,mins
    actual = realtime(correction,publish_time,sensors)
    source1.stream(actual,rollover=160)
    print('Loop!')

p.line(y='Ti_N1AU401',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N1AU402',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N1AU403',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N1AU404',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU101',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU102',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU103',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU201',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU202',x='ts',source=source1,line_color='blue')
p.line(y='Ti_N2AU203',x='ts',source=source1,line_color='blue')

p.line(y='Ti_N1LAB',x='ts',source=source1,line_color='red')
p.line(y='Ti_N2LAB1',x='ts',source=source1,line_color='red')
p.line(y='Ti_N2LAB2',x='ts',source=source1,line_color='red')

p.line(y='Ti_PBADM',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBATENCIONCOFI',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBCAFE',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBCOCINA',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBCOORCOFI',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBCOORDINACION',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBSJUNTAS',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBSMAESTROS',x='ts',source=source1,line_color='green')
p.line(y='Ti_PBVESTIBULO',x='ts',source=source1,line_color='green')

p2.line(y='RH_N1AU401',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N1AU402',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N1AU403',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N1AU404',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU101',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU102',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU103',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU201',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU202',x='ts',source=source1,line_color='blue')
p2.line(y='RH_N2AU203',x='ts',source=source1,line_color='blue')

p2.line(y='RH_N1LAB',x='ts',source=source1,line_color='red')
p2.line(y='RH_N2LAB1',x='ts',source=source1,line_color='red')
p2.line(y='RH_N2LAB2',x='ts',source=source1,line_color='red')

p2.line(y='RH_PBADM',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBATENCIONCOFI',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBCAFE',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBCOCINA',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBCOORCOFI',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBCOORDINACION',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBSJUNTAS',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBSMAESTROS',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBVESTIBULO',x='ts',source=source1,line_color='green')


ghdc = Div(width=200,margin=(5,-230,5,-500),width_policy='fixed')
ghdc.text = 'Grados hora de disconfort cálido<br>'
  
but = Button()

maxs = [source1.data[sensor].max().round(2) for sensor in ti_sensors]
maxs.sort()
mins = [source1.data[sensor].min().round(2) for sensor in ti_sensors]
mins.sort()

def cb():
    tabla1.text = '''<table border=1>
    <tr>
        <th scope="col">T max [°C]</th>
        <th scope="col">Espacio</th>
        <th scope="col">HR [%]</th>
        <th scope="col">Open area vent [%]</th>
    </tr>

    <tr>
        <td>'''+str(maxs[-1])+'''</td>
        <td>PBVESTIBULO</td>
        <td>22</td>
        <td>32</td>
    </tr>

    <tr>
        <td>'''+str(maxs[-2])+'''</td>
        <td>PBCOORCOFI</td>
        <td>18</td>
        <td>5</td>
    </tr>

    <tr>
        <td>'''+str(maxs[-3])+'''</td>
        <td>PBSMAESTROS</td>
        <td>13</td>
        <td>45</td>
    </tr>
    </table>'''

    tabla2.text = '''<table border=1>
    <tr>
        <th scope="col">T min [°C]</th>
        <th scope="col">Espacio</th>
        <th scope="col">HR [%]</th>
        <th scope="col">Open area vent [%]</th>
    </tr>

    <tr>
        <td>'''+str(mins[0])+'''</td>
        <td>PBATENCIONCOFI</td>
        <td>25</td>
        <td>80</td>
    </tr>

    <tr>
        <td>'''+str(mins[1])+'''</td>
        <td>N2AU201</td>
        <td>20</td>
        <td>60</td>
    </tr>

    <tr>
        <td>'''+str(mins[2])+'''</td>
        <td>N2AU202</td>
        <td>19</td>
        <td>75</td>
    </tr>
    </table>'''

but.on_click(cb)

tabla1 = Div(width=900,margin=(-530,-230,5,5)) 
tabla1.text = '''<table border=1>
<tr>
    <th scope="col">T max [°C]</th>
    <th scope="col">Espacio</th>
    <th scope="col">HR [%]</th>
    <th scope="col">Open area vent [%]</th>
</tr>

<tr>
    <td>'''+str(maxs[-1])+'''</td>
    <td>PBVESTIBULO</td>
    <td>22</td>
    <td>32</td>
</tr>

<tr>
    <td>'''+str(maxs[-2])+'''</td>
    <td>PBCOORCOFI</td>
    <td>18</td>
    <td>5</td>
</tr>

<tr>
    <td>'''+str(maxs[-3])+'''</td>
    <td>PBSMAESTROS</td>
    <td>13</td>
    <td>45</td>
</tr>
</table>'''


tabla2 = Div(width=900,width_policy='fixed',margin=(-400,-230,5,-670))
tabla2.text = '''<table border=1>
<tr>
    <th scope="col">T min [°C]</th>
    <th scope="col">Espacio</th>
    <th scope="col">HR [%]</th>
    <th scope="col">Open area vent [%]</th>
</tr>

<tr>
    <td>'''+str(mins[0])+'''</td>
    <td>PBATENCIONCOFI</td>
    <td>25</td>
    <td>80</td>
</tr>

<tr>
    <td>'''+str(mins[1])+'''</td>
    <td>N2AU201</td>
    <td>20</td>
    <td>60</td>
</tr>

<tr>
    <td>'''+str(mins[2])+'''</td>
    <td>N2AU202</td>
    <td>19</td>
    <td>75</td>
</tr>
</table>'''

models = ["Humphreys & Nicol", "Humphreys", "Griffiths"]

radio_group = RadioGroup(labels=models, active=0,width=5,width_policy='fixed',margin=(5,5,5,5))
radio_group.js_on_event('button_click', CustomJS(code="""
    console.log('radio_group: active=' + this.origin.active, this.toString())
"""))

d = Div(text="start")

b = Button()

def cb1(): d.text = "end"
b.on_click(cb1)


g1=gridplot([[p,radio_group,ghdc,but],[p2,tabla1,tabla2,d,b]],toolbar_location='right',merge_tools=True)

curdoc().add_root(g1)
curdoc().add_periodic_callback(update,3000)