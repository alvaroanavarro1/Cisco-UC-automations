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

# Gráfica llamadas salientes por país

plt.ylabel('Llamadas por país')
plt.title('Número de llamadas salientes por país')
rects = plt.bar(paises,llamadas_salientes, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.show()

# Analiza duración de la llamada
llamadas = len(origen)
duracion_venezuela = []
duracion_argentina = []
duracion_brasil = []
duracion_bolivia = []
duracion_colombia = []
duracion_espana = []
duracion_ecuador = []
duracion_mexico = []
duracion_peru = []
duracion_paraguay = []
duracion_panama = []
duracion_tyt = []
duracion_uruguay = []
duracion_miami = []

for i in range(1, llamadas):
    if 'Venezuela' == origen[i]:
        duracion_venezuela.append(int(duracion[i]))

    elif 'Argentina' == origen[i]:
        duracion_argentina.append(int(duracion[i]))
    
    elif 'Brasil' == origen[i]:
        duracion_brasil.append(int(duracion[i]))
    
    elif 'Bolivia' == origen[i]:
        duracion_bolivia.append(int(duracion[i]))
    
    elif 'Colombia' == origen[i]:
        duracion_colombia.append(int(duracion[i]))
    
    elif 'Espana' == origen[i]:
        duracion_espana.append(int(duracion[i]))
    
    elif 'Ecuador' == origen[i]:
        duracion_ecuador.append(int(duracion[i]))
    
    elif 'Mexico' == origen[i]:
        duracion_mexico.append(int(duracion[i]))

    elif 'Peru' == origen[i]:
        duracion_peru.append(int(duracion[i]))

    elif 'Paraguay' == origen[i]:
        duracion_paraguay.append(int(duracion[i]))

    elif 'Panama' == origen[i]:
        duracion_panama.append(int(duracion[i]))

    elif 'TYT' == origen[i]:
        duracion_tyt.append(int(duracion[i]))
    
    elif 'Uruguay' == origen[i]:
        duracion_uruguay.append(int(duracion[i]))
    
    elif 'Miami' == origen[i]:
        duracion_miami.append(int(duracion[i]))


duracion_llamadas = [sum(duracion_venezuela)/60, sum(duracion_argentina)/60, sum(duracion_brasil)/60, sum(duracion_bolivia)/60, sum(duracion_colombia)/60,
sum(duracion_espana)/60, sum(duracion_ecuador)/60, sum(duracion_mexico)/60, sum(duracion_peru)/60, sum(duracion_paraguay)/60, sum(duracion_panama)/60,
sum(duracion_tyt)/60, sum(duracion_uruguay)/60, sum(duracion_miami)/60]

# Gráfica duración de llamadas por país

plt.ylabel('Duración de Llamadas (minutos)')
plt.title('Duración de llamadas salientes por país')
rects = plt.bar(paises,duracion_llamadas, width=0.5)

for r in rects:
    height = r.get_height() 
    plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.show()