import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import csv
import numpy as np

df = pd.read_csv ('final_file-resumen.csv', usecols= ['Numero Origen','Origen','Tiempo de Desconexion', 'Duracion(s)'], low_memory=False)
df_new = df.rename(columns={'Numero Origen': 'Numero', 'Tiempo de Desconexion' : 'Hora', 'Duracion(s)' : 'Duracion'})

#fecha_comienzo = df_new.Hora[1]
#dia_comienzo = fecha_comienzo[0:6]
print('Escriba los días que desea revisar en formato dd/mm, ejemplo 02/Dec:')
dia1 = input()
dia2 = input()
dia3 = input()
dia4 = input()
dia5 = input()
dia6 = input()
dia7 = input()

tipo = input('Que tipo de llamadas desea observar?(internas/externas):')
respuesta = input('Si desea representar el promedio de todos los paises responda "paises", de lo contrario escriba el país que desea:')

paises = ['Venezuela', 'Argentina', 'Brasil', 'Bolivia', 'Colombia', 'Espana',
 'Ecuador', 'Mexico', 'Peru', 'Paraguay', 'Panama', 'TYT', 'Uruguay', 'Miami']

Horas = ['7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM'  ]

if tipo == 'internas':
    if respuesta == 'paises':
        for i in paises:

            #Dia 1 por hora interno
            pais_interno_dia1_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia1_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        
            llamadas_internas_dia1 = [len(pais_interno_dia1_7am), len(pais_interno_dia1_8am), len(pais_interno_dia1_9am), len(pais_interno_dia1_10am),
            len(pais_interno_dia1_11am), len(pais_interno_dia1_12pm), len(pais_interno_dia1_1pm), len(pais_interno_dia1_2pm), len(pais_interno_dia1_3pm),
            len(pais_interno_dia1_4pm), len(pais_interno_dia1_5pm), len(pais_interno_dia1_6pm)]

            plt.ylabel('Número de llamadas')
            plt.title('Llamadas internas por hora realizadas por ' + i + ' el dia ' + dia1)
            rects = plt.bar(Horas,llamadas_internas_dia1, width=0.5)

            for r in rects:
                height = r.get_height() 
                plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

            plt.show()

            #Dia 2 por hora Venezuela
            pais_interno_dia2_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia2_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 3 por hora interno
            pais_interno_dia3_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia3_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 4 por hora interno
            pais_interno_dia4_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia4_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 5 por hora interno
            pais_interno_dia5_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia5_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 6 por hora interno
            pais_interno_dia6_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 6 por hora interno
            pais_interno_dia6_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia6_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 7 por hora interno
            pais_interno_dia7_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_interno_dia7_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]


            promedio_7am = round((len(pais_interno_dia1_7am)+len(pais_interno_dia2_7am)+len(pais_interno_dia3_7am)+len(pais_interno_dia4_7am)+len(pais_interno_dia5_7am)+len(pais_interno_dia6_7am)+len(pais_interno_dia7_7am))/7)
            promedio_8am = round((len(pais_interno_dia1_8am)+len(pais_interno_dia2_8am)+len(pais_interno_dia3_8am)+len(pais_interno_dia4_8am)+len(pais_interno_dia5_8am)+len(pais_interno_dia6_8am)+len(pais_interno_dia7_8am))/7)
            promedio_9am = round((len(pais_interno_dia1_9am)+len(pais_interno_dia2_9am)+len(pais_interno_dia3_9am)+len(pais_interno_dia4_9am)+len(pais_interno_dia5_9am)+len(pais_interno_dia6_9am)+len(pais_interno_dia7_9am))/7)
            promedio_10am = round((len(pais_interno_dia1_10am)+len(pais_interno_dia2_10am)+len(pais_interno_dia3_10am)+len(pais_interno_dia4_10am)+len(pais_interno_dia5_10am)+len(pais_interno_dia6_10am)+len(pais_interno_dia7_10am))/7)
            promedio_11am = round((len(pais_interno_dia1_11am)+len(pais_interno_dia2_11am)+len(pais_interno_dia3_11am)+len(pais_interno_dia4_11am)+len(pais_interno_dia5_11am)+len(pais_interno_dia6_11am)+len(pais_interno_dia7_11am))/7)
            promedio_12pm = round((len(pais_interno_dia1_12pm)+len(pais_interno_dia2_12pm)+len(pais_interno_dia3_12pm)+len(pais_interno_dia4_12pm)+len(pais_interno_dia5_12pm)+len(pais_interno_dia6_12pm)+len(pais_interno_dia7_12pm))/7)
            promedio_1pm = round((len(pais_interno_dia1_1pm)+len(pais_interno_dia2_1pm)+len(pais_interno_dia3_1pm)+len(pais_interno_dia4_1pm)+len(pais_interno_dia5_1pm)+len(pais_interno_dia6_1pm)+len(pais_interno_dia7_1pm))/7)
            promedio_2pm = round((len(pais_interno_dia1_2pm)+len(pais_interno_dia2_2pm)+len(pais_interno_dia3_2pm)+len(pais_interno_dia4_2pm)+len(pais_interno_dia5_2pm)+len(pais_interno_dia6_2pm)+len(pais_interno_dia7_2pm))/7)
            promedio_3pm = round((len(pais_interno_dia1_3pm)+len(pais_interno_dia2_3pm)+len(pais_interno_dia3_3pm)+len(pais_interno_dia4_3pm)+len(pais_interno_dia5_3pm)+len(pais_interno_dia6_3pm)+len(pais_interno_dia7_3pm))/7)
            promedio_4pm = round((len(pais_interno_dia1_4pm)+len(pais_interno_dia2_4pm)+len(pais_interno_dia3_4pm)+len(pais_interno_dia4_4pm)+len(pais_interno_dia5_4pm)+len(pais_interno_dia6_4pm)+len(pais_interno_dia7_4pm))/7)
            promedio_5pm = round((len(pais_interno_dia1_5pm)+len(pais_interno_dia2_5pm)+len(pais_interno_dia3_5pm)+len(pais_interno_dia4_5pm)+len(pais_interno_dia5_5pm)+len(pais_interno_dia6_5pm)+len(pais_interno_dia7_5pm))/7)
            promedio_6pm = round((len(pais_interno_dia1_6pm)+len(pais_interno_dia2_6pm)+len(pais_interno_dia3_6pm)+len(pais_interno_dia4_6pm)+len(pais_interno_dia5_6pm)+len(pais_interno_dia6_6pm)+len(pais_interno_dia7_6pm))/7)

            promedio_semana = [promedio_7am, promedio_8am, promedio_9am, promedio_10am, promedio_11am, promedio_12pm, promedio_1pm, promedio_2pm, promedio_3pm, promedio_4pm, promedio_5pm, promedio_6pm]

            plt.ylabel('Número de llamadas')
            plt.title('Promedio de llamadas internas por hora realizadas por ' + i + ' del ' + dia1 + '-' + dia7)
            rects = plt.bar(Horas,promedio_semana, width=0.5)

            for r in rects:
                height = r.get_height() 
                plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

            plt.show()
    else:

    #Dia 1 por hora interno
        pais_interno_dia1_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]        
        pais_interno_dia1_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]       
        pais_interno_dia1_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia1_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        llamadas_internas_dia1 = [len(pais_interno_dia1_7am), len(pais_interno_dia1_8am), len(pais_interno_dia1_9am), len(pais_interno_dia1_10am),
        len(pais_interno_dia1_11am), len(pais_interno_dia1_12pm), len(pais_interno_dia1_1pm), len(pais_interno_dia1_2pm), len(pais_interno_dia1_3pm),
        len(pais_interno_dia1_4pm), len(pais_interno_dia1_5pm), len(pais_interno_dia1_6pm)]

        plt.ylabel('Número de llamadas')
        plt.title('Llamadas internas por hora realizadas por ' + respuesta + ' el dia ' + dia1)
        rects = plt.bar(Horas,llamadas_internas_dia1, width=0.5)

        for r in rects:
            height = r.get_height() 
            plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

        plt.show()

        #Dia 2 por hora interno
        pais_interno_dia2_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia2_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 3 por hora interno
        pais_interno_dia3_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia3_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 4 por hora interno
        pais_interno_dia4_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia4_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 5 por hora interno
        pais_interno_dia5_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia5_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 6 por hora interno
        pais_interno_dia6_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 6 por hora interno
        pais_interno_dia6_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia6_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 7 por hora interno
        pais_interno_dia7_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_interno_dia7_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) == 4) & (df_new.Duracion.astype(str).map(len) > 0)]


        promedio_7am = round((len(pais_interno_dia1_7am)+len(pais_interno_dia2_7am)+len(pais_interno_dia3_7am)+len(pais_interno_dia4_7am)+len(pais_interno_dia5_7am)+len(pais_interno_dia6_7am)+len(pais_interno_dia7_7am))/7)
        promedio_8am = round((len(pais_interno_dia1_8am)+len(pais_interno_dia2_8am)+len(pais_interno_dia3_8am)+len(pais_interno_dia4_8am)+len(pais_interno_dia5_8am)+len(pais_interno_dia6_8am)+len(pais_interno_dia7_8am))/7)
        promedio_9am = round((len(pais_interno_dia1_9am)+len(pais_interno_dia2_9am)+len(pais_interno_dia3_9am)+len(pais_interno_dia4_9am)+len(pais_interno_dia5_9am)+len(pais_interno_dia6_9am)+len(pais_interno_dia7_9am))/7)
        promedio_10am = round((len(pais_interno_dia1_10am)+len(pais_interno_dia2_10am)+len(pais_interno_dia3_10am)+len(pais_interno_dia4_10am)+len(pais_interno_dia5_10am)+len(pais_interno_dia6_10am)+len(pais_interno_dia7_10am))/7)
        promedio_11am = round((len(pais_interno_dia1_11am)+len(pais_interno_dia2_11am)+len(pais_interno_dia3_11am)+len(pais_interno_dia4_11am)+len(pais_interno_dia5_11am)+len(pais_interno_dia6_11am)+len(pais_interno_dia7_11am))/7)
        promedio_12pm = round((len(pais_interno_dia1_12pm)+len(pais_interno_dia2_12pm)+len(pais_interno_dia3_12pm)+len(pais_interno_dia4_12pm)+len(pais_interno_dia5_12pm)+len(pais_interno_dia6_12pm)+len(pais_interno_dia7_12pm))/7)
        promedio_1pm = round((len(pais_interno_dia1_1pm)+len(pais_interno_dia2_1pm)+len(pais_interno_dia3_1pm)+len(pais_interno_dia4_1pm)+len(pais_interno_dia5_1pm)+len(pais_interno_dia6_1pm)+len(pais_interno_dia7_1pm))/7)
        promedio_2pm = round((len(pais_interno_dia1_2pm)+len(pais_interno_dia2_2pm)+len(pais_interno_dia3_2pm)+len(pais_interno_dia4_2pm)+len(pais_interno_dia5_2pm)+len(pais_interno_dia6_2pm)+len(pais_interno_dia7_2pm))/7)
        promedio_3pm = round((len(pais_interno_dia1_3pm)+len(pais_interno_dia2_3pm)+len(pais_interno_dia3_3pm)+len(pais_interno_dia4_3pm)+len(pais_interno_dia5_3pm)+len(pais_interno_dia6_3pm)+len(pais_interno_dia7_3pm))/7)
        promedio_4pm = round((len(pais_interno_dia1_4pm)+len(pais_interno_dia2_4pm)+len(pais_interno_dia3_4pm)+len(pais_interno_dia4_4pm)+len(pais_interno_dia5_4pm)+len(pais_interno_dia6_4pm)+len(pais_interno_dia7_4pm))/7)
        promedio_5pm = round((len(pais_interno_dia1_5pm)+len(pais_interno_dia2_5pm)+len(pais_interno_dia3_5pm)+len(pais_interno_dia4_5pm)+len(pais_interno_dia5_5pm)+len(pais_interno_dia6_5pm)+len(pais_interno_dia7_5pm))/7)
        promedio_6pm = round((len(pais_interno_dia1_6pm)+len(pais_interno_dia2_6pm)+len(pais_interno_dia3_6pm)+len(pais_interno_dia4_6pm)+len(pais_interno_dia5_6pm)+len(pais_interno_dia6_6pm)+len(pais_interno_dia7_6pm))/7)

        promedio_semana = [promedio_7am, promedio_8am, promedio_9am, promedio_10am, promedio_11am, promedio_12pm, promedio_1pm, promedio_2pm, promedio_3pm, promedio_4pm, promedio_5pm, promedio_6pm]

        plt.ylabel('Número de llamadas')
        plt.title('Promedio de llamadas internas por hora realizadas por ' + respuesta + ' del ' + dia1 + '-' + dia7)
        rects = plt.bar(Horas,promedio_semana, width=0.5)

        for r in rects:
            height = r.get_height() 
            plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

        plt.show()
else:
    if respuesta == 'paises':
        for i in paises:

            #Dia 1 por hora externo
            pais_externo_dia1_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) >4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia1_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            llamadas_internas_dia1 = [len(pais_externo_dia1_7am), len(pais_externo_dia1_8am), len(pais_externo_dia1_9am), len(pais_externo_dia1_10am),
            len(pais_externo_dia1_11am), len(pais_externo_dia1_12pm), len(pais_externo_dia1_1pm), len(pais_externo_dia1_2pm), len(pais_externo_dia1_3pm),
            len(pais_externo_dia1_4pm), len(pais_externo_dia1_5pm), len(pais_externo_dia1_6pm)]

            plt.ylabel('Número de llamadas')
            plt.title('Llamadas externas por hora realizadas por ' + i + ' el dia ' + dia1)
            rects = plt.bar(Horas,llamadas_internas_dia1, width=0.5)

            for r in rects:
                height = r.get_height() 
                plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

            plt.show()

            #Dia 2 por hora externo
            pais_externo_dia2_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia2_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 3 por hora externo
            pais_externo_dia3_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia3_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 4 por hora externo
            pais_externo_dia4_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia4_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 5 por hora externo
            pais_externo_dia5_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia5_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 6 por hora externo
            pais_externo_dia6_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 6 por hora externo
            pais_externo_dia6_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia6_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

            #Dia 7 por hora externo
            pais_externo_dia7_7am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_8am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_9am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_10am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_11am = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_12pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_1pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_2pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_3pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_4pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_5pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
            pais_externo_dia7_6pm = df_new[(df_new.Origen.eq(i)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]


            promedio_7am = round((len(pais_externo_dia1_7am)+len(pais_externo_dia2_7am)+len(pais_externo_dia3_7am)+len(pais_externo_dia4_7am)+len(pais_externo_dia5_7am)+len(pais_externo_dia6_7am)+len(pais_externo_dia7_7am))/7)
            promedio_8am = round((len(pais_externo_dia1_8am)+len(pais_externo_dia2_8am)+len(pais_externo_dia3_8am)+len(pais_externo_dia4_8am)+len(pais_externo_dia5_8am)+len(pais_externo_dia6_8am)+len(pais_externo_dia7_8am))/7)
            promedio_9am = round((len(pais_externo_dia1_9am)+len(pais_externo_dia2_9am)+len(pais_externo_dia3_9am)+len(pais_externo_dia4_9am)+len(pais_externo_dia5_9am)+len(pais_externo_dia6_9am)+len(pais_externo_dia7_9am))/7)
            promedio_10am = round((len(pais_externo_dia1_10am)+len(pais_externo_dia2_10am)+len(pais_externo_dia3_10am)+len(pais_externo_dia4_10am)+len(pais_externo_dia5_10am)+len(pais_externo_dia6_10am)+len(pais_externo_dia7_10am))/7)
            promedio_11am = round((len(pais_externo_dia1_11am)+len(pais_externo_dia2_11am)+len(pais_externo_dia3_11am)+len(pais_externo_dia4_11am)+len(pais_externo_dia5_11am)+len(pais_externo_dia6_11am)+len(pais_externo_dia7_11am))/7)
            promedio_12pm = round((len(pais_externo_dia1_12pm)+len(pais_externo_dia2_12pm)+len(pais_externo_dia3_12pm)+len(pais_externo_dia4_12pm)+len(pais_externo_dia5_12pm)+len(pais_externo_dia6_12pm)+len(pais_externo_dia7_12pm))/7)
            promedio_1pm = round((len(pais_externo_dia1_1pm)+len(pais_externo_dia2_1pm)+len(pais_externo_dia3_1pm)+len(pais_externo_dia4_1pm)+len(pais_externo_dia5_1pm)+len(pais_externo_dia6_1pm)+len(pais_externo_dia7_1pm))/7)
            promedio_2pm = round((len(pais_externo_dia1_2pm)+len(pais_externo_dia2_2pm)+len(pais_externo_dia3_2pm)+len(pais_externo_dia4_2pm)+len(pais_externo_dia5_2pm)+len(pais_externo_dia6_2pm)+len(pais_externo_dia7_2pm))/7)
            promedio_3pm = round((len(pais_externo_dia1_3pm)+len(pais_externo_dia2_3pm)+len(pais_externo_dia3_3pm)+len(pais_externo_dia4_3pm)+len(pais_externo_dia5_3pm)+len(pais_externo_dia6_3pm)+len(pais_externo_dia7_3pm))/7)
            promedio_4pm = round((len(pais_externo_dia1_4pm)+len(pais_externo_dia2_4pm)+len(pais_externo_dia3_4pm)+len(pais_externo_dia4_4pm)+len(pais_externo_dia5_4pm)+len(pais_externo_dia6_4pm)+len(pais_externo_dia7_4pm))/7)
            promedio_5pm = round((len(pais_externo_dia1_5pm)+len(pais_externo_dia2_5pm)+len(pais_externo_dia3_5pm)+len(pais_externo_dia4_5pm)+len(pais_externo_dia5_5pm)+len(pais_externo_dia6_5pm)+len(pais_externo_dia7_5pm))/7)
            promedio_6pm = round((len(pais_externo_dia1_6pm)+len(pais_externo_dia2_6pm)+len(pais_externo_dia3_6pm)+len(pais_externo_dia4_6pm)+len(pais_externo_dia5_6pm)+len(pais_externo_dia6_6pm)+len(pais_externo_dia7_6pm))/7)

            promedio_semana = [promedio_7am, promedio_8am, promedio_9am, promedio_10am, promedio_11am, promedio_12pm, promedio_1pm, promedio_2pm, promedio_3pm, promedio_4pm, promedio_5pm, promedio_6pm]

            plt.ylabel('Número de llamadas')
            plt.title('Promedio de llamadas externas por hora realizadas por ' + i + ' del ' + dia1 + '-' + dia7)
            rects = plt.bar(Horas,promedio_semana, width=0.5)

            for r in rects:
                height = r.get_height() 
                plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

            plt.show()
    else:

    #Dia 1 por hora externo
        pais_externo_dia1_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]        
        pais_externo_dia1_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]       
        pais_externo_dia1_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia1_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia1)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        llamadas_internas_dia1 = [len(pais_externo_dia1_7am), len(pais_externo_dia1_8am), len(pais_externo_dia1_9am), len(pais_externo_dia1_10am),
        len(pais_externo_dia1_11am), len(pais_externo_dia1_12pm), len(pais_externo_dia1_1pm), len(pais_externo_dia1_2pm), len(pais_externo_dia1_3pm),
        len(pais_externo_dia1_4pm), len(pais_externo_dia1_5pm), len(pais_externo_dia1_6pm)]

        plt.ylabel('Número de llamadas')
        plt.title('Llamadas externas por hora realizadas por ' + respuesta + ' el dia ' + dia1)
        rects = plt.bar(Horas,llamadas_internas_dia1, width=0.5)

        for r in rects:
            height = r.get_height() 
            plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

        plt.show()

        #Dia 2 por hora externo
        pais_externo_dia2_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia2_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia2)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 3 por hora externo
        pais_externo_dia3_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia3_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia3)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 4 por hora externo
        pais_externo_dia4_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia4_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia4)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 5 por hora externo
        pais_externo_dia5_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia5_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia5)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 6 por hora externo
        pais_externo_dia6_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 6 por hora externo
        pais_externo_dia6_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia6_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia6)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]

        #Dia 7 por hora externo
        pais_externo_dia7_7am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("07:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_8am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("08:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_9am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("09:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_10am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("10:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_11am = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("11:")) & (df_new.Hora.str.contains("AM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_12pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("12:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_1pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("01:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_2pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("02:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_3pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("03:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_4pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("04:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_5pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("05:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]
        pais_externo_dia7_6pm = df_new[(df_new.Origen.eq(respuesta)) & (df_new.Hora.str.contains(dia7)) & (df_new.Hora.str.contains("06:")) & (df_new.Hora.str.contains("PM")) & (df_new.Numero.astype(str).map(len) > 4) & (df_new.Duracion.astype(str).map(len) > 0)]


        promedio_7am = round((len(pais_externo_dia1_7am)+len(pais_externo_dia2_7am)+len(pais_externo_dia3_7am)+len(pais_externo_dia4_7am)+len(pais_externo_dia5_7am)+len(pais_externo_dia6_7am)+len(pais_externo_dia7_7am))/7)
        promedio_8am = round((len(pais_externo_dia1_8am)+len(pais_externo_dia2_8am)+len(pais_externo_dia3_8am)+len(pais_externo_dia4_8am)+len(pais_externo_dia5_8am)+len(pais_externo_dia6_8am)+len(pais_externo_dia7_8am))/7)
        promedio_9am = round((len(pais_externo_dia1_9am)+len(pais_externo_dia2_9am)+len(pais_externo_dia3_9am)+len(pais_externo_dia4_9am)+len(pais_externo_dia5_9am)+len(pais_externo_dia6_9am)+len(pais_externo_dia7_9am))/7)
        promedio_10am = round((len(pais_externo_dia1_10am)+len(pais_externo_dia2_10am)+len(pais_externo_dia3_10am)+len(pais_externo_dia4_10am)+len(pais_externo_dia5_10am)+len(pais_externo_dia6_10am)+len(pais_externo_dia7_10am))/7)
        promedio_11am = round((len(pais_externo_dia1_11am)+len(pais_externo_dia2_11am)+len(pais_externo_dia3_11am)+len(pais_externo_dia4_11am)+len(pais_externo_dia5_11am)+len(pais_externo_dia6_11am)+len(pais_externo_dia7_11am))/7)
        promedio_12pm = round((len(pais_externo_dia1_12pm)+len(pais_externo_dia2_12pm)+len(pais_externo_dia3_12pm)+len(pais_externo_dia4_12pm)+len(pais_externo_dia5_12pm)+len(pais_externo_dia6_12pm)+len(pais_externo_dia7_12pm))/7)
        promedio_1pm = round((len(pais_externo_dia1_1pm)+len(pais_externo_dia2_1pm)+len(pais_externo_dia3_1pm)+len(pais_externo_dia4_1pm)+len(pais_externo_dia5_1pm)+len(pais_externo_dia6_1pm)+len(pais_externo_dia7_1pm))/7)
        promedio_2pm = round((len(pais_externo_dia1_2pm)+len(pais_externo_dia2_2pm)+len(pais_externo_dia3_2pm)+len(pais_externo_dia4_2pm)+len(pais_externo_dia5_2pm)+len(pais_externo_dia6_2pm)+len(pais_externo_dia7_2pm))/7)
        promedio_3pm = round((len(pais_externo_dia1_3pm)+len(pais_externo_dia2_3pm)+len(pais_externo_dia3_3pm)+len(pais_externo_dia4_3pm)+len(pais_externo_dia5_3pm)+len(pais_externo_dia6_3pm)+len(pais_externo_dia7_3pm))/7)
        promedio_4pm = round((len(pais_externo_dia1_4pm)+len(pais_externo_dia2_4pm)+len(pais_externo_dia3_4pm)+len(pais_externo_dia4_4pm)+len(pais_externo_dia5_4pm)+len(pais_externo_dia6_4pm)+len(pais_externo_dia7_4pm))/7)
        promedio_5pm = round((len(pais_externo_dia1_5pm)+len(pais_externo_dia2_5pm)+len(pais_externo_dia3_5pm)+len(pais_externo_dia4_5pm)+len(pais_externo_dia5_5pm)+len(pais_externo_dia6_5pm)+len(pais_externo_dia7_5pm))/7)
        promedio_6pm = round((len(pais_externo_dia1_6pm)+len(pais_externo_dia2_6pm)+len(pais_externo_dia3_6pm)+len(pais_externo_dia4_6pm)+len(pais_externo_dia5_6pm)+len(pais_externo_dia6_6pm)+len(pais_externo_dia7_6pm))/7)

        promedio_semana = [promedio_7am, promedio_8am, promedio_9am, promedio_10am, promedio_11am, promedio_12pm, promedio_1pm, promedio_2pm, promedio_3pm, promedio_4pm, promedio_5pm, promedio_6pm]

        plt.ylabel('Número de llamadas')
        plt.title('Promedio de llamadas externas por hora realizadas por ' + respuesta + ' del ' + dia1 + '-' + dia7)
        rects = plt.bar(Horas,promedio_semana, width=0.5)

        for r in rects:
            height = r.get_height() 
            plt.text(r.get_x() + r.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

        plt.show()