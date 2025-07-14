import pandas as pd
import numpy as np
import random
dthis = ['DTHIS_N1AU401','DTHIS_N1AU402','DTHIS_N1AU403','DTHIS_N1AU404','DTHIS_N1LAB','DTHIS_N2AU101','DTHIS_N2AU102','DTHIS_N2AU103','DTHIS_N2AU201','DTHIS_N2AU202','DTHIS_N2AU203','DTHIS_N2LAB1','DTHIS_N2LAB2','DTHIS_PBADM','DTHIS_PBCAFE','DTHIS_PBCOORCOFI','DTHIS_PBCOORDINACION','DTHIS_PBSJUNTAS','DTHIS_PBSMAESTROS','DTHIS_PBVESTIBULO']
all_sensors_c = ["Ti_N1AU401","RH_N1AU401","A_inWN1AU401","A_outWN1AU401","A_totWN1AU401","A_totVN1AU401","dB_N1AU401","co2_N1AU401","ilu_sub_N1AU401","ilu_u_N1AU401","ilu_sob_N1AU401","A_totWN1AU402","A_inWN1AU402","RH_N1AU402","ilu_sub_N1AU402","A_outWN1AU402","A_totVN1AU402","ilu_sob_N1AU402","co2_N1AU402","ilu_u_N1AU402","Ti_N1AU402","dB_N1AU402","A_inWN1AU403","A_totWN1AU403","RH_N1AU403","A_outWN1AU403","ilu_sub_N1AU403","A_totVN1AU403","co2_N1AU403","ilu_sob_N1AU403","ilu_u_N1AU403","Ti_N1AU403","dB_N1AU403","A_totWN1AU404","A_inWN1AU404","RH_N1AU404","ilu_sob_N1AU404","co2_N1AU404","A_totVN1AU404","ilu_sub_N1AU404","A_outWN1AU404","dB_N1AU404","Ti_N1AU404","ilu_u_N1AU404","RH_N1LAB","Ti_N1LAB","A_totVN1LAB","ilu_sub_N1LAB","ilu_sob_N1LAB","ilu_u_N1LAB","dB_N1LAB","co2_N1LAB","A_totWN1LAB","dB_N2AU101","A_inWN2AU101","A_totWN2AU101","ilu_sub_N2AU101","A_outWN2AU101","RH_N2AU101","co2_N2AU101","ilu_sob_N2AU101","Ti_N2AU101","ilu_u_N2AU101","A_totVN2AU101","dB_N2AU102","A_totWN2AU102","A_inWN2AU102","ilu_sub_N2AU102","RH_N2AU102","A_outWN2AU102","ilu_sob_N2AU102","co2_N2AU102","ilu_u_N2AU102","Ti_N2AU102","A_totVN2AU102","dB_N2AU103","A_inWN2AU103","A_totWN2AU103","ilu_sub_N2AU103","A_outWN2AU103","RH_N2AU103","co2_N2AU103","ilu_sob_N2AU103","ilu_u_N2AU103","Ti_N2AU103","A_totVN2AU103","A_totWN2AU201","A_inWN2AU201","ilu_sub_N2AU201","ilu_u_N2AU201","A_totVN2AU201","dB_N2AU201","ilu_sob_N2AU201","Ti_N2AU201","RH_N2AU201","A_outWN2AU201","co2_N2AU201","A_inWN2AU202","A_totWN2AU202","A_totVN2AU202","ilu_sub_N2AU202","dB_N2AU202","ilu_u_N2AU202","ilu_sob_N2AU202","Ti_N2AU202","A_outWN2AU202","RH_N2AU202","co2_N2AU202","A_totWN2AU203","A_inWN2AU203","A_totVN2AU203","ilu_sub_N2AU203","dB_N2AU203","ilu_sob_N2AU203","Ti_N2AU203","ilu_u_N2AU203","RH_N2AU203","A_outWN2AU203","co2_N2AU203","A_totVN2LAB1","ilu_sob_N2LAB1","dB_N2LAB1","co2_N2LAB1","ilu_u_N2LAB1","A_totWN2LAB1","Ti_N2LAB1","RH_N2LAB1","ilu_sub_N2LAB1","A_totVN2LAB2","co2_N2LAB2","dB_N2LAB2","ilu_sob_N2LAB2","Ti_N2LAB2","A_totWN2LAB2","ilu_u_N2LAB2","ilu_sub_N2LAB2","RH_N2LAB2","dB_PBADM","Ti_PBADM","A_totWPBADM","co2_PBADM","ilu_u_PBADM","RH_PBADM","ilu_sob_PBADM","A_totVPBADM","ilu_sub_PBADM","ilu_sub_PBCAFE","RH_PBCAFE","ilu_sob_PBCAFE","A_totWPBCAFE","co2_PBCAFE","dB_PBCAFE","Ti_PBCAFE","A_totVPBCAFE","ilu_u_PBCAFE","co2_PBCOORCOFI","dB_PBCOORCOFI","ilu_sob_PBCOORCOFI","A_totWPBCOORCOFI","A_totVPBCOORCOFI","ilu_u_PBCOORCOFI","RH_PBCOORCOFI","ilu_sub_PBCOORCOFI","Ti_PBCOORCOFI","RH_PBCOORDINACION","A_totWPBCOORDINACION","co2_PBCOORDINACION","ilu_sob_PBCOORDINACION","ilu_sub_PBCOORDINACION","A_totVPBCOORDINACION","dB_PBCOORDINACION","Ti_PBCOORDINACION","ilu_u_PBCOORDINACION","RH_PBSJUNTAS","Ti_PBSJUNTAS","ilu_sob_PBSJUNTAS","A_totWPBSJUNTAS","dB_PBSJUNTAS","ilu_u_PBSJUNTAS","A_totVPBSJUNTAS","ilu_sub_PBSJUNTAS","co2_PBSJUNTAS","ilu_sub_PBSMAESTROS","RH_PBSMAESTROS","A_totVPBSMAESTROS","ilu_u_PBSMAESTROS","co2_PBSMAESTROS","A_totWPBSMAESTROS","ilu_sob_PBSMAESTROS","dB_PBSMAESTROS","Ti_PBSMAESTROS","A_totWPBVESTIBULO","Ti_PBVESTIBULO","RH_PBVESTIBULO","ilu_sob_PBVESTIBULO","co2_PBVESTIBULO","dB_PBVESTIBULO","ilu_u_PBVESTIBULO","A_totVPBVESTIBULO","ilu_sub_PBVESTIBULO"]
all_sensors=[["Ti_N1AU401","RH_N1AU401","A_inWN1AU401","A_outWN1AU401","A_totWN1AU401","A_totVN1AU401","dB_N1AU401","co2_N1AU401","ilu_sub_N1AU401","ilu_u_N1AU401","ilu_sob_N1AU401"],
["A_totWN1AU402","A_inWN1AU402","RH_N1AU402","ilu_sub_N1AU402","A_outWN1AU402","A_totVN1AU402","ilu_sob_N1AU402","co2_N1AU402","ilu_u_N1AU402","Ti_N1AU402","dB_N1AU402"],
["A_inWN1AU403","A_totWN1AU403","RH_N1AU403","A_outWN1AU403","ilu_sub_N1AU403","A_totVN1AU403","co2_N1AU403","ilu_sob_N1AU403","ilu_u_N1AU403","Ti_N1AU403","dB_N1AU403"],
["A_totWN1AU404","A_inWN1AU404","RH_N1AU404","ilu_sob_N1AU404","co2_N1AU404","A_totVN1AU404","ilu_sub_N1AU404","A_outWN1AU404","dB_N1AU404","Ti_N1AU404","ilu_u_N1AU404"],
["RH_N1LAB","Ti_N1LAB","A_totVN1LAB","ilu_sub_N1LAB","ilu_sob_N1LAB","ilu_u_N1LAB","dB_N1LAB","co2_N1LAB","A_totWN1LAB"],
["dB_N2AU101","A_inWN2AU101","A_totWN2AU101","ilu_sub_N2AU101","A_outWN2AU101","RH_N2AU101","co2_N2AU101","ilu_sob_N2AU101","Ti_N2AU101","ilu_u_N2AU101","A_totVN2AU101"],
["dB_N2AU102","A_totWN2AU102","A_inWN2AU102","ilu_sub_N2AU102","RH_N2AU102","A_outWN2AU102","ilu_sob_N2AU102","co2_N2AU102","ilu_u_N2AU102","Ti_N2AU102","A_totVN2AU102"],
["dB_N2AU103","A_inWN2AU103","A_totWN2AU103","ilu_sub_N2AU103","A_outWN2AU103","RH_N2AU103","co2_N2AU103","ilu_sob_N2AU103","ilu_u_N2AU103","Ti_N2AU103","A_totVN2AU103"],
["A_totWN2AU201","A_inWN2AU201","ilu_sub_N2AU201","ilu_u_N2AU201","A_totVN2AU201","dB_N2AU201","ilu_sob_N2AU201","Ti_N2AU201","RH_N2AU201","A_outWN2AU201","co2_N2AU201"],
["A_inWN2AU202","A_totWN2AU202","A_totVN2AU202","ilu_sub_N2AU202","dB_N2AU202","ilu_u_N2AU202","ilu_sob_N2AU202","Ti_N2AU202","A_outWN2AU202","RH_N2AU202","co2_N2AU202"],
["A_totWN2AU203","A_inWN2AU203","A_totVN2AU203","ilu_sub_N2AU203","dB_N2AU203","ilu_sob_N2AU203","Ti_N2AU203","ilu_u_N2AU203","RH_N2AU203","A_outWN2AU203","co2_N2AU203"],
["A_totVN2LAB1","ilu_sob_N2LAB1","dB_N2LAB1","co2_N2LAB1","ilu_u_N2LAB1","A_totWN2LAB1","Ti_N2LAB1","RH_N2LAB1","ilu_sub_N2LAB1"],
["A_totVN2LAB2","co2_N2LAB2","dB_N2LAB2","ilu_sob_N2LAB2","Ti_N2LAB2","A_totWN2LAB2","ilu_u_N2LAB2","ilu_sub_N2LAB2","RH_N2LAB2"],
["dB_PBADM","Ti_PBADM","A_totWPBADM","co2_PBADM","ilu_u_PBADM","RH_PBADM","ilu_sob_PBADM","A_totVPBADM","ilu_sub_PBADM"],
["ilu_sub_PBCAFE","RH_PBCAFE","ilu_sob_PBCAFE","A_totWPBCAFE","co2_PBCAFE","dB_PBCAFE","Ti_PBCAFE","A_totVPBCAFE","ilu_u_PBCAFE"],
["co2_PBCOORCOFI","dB_PBCOORCOFI","ilu_sob_PBCOORCOFI","A_totWPBCOORCOFI","A_totVPBCOORCOFI","ilu_u_PBCOORCOFI","RH_PBCOORCOFI","ilu_sub_PBCOORCOFI","Ti_PBCOORCOFI"],
["RH_PBCOORDINACION","A_totWPBCOORDINACION","co2_PBCOORDINACION","ilu_sob_PBCOORDINACION","ilu_sub_PBCOORDINACION","A_totVPBCOORDINACION","dB_PBCOORDINACION","Ti_PBCOORDINACION","ilu_u_PBCOORDINACION"],
["RH_PBSJUNTAS","Ti_PBSJUNTAS","ilu_sob_PBSJUNTAS","A_totWPBSJUNTAS","dB_PBSJUNTAS","ilu_u_PBSJUNTAS","A_totVPBSJUNTAS","ilu_sub_PBSJUNTAS","co2_PBSJUNTAS"],
["ilu_sub_PBSMAESTROS","RH_PBSMAESTROS","A_totVPBSMAESTROS","ilu_u_PBSMAESTROS","co2_PBSMAESTROS","A_totWPBSMAESTROS","ilu_sob_PBSMAESTROS","dB_PBSMAESTROS","Ti_PBSMAESTROS"],
["A_totWPBVESTIBULO","Ti_PBVESTIBULO","RH_PBVESTIBULO","ilu_sob_PBVESTIBULO","co2_PBVESTIBULO","dB_PBVESTIBULO","ilu_u_PBVESTIBULO","A_totVPBVESTIBULO","ilu_sub_PBVESTIBULO"]]

exceed_dB = np.arange(115,80,-5.)
warning_dB = np.arange(85,55,-5.)
adequate_dB = np.arange(60,-5,-5.)

exceed_co2 = np.arange(480,505,5.)
warning_co2 = np.arange(440,485,5.)
adequate_co2 = np.arange(400,445,5.)

o_zones=['dB_N1AU401', 'dB_N1AU402', 'dB_N1AU403', 'dB_N1AU404',
       'dB_N2AU101', 'dB_N2AU102', 'dB_N2AU103', 'dB_N2AU201',
       'dB_N2AU202', 'dB_N2AU203', 'dB_PBADM', 'dB_PBCOORCOFI',
       'dB_PBCOORDINACION', 'dB_PBSJUNTAS', 'dB_PBSMAESTROS',
       'dB_PBVESTIBULO', 'dB_N1LAB', 'dB_N2LAB1', 'dB_N2LAB2',
       'dB_PBCAFE', 'time', 'co2_N1AU401', 'co2_N1AU402', 'co2_N1AU403',
       'co2_N1AU404', 'co2_N2AU101', 'co2_N2AU102', 'co2_N2AU103',
       'co2_N2AU201', 'co2_N2AU202', 'co2_N2AU203', 'co2_PBADM',
       'co2_PBCOORCOFI', 'co2_PBCOORDINACION', 'co2_PBSJUNTAS',
       'co2_PBSMAESTROS', 'co2_PBVESTIBULO', 'co2_N1LAB', 'co2_N2LAB1',
       'co2_N2LAB2', 'co2_PBCAFE', 'ilu_sub_N1AU401', 'ilu_u_N1AU401',
       'ilu_sob_N1AU401', 'ilu_sub_N1AU402', 'ilu_u_N1AU402',
       'ilu_sob_N1AU402', 'ilu_sub_N1AU403', 'ilu_u_N1AU403',
       'ilu_sob_N1AU403', 'ilu_sub_N1AU404', 'ilu_u_N1AU404',
       'ilu_sob_N1AU404', 'ilu_sub_N2AU101', 'ilu_u_N2AU101',
       'ilu_sob_N2AU101', 'ilu_sub_N2AU102', 'ilu_u_N2AU102',
       'ilu_sob_N2AU102', 'ilu_sub_N2AU103', 'ilu_u_N2AU103',
       'ilu_sob_N2AU103', 'ilu_sub_N2AU201', 'ilu_u_N2AU201',
       'ilu_sob_N2AU201', 'ilu_sub_N2AU202', 'ilu_u_N2AU202',
       'ilu_sob_N2AU202', 'ilu_sub_N2AU203', 'ilu_u_N2AU203',
       'ilu_sob_N2AU203', 'ilu_sub_PBADM', 'ilu_u_PBADM', 'ilu_sob_PBADM',
       'ilu_sub_PBCOORCOFI', 'ilu_u_PBCOORCOFI', 'ilu_sob_PBCOORCOFI',
       'ilu_sub_PBCOORDINACION', 'ilu_u_PBCOORDINACION',
       'ilu_sob_PBCOORDINACION', 'ilu_sub_PBSJUNTAS', 'ilu_u_PBSJUNTAS',
       'ilu_sob_PBSJUNTAS', 'ilu_sub_PBSMAESTROS', 'ilu_u_PBSMAESTROS',
       'ilu_sob_PBSMAESTROS', 'ilu_sub_PBVESTIBULO', 'ilu_u_PBVESTIBULO',
       'ilu_sob_PBVESTIBULO', 'ilu_sub_N1LAB', 'ilu_u_N1LAB',
       'ilu_sob_N1LAB', 'ilu_sub_N2LAB1', 'ilu_u_N2LAB1',
       'ilu_sob_N2LAB1', 'ilu_sub_N2LAB2', 'ilu_u_N2LAB2',
       'ilu_sob_N2LAB2', 'ilu_sub_PBCAFE', 'ilu_u_PBCAFE',
       'ilu_sob_PBCAFE']

dB_zones_au = []
dB_zones_others = []
for zone in o_zones:
    if 'dB_' in zone:
        if 'AU' in zone:
            dB_zones_au.append(zone)
        else:
            dB_zones_others.append(zone)
co2_zones=[]
co2_zones_au = []
co2_zones_others = []
for zone in o_zones:
    if 'co2_' in zone:
        if 'AU' in zone:
            co2_zones_au.append(zone)
        else:
            co2_zones_others.append(zone)
        co2_zones.append(zone)
sub_zones_au = []
sub_zones_others = []
for zone in o_zones:
    if 'ilu_sub_' in zone:
        if 'AU' in zone:
            sub_zones_au.append(zone)
        else:
            sub_zones_others.append(zone)
u_zones_au = []
u_zones_others = []
for zone in o_zones:
    if 'ilu_u_' in zone:
        if 'AU' in zone:
            u_zones_au.append(zone)
        else:
            u_zones_others.append(zone)
sob_zones_au = []
sob_zones_others = []
for zone in o_zones:
    if 'ilu_sob_' in zone:
        if 'AU' in zone:
            sob_zones_au.append(zone)
        else:
            sob_zones_others.append(zone)


aulas_n = ['N1AU401', 'N1AU402', 'N1AU403', 'N1AU404', 'N2AU101', 'N2AU102', 'N2AU103', 'N2AU201', 'N2AU202', 'N2AU203']
others_n = ['PBADM', 'PBCOORCOFI', 'PBCOORDINACION', 'PBSJUNTAS', 'PBSMAESTROS', 'PBVESTIBULO', 'N1LAB', 'N2LAB1', 'N2LAB2', 'PBCAFE']

ilus=['subs','us','sobs']

perce =[]
for i in range(10):
    perce.append(random.randint(0,100))

df=pd.DataFrame()
df['x']=np.ones(10)*0.5
df['y']=np.array([0.38,1.48,2.58,3.68,4.8,5.9,7,8.1,9.2,10.3])
df['text']=[str(num)+'%' for num in perce]

#comfort_sensors = ["RH_N1AU401","RH_N1AU402","RH_N1AU403","RH_N1AU404","RH_N1LAB","RH_N2AU101","RH_N2AU102","RH_N2AU103","RH_N2AU201","RH_N2AU202","RH_N2AU203","RH_N2LAB1","RH_N2LAB2","RH_PBADM","RH_PBATENCIONCOFI","RH_PBCAFE","RH_PBCOCINA","RH_PBCOORCOFI","RH_PBCOORDINACION","RH_PBSJUNTAS","RH_PBSMAESTROS","RH_PBVESTIBULO","T_out","Ti_N1AU401","Ti_N1AU402","Ti_N1AU403","Ti_N1AU404","Ti_N1LAB","Ti_N2AU101","Ti_N2AU102","Ti_N2AU103","Ti_N2AU201","Ti_N2AU202","Ti_N2AU203","Ti_N2LAB1","Ti_N2LAB2","Ti_PBADM","Ti_PBATENCIONCOFI","Ti_PBCAFE","Ti_PBCOCINA","Ti_PBCOORCOFI","Ti_PBCOORDINACION","Ti_PBSJUNTAS","Ti_PBSMAESTROS","Ti_PBVESTIBULO"]
#ti_sensors = ["Ti_N1AU401","Ti_N1AU402","Ti_N1AU403","Ti_N1AU404","Ti_N1LAB","Ti_N2AU101","Ti_N2AU102","Ti_N2AU103","Ti_N2AU201","Ti_N2AU202","Ti_N2AU203","Ti_N2LAB1","Ti_N2LAB2","Ti_PBADM","Ti_PBATENCIONCOFI","Ti_PBCAFE","Ti_PBCOCINA","Ti_PBCOORCOFI","Ti_PBCOORDINACION","Ti_PBSJUNTAS","Ti_PBSMAESTROS","Ti_PBVESTIBULO"]
#rh_sensors = ["RH_N1AU401","RH_N1AU402","RH_N1AU403","RH_N1AU404","RH_N1LAB","RH_N2AU101","RH_N2AU102","RH_N2AU103","RH_N2AU201","RH_N2AU202","RH_N2AU203","RH_N2LAB1","RH_N2LAB2","RH_PBADM","RH_PBATENCIONCOFI","RH_PBCAFE","RH_PBCOCINA","RH_PBCOORCOFI","RH_PBCOORDINACION","RH_PBSJUNTAS","RH_PBSMAESTROS","RH_PBVESTIBULO"]

publish_time = pd.Timedelta('5m')
correction = pd.Timedelta('6H')
zones = dict([(str(name),[]) for name in all_sensors_c])