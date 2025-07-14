from bokeh.plotting import curdoc
from bokeh.driving import count
from bokeh.models import TabPanel,Tabs
from bokeh.layouts import layout
#from datetime import datetime,time
import pandas as pd
from bokeh_realtime_packagev2.functions import *
from bokeh_realtime_packagev2.conditions import *

p,p2,radio_group,p3,p7_o,p6_o,p5_o,p9_o,p4_o,p2_o,p_o,p8_o,p3_o,source1,source2,source3= do_plots(zones)
data = historical(correction,publish_time,all_sensors)
source1.data = data
dates = source1.data['ts']
date_min=dates[0]
date_max_p=dates[0]+pd.Timedelta('1D')
date_max=date_max_p.to_numpy()
p.x_range.start = date_min
p.x_range.end = date_max
p3_o.x_range.start = date_min
p3_o.x_range.end = date_max

# lists = pd.DataFrame()
# lists['zones']=spaces
# lists['ti']=[str(round(edificio['Ti_'+zone].iloc[100],1))+' °C' for zone in spaces]
# lists['rh']=[str(round(edificio['RH_'+zone].iloc[100],1))+' %' for zone in spaces]
# lists['aw']=[str(round(edificio['A_totW'+zone].iloc[100]+edificio['A_totV'+zone].iloc[100],1))+'m³' for zone in spaces]
# lists['x1']=np.ones(22)*0.1
# lists['x2']=np.ones(22)*2
# lists['x3']=np.ones(22)*3.53
# lists['x4']=np.ones(22)*5.1
# lists['y']=np.arange(22,0,-1)

# titles=pd.DataFrame()
# titles['zones']=['Zona']
# titles['ti']=['Temperatura al interior']
# titles['rh']=['Humedad Relativa']
# titles['aw']=['Área de ventanas abierta']
# titles['x1']=[0.1]
# titles['x2']=[2]
# titles['x3']=[3.53]
# titles['x4']=[5.1]
# titles['y']=[23]

# ploting=pd.concat([titles,lists])

# listed = ColumnDataSource(ploting)

print('Inicio')


@count()
def update(var):
    global source1,source2,source3
    actual,actual2,actual3 = realtime(correction,publish_time,all_sensors)
    source1.stream(actual,rollover=288)
    source2.stream(actual2,rollover=10)
    source3.stream(actual3,rollover=10)
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
p2.line(y='RH_PBCOORCOFI',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBCOORDINACION',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBSJUNTAS',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBSMAESTROS',x='ts',source=source1,line_color='green')
p2.line(y='RH_PBVESTIBULO',x='ts',source=source1,line_color='green')


#Acá va lo de ambient quality


p_o.hbar(y='names', right='valuesco2',left=0, height=0.6,line_color='black',color='white',source=source3)

p2_o.hbar(y='names', right='valuesdb', height=0.6,line_color='black',color='white',source=source3)

p5_o.hbar(y='names', right='valuesco2',left=0, height=0.6,line_color='black',color='white',source=source2)

p6_o.hbar(y='names', left='valuesdb', right=0, height=0.6,line_color='black',color='white',source=source2)

p3_o.line(y='co2_N1AU401',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N1AU402',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N1AU403',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N1AU404',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU101',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU102',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU103',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU201',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU202',x='ts',source=source1,line_color='blue')
p3_o.line(y='co2_N2AU203',x='ts',source=source1,line_color='blue')

p3_o.line(y='co2_N1LAB',x='ts',source=source1,line_color='red')
p3_o.line(y='co2_N2LAB1',x='ts',source=source1,line_color='red')
p3_o.line(y='co2_N2LAB2',x='ts',source=source1,line_color='red')

p3_o.line(y='co2_PBADM',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBCOORCOFI',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBCOORDINACION',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBSJUNTAS',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBSMAESTROS',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBVESTIBULO',x='ts',source=source1,line_color='green')
p3_o.line(y='co2_PBCAFE',x='ts',source=source1,line_color='green')

p7_o.hbar_stack(ilus,y='names',source=source2,color=['green','blue','red'],line_color='black')

p4_o.hbar_stack(ilus,y='names',source=source3,color=['green','blue','red'],line_color='black')

comfort_panel=layout([[p,radio_group],[p2,p3]])
occupation_panel=layout([[p7_o,p6_o,p5_o,p9_o],[p4_o,p2_o,p_o,p8_o],[p3_o]])
tab1 = TabPanel(child=comfort_panel,title="Comfort panel")
tab2 = TabPanel(child=occupation_panel,title="Environment Quality panel")
#tab3= TabPanel(child=consume_panel,title='Consumption panel')
tabs = Tabs(tabs=[ tab1, tab2 ])

curdoc().add_root(tabs)
curdoc().add_periodic_callback(update,300000)