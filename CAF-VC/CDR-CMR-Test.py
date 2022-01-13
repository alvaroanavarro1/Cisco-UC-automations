import pandas as pd
import re
import re
import datetime as dt
import pytz as pytz
import csv
import matplotlib.pyplot as plt


# SOURCE FILES #

file_phone = pd.read_csv("phone.csv", low_memory=False)
#file_gw = pd.read_csv("gateway.csv", low_memory=False)
file_tk = pd.read_csv("trunk.csv", low_memory=False)
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


def get_location(DeviceName):
    value = str(DeviceName)
    print(value)

        
    if re.match('^SEP.*$|^[Cc][Ss][Ff].*$|^[Tt][Cc][Tt].*$|^BOT.*$', value):
        # Busco DeviceName en archivo phone.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_phone.loc[file_phone['Device Name'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'Device Pool'])
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match('^CDP.*$|^NAP.*$|^PER.*$|^PAN.*$|^URU.*$|^VEN.*$|^ARG.*$|^COL.*$|^CDP.*$', value):
        # Busco DeviceName en archivo trunk.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_tk.loc[file_tk['DEVICE NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value


    elif re.match('^CFB_[0-9].*$|^ANN_[0-9].*$|^MTP_[0-9].*$|^EXTMTP.*$', value):
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^Conductor.*$|^HD_bridge.*$|^MCU.*$', value):
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^CFB.*$', value):
        file_temp = file_cfb.loc[file_cfb['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL'] 
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match('^XCODE.*$', value):
        file_temp = file_xcode.loc[file_xcode['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]

        return aux_value
    
    elif re.match('^Parking.*$|^CAF.*$|^CiscoUM1.*', value):
        aux_value = 'Miami'
        
        return aux_value

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
    
    print("Espere mientras se realiza el link entre telefonos y verificación de horarios\n")
    #file_cdr.to_csv(r'D:\Desktop-Backup\Temp\ProjectCDR-CMR\Sub-Import-Project\CAF\result-test.csv')
    file_cdr['source'] = file_cdr['origDeviceName'].apply(lambda x: get_location(x))
    file_cdr['destination'] = file_cdr['destDeviceName'].apply(lambda x: get_location(x))
    # Mapping Time:
    time_values_loc = ['year','month', 'day', 'hour', 'dateTimeOrigination1', 'dateTimeConnect1', 'dateTimeDisconnect1','dateTimeOrigination', 'dateTimeConnect', 'dateTimeDisconnect', 'source']
    file_cdr[time_values_loc] = file_cdr[time_values_loc].apply(get_time, axis=1)
    print("Listo! El archivo final debe estar en la carpeta")
    
    return file_cdr

# Lectura de archivos y aplicación de formato a los mismos

file_cdr = pd.read_csv('cdr.csv',low_memory=False)
file_cmr = pd.read_csv('cmr.csv',low_memory=False)

# CMR DATA #
filter_colum_metrics =[

'orignumberPacketsSent',
'orignumberPacketsReceived','orignumberPacketsLost','origjitter','origlatency','destnumberPacketsSent',
'destnumberPacketsReceived','destnumberPacketsLost','destjitter','destlatency'
]

file_cmr = file_cmr[filter_colum_metrics]
file_cdr = pd.concat([file_cdr, file_cmr], axis=1, sort=False)

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

##########################################################################
#Codigo para la graficación de estadisticas de llamada

filename = 'final_file-resumen.csv'
with open(filename) as f:
	reader = csv.reader(f)

    # Extraemos las variables de interes
	origen, destino, duracion = [], [], []
	for row in reader:
		origen.append(row[7])
		destino.append(row[8])
		duracion.append(row[13])

# Analiza las llamadas salientes
Venezuela_origen = origen.count('Venezuela')
Argentina_origen = origen.count('Argentina')
Brasil_origen = origen.count('Brasil')
Bolivia_origen = origen.count('Bolivia')
Colombia_origen = origen.count('Colombia')
Espana_origen = origen.count('Espana')
Ecuador_origen = origen.count('Ecuador')
Mexico_origen = origen.count('Mexico')
Peru_origen = origen.count('Peru')
Paraguay_origen = origen.count('Paraguay')
Panama_origen = origen.count('Panama')
TYT_origen = origen.count('TYT')
Uruguay_origen = origen.count('Uruguay')
Miami_origen = origen.count('Miami')

paises = ['Venezuela', 'Argentina', 'Brasil', 'Bolivia', 'Colombia', 'Espana',
 'Ecuador', 'Mexico', 'Peru', 'Paraguay', 'Panama', 'TYT', 'Uruguay', 'Miami']

llamadas_salientes = [Venezuela_origen, Argentina_origen, Brasil_origen, Bolivia_origen, Colombia_origen, Espana_origen, 
Ecuador_origen, Mexico_origen, Peru_origen, Paraguay_origen, Panama_origen, TYT_origen, Uruguay_origen, Miami_origen]

# Analiza las llamadas entrantes
Venezuela_destino = destino.count('Venezuela')
Argentina_destino = destino.count('Argentina')
Brasil_destino = destino.count('Brasil')
Bolivia_destino = destino.count('Bolivia')
Colombia_destino = destino.count('Colombia')
Espana_destino = destino.count('Espana')
Ecuador_destino = destino.count('Ecuador')
Mexico_destino = destino.count('Mexico')
Peru_destino = destino.count('Peru')
Paraguay_destino = destino.count('Paraguay')
Panama_destino = destino.count('Panama')
TYT_destino = destino.count('TYT')
Uruguay_destino = destino.count('Uruguay')
Miami_destino = destino.count('Miami')

llamadas_entrantes = [Venezuela_destino, Argentina_destino, Brasil_destino, Bolivia_destino, Colombia_destino, Espana_destino, 
Ecuador_destino, Mexico_destino, Peru_destino, Paraguay_destino, Panama_destino, TYT_destino, Uruguay_destino, Miami_destino]

# Gráfica llamadas salientes por país

plt.ylabel('Llamadas por país')
plt.title('Número de llamadas salientes por país')
rects = plt.bar(paises,llamadas_salientes, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.show()


# Gráfica llamadas entrantes por país

plt.ylabel('Llamadas por país')
plt.title('Número de llamadas entrantes por país')
rects = plt.bar(paises,llamadas_entrantes, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.show()


# Analiza duración de la llamada salientes
llamadas = len(origen)
duracion_saliente_venezuela = []
duracion_saliente_argentina = []
duracion_saliente_brasil = []
duracion_saliente_bolivia = []
duracion_saliente_colombia = []
duracion_saliente_espana = []
duracion_saliente_ecuador = []
duracion_saliente_mexico = []
duracion_saliente_peru = []
duracion_saliente_paraguay = []
duracion_saliente_panama = []
duracion_saliente_tyt = []
duracion_saliente_uruguay = []
duracion_saliente_miami = []

for i in range(1, llamadas):
    if 'Venezuela' == origen[i]:
        duracion_saliente_venezuela.append(float(duracion[i]))

    elif 'Argentina' == origen[i]:
        duracion_saliente_argentina.append(float(duracion[i]))
    
    elif 'Brasil' == origen[i]:
        duracion_saliente_brasil.append(float(duracion[i]))
    
    elif 'Bolivia' == origen[i]:
        duracion_saliente_bolivia.append(float(duracion[i]))
    
    elif 'Colombia' == origen[i]:
        duracion_saliente_colombia.append(float(duracion[i]))
    
    elif 'Espana' == origen[i]:
        duracion_saliente_espana.append(float(duracion[i]))
    
    elif 'Ecuador' == origen[i]:
        duracion_saliente_ecuador.append(float(duracion[i]))
    
    elif 'Mexico' == origen[i]:
        duracion_saliente_mexico.append(float(duracion[i]))

    elif 'Peru' == origen[i]:
        duracion_saliente_peru.append(float(duracion[i]))

    elif 'Paraguay' == origen[i]:
        duracion_saliente_paraguay.append(float(duracion[i]))

    elif 'Panama' == origen[i]:
        duracion_saliente_panama.append(float(duracion[i]))

    elif 'TYT' == origen[i]:
        duracion_saliente_tyt.append(float(duracion[i]))
    
    elif 'Uruguay' == origen[i]:
        duracion_saliente_uruguay.append(float(duracion[i]))
    
    elif 'Miami' == origen[i]:
        duracion_saliente_miami.append(float(duracion[i]))


duracion_llamadas_salientes = [sum(duracion_saliente_venezuela)/60, sum(duracion_saliente_argentina)/60, sum(duracion_saliente_brasil)/60, sum(duracion_saliente_bolivia)/60, sum(duracion_saliente_colombia)/60,
sum(duracion_saliente_espana)/60, sum(duracion_saliente_ecuador)/60, sum(duracion_saliente_mexico)/60, sum(duracion_saliente_peru)/60, sum(duracion_saliente_paraguay)/60, sum(duracion_saliente_panama)/60,
sum(duracion_saliente_tyt)/60, sum(duracion_saliente_uruguay)/60, sum(duracion_saliente_miami)/60]

# Gráfica duración de llamadas por país

plt.ylabel('Duración de Llamadas (minutos)')
plt.title('Duración de llamadas salientes por país')
rects = plt.bar(paises,duracion_llamadas_salientes, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % float(height), ha='center', va='bottom')

plt.show()


# Analiza duración de la llamada entrantes
duracion_entrante_venezuela = []
duracion_entrante_argentina = []
duracion_entrante_brasil = []
duracion_entrante_bolivia = []
duracion_entrante_colombia = []
duracion_entrante_espana = []
duracion_entrante_ecuador = []
duracion_entrante_mexico = []
duracion_entrante_peru = []
duracion_entrante_paraguay = []
duracion_entrante_panama = []
duracion_entrante_tyt = []
duracion_entrante_uruguay = []
duracion_entrante_miami = []

for i in range(1, llamadas):
    if 'Venezuela' == destino[i]:
        duracion_entrante_venezuela.append(float(duracion[i]))

    elif 'Argentina' == destino[i]:
        duracion_entrante_argentina.append(float(duracion[i]))
    
    elif 'Brasil' == destino[i]:
        duracion_entrante_brasil.append(float(duracion[i]))
    
    elif 'Bolivia' == destino[i]:
        duracion_entrante_bolivia.append(float(duracion[i]))
    
    elif 'Colombia' == destino[i]:
        duracion_entrante_colombia.append(float(duracion[i]))
    
    elif 'Espana' == destino[i]:
        duracion_entrante_espana.append(float(duracion[i]))
    
    elif 'Ecuador' == destino[i]:
        duracion_entrante_ecuador.append(float(duracion[i]))
    
    elif 'Mexico' == destino[i]:
        duracion_entrante_mexico.append(float(duracion[i]))

    elif 'Peru' == destino[i]:
        duracion_entrante_peru.append(float(duracion[i]))

    elif 'Paraguay' == destino[i]:
        duracion_entrante_paraguay.append(float(duracion[i]))

    elif 'Panama' == destino[i]:
        duracion_entrante_panama.append(float(duracion[i]))

    elif 'TYT' == destino[i]:
        duracion_entrante_tyt.append(float(duracion[i]))
    
    elif 'Uruguay' == destino[i]:
        duracion_entrante_uruguay.append(float(duracion[i]))
    
    elif 'Miami' == destino[i]:
        duracion_entrante_miami.append(float(duracion[i]))


duracion_llamadas_entrante = [sum(duracion_entrante_venezuela)/60, sum(duracion_entrante_argentina)/60, sum(duracion_entrante_brasil)/60, sum(duracion_entrante_bolivia)/60, sum(duracion_entrante_colombia)/60,
sum(duracion_entrante_espana)/60, sum(duracion_entrante_ecuador)/60, sum(duracion_entrante_mexico)/60, sum(duracion_entrante_peru)/60, sum(duracion_entrante_paraguay)/60, sum(duracion_entrante_panama)/60,
sum(duracion_entrante_tyt)/60, sum(duracion_entrante_uruguay)/60, sum(duracion_entrante_miami)/60]

# Gráfica duración de llamadas por país

plt.ylabel('Duración de Llamadas (minutos)')
plt.title('Duración de llamadas entrantes por país')
rects = plt.bar(paises,duracion_llamadas_entrante, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % float(height), ha='center', va='bottom')

plt.show()

