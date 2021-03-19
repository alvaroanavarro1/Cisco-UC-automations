import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import csv
import numpy as np

df_1 = pd.read_csv ('reporte.csv', usecols= ['Device Name','Status'], low_memory=False)
df_new1 = df_1.rename(columns={'Device Name': 'Device'})
#df_new1 = df_new1.to_string(index=False)


df_2 = pd.read_csv ('phone.csv', usecols= ['Device Name', 'Description', 'Device Pool', 'Device Type', 'Directory Number 1','Line Text Label 1', 'Owner User ID'], low_memory=False)
df_new2 = df_2.rename(columns={'Device Name': 'Device', 'Directory Number 1' : 'DirectoryNum', 'Line Text Label 1' : 'Owner', 'Owner User ID' : 'OwnerID'})
#df_new2 = df_new2.to_string(index=False)

mac = []
for i in df_new2['Device']:
    if 'SEP' in i:
        mac.append(i[3:])
    else:
        mac.append('')

df_new2 = df_new2.assign(MAC = mac) 


location = []
media_group_list = []
site = []
for i in df_new2['Device Pool']:
    if 'DP-KOF-VEN-PVAL' in i:
        location.append('Hub_None')
        media_group_list.append('MRL-KOFVEN-PVAL')
        site.append('PLANTA VALENCIA')
    elif 'DP-KOF-VEN-OFC' in i:
        location.append('Hub_None')
        media_group_list.append('MRL-KOFVEN-OFC')
        site.append('OFICINA CENTRAL')
    elif 'DP-KOF-VEN-ALGO' in i:
        location.append('LC-KOF-VEN-ALGO')
        media_group_list.append('MRL-KOFVEN-ALGO')
        site.append('ALGODONAL')
    elif 'DP-KOF-VEN-ANTI' in i:
        location.append('LC-KOF-VEN-ANTI')
        media_group_list.append('MRL-KOFVEN-ANTI')
        site.append('ANTIMANO')
    elif 'DP-KOF-VEN-APUR' in i:
        location.append('LC-KOF-VEN-APUR')
        media_group_list.append('MRL-KOFVEN-APUR')
        site.append('APURE')
    elif 'DP-KOF-VEN-BLNA' in i:
        location.append('LC-KOF-VEN-BLNA')
        media_group_list.append('MRL-KOFVEN-BLNA')
        site.append('BARCELONA')
    elif 'DP-KOF-VEN-LGUA' in i:
        location.append('LC-KOF-VEN-LGUA')
        media_group_list.append('MRGL-CCFLG')
        site.append('LA GUAIRA')
    elif 'DP-KOF-VEN-BQTO' in i:
        location.append('LC-KOF-VEN-BQTO')
        media_group_list.append('MRL-KOFVEN-BQTO')
        site.append('BARQUISIMETO')
    elif 'DP-KOF-VEN-BRNA' in i:
        location.append('LC-KOF-VEN-BRNA')
        media_group_list.append('MRL-KOFVEN-BRNA')
        site.append('BARINAS')
    elif 'DP-KOF-VEN-CATI' in i:
        location.append('LC-KOF-VEN-CATI')
        media_group_list.append('MRL-KOFVEN-LCAT')
        site.append('LA CATIA')
    elif 'DP-KOF-VEN-CBOL' in i:
        location.append('LC-KOF-VEN-CBOL')
        media_group_list.append('MRL-KOFVEN-CBOL')
        site.append('CIUDAD BOLIVAR')
    elif 'DP-KOF-VEN-CBZO' in i:
        location.append('LC-KOF-VEN-CBZO')
        media_group_list.append('MRL-KOFVEN-CBZO')
        site.append('CALABOZO')
    elif 'DP-KOF-VEN-COJE' in i:
        location.append('LC-KOF-VEN-COJE')
        media_group_list.append('MRL-KOFVEN-COJE')
        site.append('CIUDAD OJEDA')
    elif 'DP-KOF-VEN-CUMA' in i:
        location.append('LC-KOF-VEN-CUMA')
        media_group_list.append('MRL-KOFVEN-CUMA')
        site.append('CUMANA')
    elif 'DP-KOF-VEN-DMCY' in i:
        location.append('LC-KOF-VEN-DMCY')
        media_group_list.append('MRL-KOFVEN-DMCY')
        site.append('DIST. MARACAY')
    elif 'DP-KOF-VEN-DVAL' in i:
        location.append('LC-KOF-VEN-DVAL')
        media_group_list.append('MRL-KOFVEN-DVAL')
        site.append('DIST. VALENCIA')
    elif 'DP-KOF-VEN-GNPA' in i:
        location.append('LC-KOF-VEN-GNPA')
        media_group_list.append('MRL-KOFVEN-GNPA')
        site.append('GUANIPA')
    elif 'DP-KOF-VEN-GUAR' in i:
        location.append('LC-KOF-VEN-GUAR')
        media_group_list.append('MRL-KOFVEN-GUAR')
        site.append('GUARENAS')
    elif 'DP-KOF-VEN-LCOR' in i:
        location.append('LC-KOF-VEN-LCOR')
        media_group_list.append('MRL-KOF-VEN-OFC')
        site.append('LOS CORTIJOS')
    elif 'DP-KOF-VEN-LPAS' in i:
        location.append('LC-KOF-VEN-LPAS')
        media_group_list.append('MRL-KOFVEN-LPAS')
        site.append('LA PASCUA')
    elif 'DP-KOF-VEN-MARG' in i:
        location.append('LC-KOF-VEN-MARG')
        media_group_list.append('MRL-KOFVEN-MARG')
        site.append('MARGARITA')
    elif 'DP-KOF-VEN-MATU' in i:
        location.append('LC-KOF-VEN-MATU')
        media_group_list.append('MRL-KOFVEN-MATU')
        site.append('MATURIN')
    elif 'DP-KOF-VEN-MATU' in i:
        location.append('LC-KOF-VEN-MATU')
        media_group_list.append('MRL-KOFVEN-MATU')
        site.append('MATURIN')
    elif 'DP-KOF-VEN-MCBO' in i:
        location.append('LC-KOF-VEN-MCBO')
        media_group_list.append('MRL-KOFVEN-MCBO')
        site.append('MARACAIBO')
    elif 'DP-KOF-VEN-MCBN' in i:
        location.append('LC-KOF-VEN-MCBN')
        media_group_list.append('MRL-KOFVEN-MCBN')
        site.append('MARACAIBO NORTE')
    elif 'DP-KOF-VEN-MCBS' in i:
        location.append('LC-KOF-VEN-MCBS')
        media_group_list.append('MRL-KOFVEN-MCBS')
        site.append('MARACAIBO SUR')
    elif 'DP-KOF-VEN-OFC' in i:
        location.append('LC-KOF-VEN-OFC')
        media_group_list.append('MRL-KOF-VEN-OFC')
        site.append('OFICINA CENTRAL')
    elif 'DP-KOF-VEN-OFC-VCFB' in i:
        location.append('LC-KOF-VEN-OFC')
        media_group_list.append('MRL-KOF-VEN-OFC')
        site.append('OFICINA CENTRAL')
    elif 'DP-KOF-VEN-SCRI' in i:
        location.append('LC-KOF-VEN-SCRI')
        media_group_list.append('MRL-KOFVEN-SCRI')
        site.append('SAN CRISTOBAL')
    elif 'DP-KOF-VEN-SFLX' in i:
        location.append('LC-KOF-VEN-SFLX')
        media_group_list.append('MRL-KOFVEN-SFLX')
        site.append('SAN FELIX')
    elif 'DP-KOF-VEN-SFLX' in i:
        location.append('LC-KOF-VEN-SFLX')
        media_group_list.append('MRL-KOFVEN-SFLX')
        site.append('SAN FELIX')
    else:
        location.append('')
        media_group_list.append('')
        site.append('')
   
df_new2 = df_new2.assign(Location = location) 
df_new2 = df_new2.assign(Media = media_group_list) 
df_new2 = df_new2.assign(Site = site) 

status = []
status = df_new1['Status'] 
devicename = df_new2['Device']
orden = []

for v in devicename:
    orden.append(df_new1.loc[df_new1['Device'] == v, 'Status'].to_string(index=False))


df_new2 = df_new2.assign(Status = orden) 

df_new2 = df_new2[['Device', 'MAC', 'Status', 'Description', 'Device Pool', 'Location', 'Media', 'Device Type', 'DirectoryNum', 'Owner', 'OwnerID', 'Site']]

df_new2.to_csv('reporte-final.csv', index=False)