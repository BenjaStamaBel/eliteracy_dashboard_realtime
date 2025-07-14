# myplot.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import count
import random
from datetime import datetime
from iertools.tb import TB
import pandas as pd



tmp0= TB(config_file='config_gbv.ini',device_name='Termopares cafe')



p = figure(x_axis_type='datetime',plot_width=400, plot_height=400)
r1 = p.line([], [], color="firebrick", line_width=2)

ds1 = r1.data_source

@count()
def update(var):
    sensores_cafe = ["Thermocouple_1","Thermocouple_10","Thermocouple_11",
            "Thermocouple_12","Thermocouple_2","Thermocouple_3",
            "Thermocouple_4","Thermocouple_5","Thermocouple_6",
            "Thermocouple_7","Thermocouple_8","Thermocouple_9"]
    fecha1=datetime.now()-pd.Timedelta('30s')
    fecha2=datetime.now()
    termopares = pd.concat([tmp0.get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2).resample('30s').mean() for sensor in sensores_cafe],axis=1)
    tmp = []
    for i in range(len(termopares.index)):
        tmp.append(termopares.iloc[i].mean())
    
    termopares['Ti'] = tmp

    cafe = termopares
#    source = ColumnDataSource(data=cafe)
    
    ds1.data['x'].append(cafe.index)
    ds1.data['y'].append(cafe['Ti'])
    ds1.trigger('data', ds1.data, ds1.data)

curdoc().add_root(p)

##Milisegundos de unidades
curdoc().add_periodic_callback(update, 40000)