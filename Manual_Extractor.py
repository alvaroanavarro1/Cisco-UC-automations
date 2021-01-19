# Extractor manual para los archivos CDR/CMR CAF
# Se deben descargar los archivos con los siguientes nombres "file_cdr.csv" y "file_cmr.csv"

import pandas as pd
import os as os
import re
import time, threading
import schedule
import datetime as dt
import pytz as pytz
import time
from bs4 import BeautifulSoup
import io
from io import StringIO

# Archivos necesarios para realizar la extracción
# El archivo phone.csv debe estar actualizado a la fecha

file_phone = pd.read_csv("phone.csv", low_memory=False)
file_gw = pd.read_csv("gateway.csv", low_memory=False)
file_dp = pd.read_csv("devicepool.csv", low_memory=False)
file_cfb = pd.read_csv("conferencebridge.csv", low_memory=False)
file_xcode = pd.read_csv("transcoder.csv", low_memory=False)



# TIME ZONES #

Argentina = {'site':'Argentina', 'timezone': 'America/Argentina/Buenos_Aires'}
Brasil = {'site':'Brasil', 'timezone':'Etc/GMT+3'}
Bolivia = {'site':'Bolivia', 'timezone': 'America/La_Paz'}
Colombia = {'site':'Colombia', 'timezone': 'America/Bogota'}
Espana = {'site':'Espana', 'timezone': 'Europe/Madrid'}
Ecuador = {'site':'Ecuador', 'timezone':'America/Guayaquil'}
Mexico = {'site':'Mexico', 'timezone': 'America/Cancun'}
Peru = {'site':'Peru', 'timezone': 'America/Lima'}
Paraguay = {'site':'Paraguay', 'timezone':'America/Asuncion'}
Panama = {'site':'Panama', 'timezone':'America/Panama'}
TYT =  {'site':'TYT', 'timezone':'America/Port_of_Spain'}
Uruguay = {'site':'Uruguay', 'timezone':'America/Argentina/Buenos_Aires'}
Venezuela = {'site':'Venezuela', 'timezone':'Etc/GMT+4'}
Miami =  {'site':'Miami', 'timezone':'America/New_York'}
sites = [Argentina,Brasil,Bolivia,Colombia,Espana,Ecuador,Mexico,Peru,Paraguay,Panama,TYT,Uruguay,Venezuela,Miami]

# Función que linkea dirección MAC del telefono con país de origen

def get_location(DeviceName):
    value = str(DeviceName)
    print(value)

    if value == 'csfms38680':
        aux_value = 'Venezuela'
        return aux_value
        
    if re.match('^SEP.*$|^[Cc][Ss][Ff].*$|^[Tt][Cc][Tt].*$|^BOT.*$', value):
        #print('1')
        # Busco DeviceName en archivo phone.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_phone.loc[file_phone['Device Name'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'Device Pool'])
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|^AALN.*$|^AN.*$|^VG.*$|^Trunk.*$|^SIP.*', value):
        #print('2')
        # Busco DeviceName en archivo gateway.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_gw.loc[file_gw['DEVICE NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value


    elif re.match('^CFB_[0-9].*$|^ANN_[0-9].*$|^MTP_[0-9].*$|^EXTMTP.*$', value):
        #print('3')
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^Conductor.*$|^HD_bridge.*$|^MCU.*$', value):
        #print('4')
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^CFB.*$', value):
        #print('5')
        file_temp = file_cfb.loc[file_cfb['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL'] 
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match('^XCODE.*$', value):
        #print('6')
        file_temp = file_xcode.loc[file_xcode['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]

        return aux_value
    
    elif re.match('^Parking.*$|^CAF.*$|^CiscoUM1.*', value):
        #print('7')
        aux_value = 'Miami'
        
        return aux_value

# Función que transforma el tiempo crudo de los archivos

def get_time(x):

    source = str(x.source)

    for aux in sites:
        if source == aux['site']:
            time_zone = pytz.timezone(aux['timezone'])
            x_new = x
            try:
                x_new.dateTimeOrigination1 = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone)
                x_new.month = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%B')
                x_new.year = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%Y')
                x_new.day = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%d')
                x_new.hour = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%I %p')
                x_new.dateTimeOrigination = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
            except:
                pass
            try:
                x_new.dateTimeConnect1 = dt.datetime.fromtimestamp(x_new.dateTimeConnect).astimezone(time_zone)
                x_new.dateTimeConnect = dt.datetime.fromtimestamp(x_new.dateTimeConnect).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
            except:
                pass
            try:
                x_new.dateTimeDisconnect1 = dt.datetime.fromtimestamp(x_new.dateTimeDisconnect).astimezone(time_zone)
                x_new.dateTimeDisconnect = dt.datetime.fromtimestamp(x_new.dateTimeDisconnect).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
                x_new.source = x.source
                return x_new
                break
            except:
                pass
                return x_new
                break
        else:
            None

# Función que da formato al archivo final. Se aplican funciones de mapeo de localidad y tiempo

def change(file_cdr):
    
    file_cdr['dateTimeOrigination1'] = file_cdr['dateTimeOrigination']
    file_cdr['dateTimeConnect1'] = file_cdr['dateTimeConnect']
    file_cdr['dateTimeDisconnect1'] = file_cdr['dateTimeDisconnect']
    file_cdr.insert(4, 'year', 0)
    file_cdr.insert(5, 'month', 0)
    file_cdr.insert(6, 'day', 0)
    file_cdr.insert(7, 'hour', 0)
    file_cdr.insert(8, 'source', 0)
    file_cdr.insert(9, 'destination', 0)
    file_cdr.insert(10, 'concurrency', 0)
    
    print("Step 1. Please wait. Mapping source/destination and verifying timezones.\n")
    #file_cdr.to_csv(r'D:\Desktop-Backup\Temp\ProjectCDR-CMR\Sub-Import-Project\CAF\result-test.csv')
    file_cdr['source'] = file_cdr['origDeviceName'].apply(lambda x: get_location(x))
    file_cdr['destination'] = file_cdr['destDeviceName'].apply(lambda x: get_location(x))
    # Mapping Time:
    time_values_loc = ['year','month', 'day', 'hour', 'dateTimeOrigination1', 'dateTimeConnect1', 'dateTimeDisconnect1','dateTimeOrigination', 'dateTimeConnect', 'dateTimeDisconnect', 'source']
    file_cdr[time_values_loc] = file_cdr[time_values_loc].apply(get_time, axis=1)
    print("Step 1. Done!")
    
    return file_cdr

# Lectura de archivos y aplicación de formato a los mismos

file_cdr = pd.read_csv('file_cdr.csv',low_memory=False)
file_cmr = pd.read_csv('file_cmr.csv',low_memory=False)

# CMR DATA #
filter_colum_metrics =[

'orignumberPacketsSent',
'orignumberPacketsReceived','orignumberPacketsLost','origjitter','origlatency','destnumberPacketsSent',
'destnumberPacketsReceived','destnumberPacketsLost','destjitter','destlatency'
]

file_cmr = file_cmr[filter_colum_metrics]
file_cdr = pd.concat([file_cdr, file_cmr], axis=1, sort=False)

# Generación de archivos de debug
#file_cdr.to_csv('CAF-CDR3.csv')
#file_cdr = pd.read_csv('CAF-CDR3.csv',low_memory=False)

file_cdr = change(file_cdr)
file_cdr.to_csv('final_file.csv')

# Formato de nombre de columnas a español

file = pd.read_csv('final_file.csv',low_memory=False)
filter1 = ['callingPartyNumber','callingPartyUnicodeLoginUserID','origDeviceName','destDeviceName','originalCalledPartyNumber','finalCalledPartyNumber','finalCalledPartyUnicodeLoginUserID',
           'source','destination','origCause_value','destCause_value','dateTimeConnect','dateTimeDisconnect','duration']


file = file[filter1]

file = file.rename(columns={"callingPartyNumber": "Numero Origen",
                          "callingPartyUnicodeLoginUserID": "ID Usuario Origen",
                          "origDeviceName":"Dispositivo Origen",
                          "destDeviceName":"Dispositivo Destino",
                          "originalCalledPartyNumber":"Numero Marcado Original",
                          "finalCalledPartyNumber":"Numero Marcado Final",
                          "finalCalledPartyUnicodeLoginUserID":"ID Usuario Destino",
                          "source":"Origen",
                          "destination":"Destino",
                          "origCause_value":"Codigo Origen",
                          "destCause_value":"Codigo Destino",
                          "dateTimeConnect":"Tiempo de Conexion",
                          "dateTimeDisconnect":"Tiempo de Desconexion",
                          "duration":"Duracion(s)"})


file = file.to_csv('final_file' +'-resumen.csv',index=False)

