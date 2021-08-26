import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np


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