from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Range1d, RadioGroup, CustomJS, HoverTool, CrosshairTool, Span
import random
from datetime import datetime,time
from iertools.tb import TB
import pandas as pd
from bokeh_realtime_packagev2.conditions import *
from dateutil.parser import parse

def do_plots(dict):
    dict.update({'ts':[]})
    dummy=pd.DataFrame(data=dict)
    dummy.set_index('ts',inplace=True)
    dummy2 = pd.DataFrame(data={'names':[],'valuesco2':[],'valuesdb':[],'subs':[],'us':[],'sobs':[]})
    dummy3 = pd.DataFrame(data={'names':[],'valuesco2':[],'valuesdb':[],'subs':[],'us':[],'sobs':[]})

    source1 = ColumnDataSource(dummy)
    source2 = ColumnDataSource(dummy2)
    source3 = ColumnDataSource(dummy3)

    #Figura 1 Temperatura al interior
    #tooltips=[('Space','$name'),('Temperature','$y °C'),('Date','@x')]
    height = Span(dimension="height", line_width=1)
    # width = Span(dimension="width", line_width=0.5)
    crosshair = CrosshairTool(overlay=height)
    p = figure(width=1225, height=614,x_axis_type=None,margin=(0,600,0,0),toolbar_location=None)
    p.y_range = Range1d(16.,27.)
    p.yaxis.axis_label = "Temperature [°C]"
    hover1 = HoverTool(
        tooltips=[
            ('Space','$name'),
            #('Temperature','$y °C'),
            ('Hour','@datetime{%H:%M}')
        ]
    )
    #hover1.tooltips = [('Space','$name'),('Temperature','$y °C'),('Date','@$x')]
    hover1.formatters = {'@datetime':'datetime'}
    hover1.line_policy = 'nearest'
    hover1.mode = 'mouse'
    p.add_tools(hover1)
    p.add_tools(crosshair)

    #Figura 2 Humedad Relativa
    #tooltips2 =[('Space','$name'),('Relative Humidity','$y %'),('Date','@x')]
    p2 = figure(width=1200,height=306,x_range=p.x_range,x_axis_type='datetime',toolbar_location=None)
    p2.yaxis.axis_label = 'Relative Humidity [%]'
    #HoverTool.formatters={}
    hover2 = HoverTool(
        tooltips=[
            ('Space','$name'),
            #('Relative Humidity','$y %'),
            ('Hour','@datetime{%H:%M}')
        ]
    )
    #hover1.tooltips = [('Space','$name'),('Temperature','$y °C'),('Date','@$x')]
    hover2.formatters = {'@datetime':'datetime'}
    p2.add_tools(hover2)
    p2.add_tools(crosshair)

    #Figura de selección de modelo
    models = ["Humphreys & Nicol", "Humphreys", "Griffiths"]

    radio_group = RadioGroup(labels=models, active=0,width=5,width_policy='fixed',margin=(0,0,0,-600))
    radio_group.js_on_event('button_click', CustomJS(code="""
        console.log('radio_group: active=' + this.origin.active, this.toString())
    """))

    #Figura de grados hora
    #GHDC = (edificio.Ti_N1AU401[edificio.Ti_N1AU401>edificio.lsc]-edificio.Tn).sum()*(1./6.)
    #ghdc = Div(width=200,margin=(0,0,0,150),width_policy='fixed')
    #ghdc.text = '<span style="font-size: 12pt;">Grados hora de disconfort cálido</span><br>' + str(GHDC)

    #Figura de lista de zonas
    p3 = figure(width=680,toolbar_location=None,tooltips='',x_range=Range1d(0,6),margin=(-500,0,0,30))

    #Occupation dashboard

    p_o = figure(height=300,toolbar_location=None, tools="",width=603,margin=(0,0,0,0))
    p_o.xgrid.grid_line_color = None
    p_o.x_range.start = 400
    p_o.x_range.end=500
    p_o.xaxis.axis_label= 'CO2 concentration [ppm]'
    p_o.yaxis.major_label_text_align='right'
    p_o.varea(x=exceed_co2,y1=0,y2=10,color='red',alpha=0.2)
    p_o.varea(x=warning_co2,y1=0,y2=10,color='yellow',alpha=0.2)
    p_o.varea(x=adequate_co2,y1=0,y2=10,color='green',alpha=0.2)

    p2_o = figure(height=300,width=553,toolbar_location=None,y_axis_location='right', tools="",margin=(0,0,0,15))
    p2_o.xgrid.grid_line_color = None
    p2_o.x_range.start = 115
    p2_o.x_range.end=0
    p2_o.xaxis.axis_label = 'Sound levels [dB]'
    p2_o.yaxis.major_label_text_color='white'
    p2_o.yaxis.major_label_standoff = 0
    p2_o.yaxis.major_label_text_font_size = '0.5pt'
    p2_o.varea(x=exceed_dB,y1=0,y2=10,color='red',alpha=0.2)
    p2_o.varea(x=warning_dB,y1=0,y2=10,color='yellow',alpha=0.2)
    p2_o.varea(x=adequate_dB,y1=0,y2=10,color='green',alpha=0.2)

    p5_o = figure(height=300,width=550,toolbar_location=None, tools="",x_axis_type=None,x_range=p_o.x_range,margin=(0,0,0,55))
    p5_o.xgrid.grid_line_color = None
    p5_o.yaxis.visible = True
    p5_o.varea(x=exceed_co2,y1=0,y2=10,color='red',alpha=0.2)
    p5_o.varea(x=warning_co2,y1=0,y2=10,color='yellow',alpha=0.2)
    p5_o.varea(x=adequate_co2,y1=0,y2=10,color='green',alpha=0.2)

    p6_o = figure(height=300,width=550,toolbar_location=None, tools="",y_axis_location='right',x_axis_type=None,x_range=p2_o.x_range,margin=(0,0,0,15))
    p6_o.xgrid.grid_line_color = None
    p6_o.x_range.start = 115
    p6_o.x_range.end=0
    p6_o.yaxis.major_label_text_color = 'white'
    p6_o.yaxis.major_label_standoff = 0
    p6_o.yaxis.major_label_text_font_size = '0.5pt'
    p6_o.varea(x=exceed_dB,y1=0,y2=10,color='red',alpha=0.2)
    p6_o.varea(x=warning_dB,y1=0,y2=10,color='yellow',alpha=0.2)
    p6_o.varea(x=adequate_dB,y1=0,y2=10,color='green',alpha=0.2)

    p3_o = figure(width=1915,height=306,x_axis_type='datetime',toolbar_location=None)
    p3_o.yaxis.axis_label = 'CO2 concentration [ppm]'

    p7_o=figure(height=300,width=550,toolbar_location=None, tools="",x_axis_type=None,margin=(0,0,0,53))
    p7_o.x_range.start = 0
    p7_o.x_range.end =100

    p4_o=figure(height=300,width=603,toolbar_location=None, tools="",x_range=p7_o.x_range,margin=(0,0,0,0))
    p4_o.x_range.start = 0
    p4_o.x_range.end = 100
    p4_o.xaxis.axis_label = 'Percentage of surfaces [%]'

    df=pd.DataFrame()
    df['x']=np.ones(10)*0.5
    df['y']=np.array([0.38,1.48,2.58,3.68,4.8,5.9,7,8.1,9.2,10.3])
    df['text']=[str(num)+'%' for num in perce]

    p8_o = figure(height=300,toolbar_location=None, tools="",width=40,margin=(0,0,0,0),y_range=Range1d(0,11))
    p8_o.yaxis.visible = False
    p8_o.xaxis.visible = False
    p8_o.grid.visible = False

    p9_o = figure(height=300,toolbar_location=None, tools="",width=40,margin=(0,0,0,0),y_range=Range1d(0,11))
    p9_o.yaxis.visible = False
    p9_o.xaxis.visible = False
    p9_o.grid.visible = False

    return p,p2,radio_group,p3,p7_o,p6_o,p5_o,p9_o,p4_o,p2_o,p_o,p8_o,p3_o,source1,source2,source3


def realtime(correction,publish_time,sensors):
    tmps = [TB(config_file='config_bokeh.ini',device_name=name) for name in dthis];

    actual=pd.DataFrame()
    fecha1=datetime.now()+correction-publish_time
    fecha2=datetime.now()+correction
    for i in range(len(tmps)):
        memory = pd.concat([tmps[i].get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2).resample('5min').mean() for sensor in sensors[i]],axis=1)
        actual = pd.concat([memory,actual],axis=1)

    actual2=pd.DataFrame(index=pd.Index(data=aulas_n,name='names'))
    actual2['valuesco2']=actual[co2_zones_au].values.reshape(10)
    actual2['valuesdb']=actual[dB_zones_au].values.reshape(10)
    actual2['subs']=actual[sub_zones_au].values.reshape(10)
    actual2['us']=actual[u_zones_au].values.reshape(10)
    actual2['sobs']=actual[sob_zones_au].values.reshape(10)
    

    actual3=pd.DataFrame(index=pd.Index(data=others_n,name='names'))
    actual3['valuesco2']=actual[co2_zones_others].values.reshape(10)
    actual3['valuesdb']=actual[dB_zones_others].values.reshape(10)
    actual3['subs']=actual[sub_zones_au].values.reshape(10)
    actual3['us']=actual[u_zones_au].values.reshape(10)
    actual3['sobs']=actual[sob_zones_au].values.reshape(10)
 

    return actual,actual2,actual3


def historical(correction,publish_time,sensors):
    tmps = [TB(config_file='config_bokeh.ini',device_name=name) for name in dthis];

    total=pd.DataFrame()
    fecha2=datetime.now()+correction-publish_time
    day = str(datetime.now().day)
    month = str(datetime.now().month)
    year = str(datetime.now().year)
    fecha1=parse(year+'-'+month+'-'+day+' 00:00:00')+correction
    for i in range(len(tmps)):
        memory = pd.concat([tmps[i].get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2).resample('5min').mean() for sensor in sensors[i]],axis=1)
        total = pd.concat([memory,total],axis=1)

    return total

