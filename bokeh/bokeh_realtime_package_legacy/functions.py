from bokeh.plotting import figure, curdoc
from bokeh.driving import count
from bokeh.models import ColumnDataSource, Range1d
import random
from datetime import datetime,time
from iertools.tb import TB
import pandas as pd

def define_period(time):
    period = pd.Timedelta(time)

    return period

def do_plot():
    dummy=pd.DataFrame(data={'ts':[],'temperature':[]})
    dummy.set_index('ts',inplace=True)

    source1 = ColumnDataSource(dummy)
    source2 = ColumnDataSource(dummy)
    source3 = ColumnDataSource(dummy)
    source4 = ColumnDataSource(dummy)
    source5 = ColumnDataSource(dummy)

    p = figure(x_axis_type='datetime',plot_width=1200, plot_height=400)
    p.y_range = Range1d(-1.3,1.3)
    p.x_range = Range1d(-0.2,10.2)

    return p,source1,source2,source3,source4,source5

def realtime(correction,publish_time):
    tmp0= TB(config_file='config_co2.ini',device_name='Test')
    sensor = "temperature"

    fecha1=datetime.now()+correction-publish_time
    fecha2=datetime.now()+correction
    termopares = tmp0.get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2)

    return termopares

def indexing_update(test,indicador):
    nindex = [indicador+1]
    nvalues = [test.temperature[0]]
    tmpd0 = pd.DataFrame(data=[nindex,nvalues])
    tmpd0 = tmpd0.T
    tmpd0.columns = ['ts','temperature']
    tmpd0.set_index('ts',inplace=True)

    return tmpd0

def reindexing_update(test,indicador):
    nindex = [indicador]
    nvalues = [test.temperature[0]]
    tmpd0 = pd.DataFrame(data=[nindex,nvalues])
    tmpd0 = tmpd0.T
    tmpd0.columns = ['ts','temperature']
    tmpd0.set_index('ts',inplace=True)

    return tmpd0

def last_actual_exchange(data):
    new = pd.DataFrame(data=data)
    new.set_index('ts',inplace=True)
    prueb = pd.DataFrame({'ts':[0],'temperature':[new.temperature[10]]})
    prueb.set_index('ts',inplace=True)

    return prueb,new


def historical(act_initial,nperiod,period,correction,publish_time):
    tmp0= TB(config_file='config_co2.ini',device_name='Test')
    sensor = "temperature"
    fecha2=datetime.now()+correction-publish_time
    fecha1=fecha2-(nperiod*period)
    memory = tmp0.get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2)
    cafe = pd.concat([act_initial,memory])
    nindex = []
    nvalues = []
    for i in range(len(memory),-1,-1):
        nindex.append(cafe.index[i])
        nvalues.append(cafe.temperature[i])
    cafe = pd.DataFrame(data=[nindex,nvalues])
    cafe = cafe.T
    cafe.columns = ['ts','temperature']
    cafe.set_index('ts',inplace=True)

    return cafe

def historical_mult(act_initial,nperiod,period,correction,publish_time,p):
    fecha = datetime.now()
    if fecha.second <= 9:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,0))
    elif fecha.second <= 19:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,10))
    elif fecha.second <= 29:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,20))
    elif fecha.second <= 39:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,30))
    elif fecha.second <= 49:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,40))
    elif fecha.second <= 59:
        lim = datetime.combine(fecha,time(fecha.hour,fecha.minute,50))
    tmp0= TB(config_file='config_co2.ini',device_name='Test')
    sensor = "temperature"
    fecha2=lim+correction+pd.Timedelta(str(fecha.second)+'s')
    fecha1=lim+correction-(4*period)
    memory = tmp0.get_df(key=sensor,start_datetime=fecha1,end_datetime=fecha2)
    fecha_sup = lim-pd.Timedelta('1H')
    d5 = memory.truncate(after=fecha_sup-3*period+pd.Timedelta('1s'))
    d4 = memory.truncate(before=fecha_sup-3*period-pd.Timedelta('0.5s'),after=fecha_sup-2*period+pd.Timedelta('0.5s'))
    d3 = memory.truncate(before=fecha_sup-2*period-pd.Timedelta('0.5s'),after=fecha_sup-period+pd.Timedelta('0.5s'))
    d2 = memory.truncate(before=fecha_sup-period-pd.Timedelta('0.5s'),after=fecha_sup+pd.Timedelta('0.5s'))
    d1 = memory.truncate(before=fecha_sup)

    global_index = [0,1,2,3,4,5,6,7,8,9,10]
    tmpd1 = pd.concat([act_initial,d1])
    nindex = []
    nvalues = []
    for i in range(0,len(tmpd1),1):
        nindex.append(global_index[i])
        nvalues.append(tmpd1.temperature[i])
    tmpd1 = pd.DataFrame(data=[nindex,nvalues])
    tmpd1 = tmpd1.T
    tmpd1.columns = ['ts','temperature']
    tmpd1.set_index('ts',inplace=True)

    nvalues = []
    for i in range(len(d2)-1,-1,-1):
        nvalues.append(d2.temperature[i])
    tmpd2 = pd.DataFrame(data=[global_index,nvalues])
    tmpd2 = tmpd2.T
    tmpd2.columns = ['ts','temperature']
    tmpd2.set_index('ts',inplace=True)

    nvalues = []
    for i in range(len(d3)-1,-1,-1):
        nvalues.append(d3.temperature[i])
    tmpd3 = pd.DataFrame(data=[global_index,nvalues])
    tmpd3 = tmpd3.T
    tmpd3.columns = ['ts','temperature']
    tmpd3.set_index('ts',inplace=True)

    nvalues = []
    for i in range(len(d4)-1,-1,-1):
        nvalues.append(d4.temperature[i])
    tmpd4 = pd.DataFrame(data=[global_index,nvalues])
    tmpd4 = tmpd4.T
    tmpd4.columns = ['ts','temperature']
    tmpd4.set_index('ts',inplace=True)

    nvalues = []
    for i in range(len(d5)-1,-1,-1):
        nvalues.append(d5.temperature[i])
    tmpd5 = pd.DataFrame(data=[global_index,nvalues])
    tmpd5 = tmpd5.T
    tmpd5.columns = ['ts','temperature']
    tmpd5.set_index('ts',inplace=True)

    return tmpd1.index[0],tmpd1,tmpd2,tmpd3,tmpd4,tmpd5

def line_with_points(figure,data_source):

    line = figure.line(x='ts', y='temperature',source=data_source, color="firebrick", line_width=2)
    points = figure.circle(x='ts',y='temperature',source=data_source,color='black')

    return line, points

def mult_lines(figure,data_source2,data_source3,data_source4,data_source5):

    line2 = figure.line(x='ts', y='temperature',source=data_source2, color="gray",alpha=0.5, line_width=2)
    line3 = figure.line(x='ts', y='temperature',source=data_source3, color="gray",alpha=0.4, line_width=2)
    line4 = figure.line(x='ts', y='temperature',source=data_source4, color="gray",alpha=0.3, line_width=2)
    line5 = figure.line(x='ts', y='temperature',source=data_source5, color="gray",alpha=0.2, line_width=2)

    return line2,line3,line4,line5
