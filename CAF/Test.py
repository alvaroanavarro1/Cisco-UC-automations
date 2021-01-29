import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

output = []
for i in range(10,20):
    output.append(i)

output = ["%02d" % n for n in output]
print(output)


#filename = 'final_file-resumen.csv'
#with open(filename) as f:
	#reader = csv.reader(f)

    # Extraemos las variables de interes
	#numero_origen, fecha_hora, pais_origen = [], [], []
	#for row in reader:
		#numero_origen.append(row[0])
		#fecha_hora.append(row[12])
		#pais_origen.append(row[7])

#hora_num = []
#hora_dia = []
#fecha = []
#for c in fecha_hora:
#	for d in c:	
#		hora_num.append(c[14:15])
#		hora_dia.append(c[20:23])
#		fecha.append(c[0:6])

#hora =[]
#for j in range(1,len(hora_num)):
#	hora.append(hora_num[j] + hora_dia[j])
#for j in range(1,len(hora_llamadas_internas)):
#if str(dia_comienzo) in hora_llamadas_internas[j]:
#if '01 PM' in hora_llamadas_internas[j]:

#fecha_comienzo = fecha_hora[1]
#fecha_final = fecha_hora[-1]
#dia_comienzo = fecha_comienzo[0:6]
#dia_final = fecha_final[0:6]



#llamadas_internas = []
#llamadas_internas_pais = []
#llamadas_externas = []
#hora_llamadas_internas = []
#hora_llamadas_externas = []
#miami = 'Miami'
#contador = 0


#for i in numero_origen:
    #if len(i) == 4:
     #   hora_llamadas_internas.append(fecha_hora[numero_origen.index(i)])    
      #  llamadas_internas_pais.append(pais_origen[numero_origen.index(i)])
        #contador = contador + 1

    #else:
        #hora_llamadas_externas.append(fecha_hora[numero_origen.index(i)])
        #llamadas_externas.append(i)


#for j in range(1, len(hora_llamadas_internas)):
#    if str(dia_comienzo) in hora_llamadas_internas[j]:
#        dias_comienzof.append(hora_llamadas_internas[j])
#        if any('01:' and 'PM'  in x for x in dias_comienzof):
#            contador = contador + 1
#aux = []
#for j in range(1,len(llamadas_internas_pais)):
#    if 'Miami' in llamadas_internas_pais[j]:
#        aux.append(j)
        #if '05/Jan' in hora_llamadas_internas[j]:
            #contador = contador + 1

#print(aux)






