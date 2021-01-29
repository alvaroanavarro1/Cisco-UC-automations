# Cisco-UC-automations

Repositorio para la automatización de procesos de Cisco Call Manager en Soutec. Por los momentos se encuentran códigos para visualizar data y manipulación de datos para reportes:

- ## CAF:
  - [**CDR-CMR-Extractor-v2.py**](https://github.com/alvaroanavarro1/Cisco-UC-automations/blob/master/CAF/CDR-CMR-Extractor-v2.py): Código original de Brian Quintero para extracción de cdr y cmr.
  - [**Manual_Extractor.py**](https://github.com/alvaroanavarro1/Cisco-UC-automations/blob/master/CAF/Manual_Extractor.py): Código realizado para la extracción del reporte final, con archivos cdr y cmr extraídos manualmente.
  - [**CDR-CMR-Visualization_Test.py**](https://github.com/alvaroanavarro1/Cisco-UC-automations/blob/master/CAF/CDR-CMR-Visualization_Test.py): Código para visualización de llamadas salientes por país y duración de las mismas.
  - [**average_calls.py**](https://github.com/alvaroanavarro1/Cisco-UC-automations/blob/master/CAF/average_calls.py): Código para visualización de promedio de llamadas por hora para un periodo definido por el usuario. Aplica para llamadas internas y externas.
- ## Coca-Cola:
  - [**cocacola_report.py**](https://github.com/alvaroanavarro1/Cisco-UC-automations/blob/master/Coca-Cola/cocacola_report.py): Código para la manipulación de datos y completación para reporte de telefonos mensuales en Coca-Cola.

## Archivos CSV necesarios
Los archivos necesarios para correr estos programas son extraídos del Call Manager, estos archivos son:
- conferencebridge.csv
- devicepool.csv
- gateway.csv 
- phone.csv
- transcoder.csv
