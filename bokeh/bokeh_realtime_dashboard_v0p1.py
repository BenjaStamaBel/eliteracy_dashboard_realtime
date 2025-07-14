# myplot.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import count
from bokeh.models import ColumnDataSource, Range1d
import random
from datetime import datetime
from iertools.tb import TB
import pandas as pd

dummy=pd.DataFrame(data={'ts':[],'temperature':[]})
dummy.set_index('ts',inplace=True)

source = ColumnDataSource(dummy)
    
p = figure(x_axis_type='datetime',plot_width=1200, plot_height=400)
p.y_range = Range1d(-1.05,1.05)
now = datetime.now() - pd.Timedelta('1h') - pd.Timedelta('40s')
limit = now + pd.Timedelta('1m')
#p.x_range = Range1d(now,limit)

sel = 0
print(now)
@count()
def update(var):
    global sel
    global source
        
    tmp0= TB(config_file='config_co2.ini',device_name='Test')
    sensor = "temperature"
    fecha1=datetime.now()+pd.Timedelta('4H')+pd.Timedelta('59m')+pd.Timedelta('50s')
    fecha2=datetime.now()+pd.Timedelta('7H')
    termopares = tmp0.get_df(key="temperature",start_datetime=fecha1,end_datetime=fecha2)
    
    if sel == 0:
        tmp0= TB(config_file='config_co2.ini',device_name='Test')
        fecha1=datetime.now()+pd.Timedelta('4H')+pd.Timedelta('35m')+pd.Timedelta('10s')
        fecha2=datetime.now()+pd.Timedelta('4H')+pd.Timedelta('59m')+pd.Timedelta('50s')
        memory = tmp0.get_df(key="temperature",start_datetime=fecha1,end_datetime=fecha2)

        print('\nfirst')
        sel = 1
        cafe = pd.concat([termopares,memory])
        nindex = []
        nvalues = []
        for i in range(len(memory),-1,-1):
            nindex.append(cafe.index[i])
            nvalues.append(cafe.temperature[i])
        cafe = pd.DataFrame(data=[nindex,nvalues])
        cafe = cafe.T
        cafe.columns = ['ts','temperature']
        cafe.set_index('ts',inplace=True)
    else:
        cafe=termopares

    #roll_over == len(memory)
    source.stream(cafe,rollover=149)
    print(sel)

r1 = p.line(x='ts', y='temperature',source=source, color="firebrick", line_width=2)
p1 = p.circle(x='ts',y='temperature',source=source,color='black')
curdoc().add_root(p) 

##Milisegundos de unidades
curdoc().add_periodic_callback(update, 10000)