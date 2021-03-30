from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin
from requests import Session
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from lxml import etree
import time


disable_warnings(InsecureRequestWarning)
username = 'administrator'
password = 'ccmcaf2015'
host = '10.200.160.30'

wsdl = 'C:/Users/anavarro/OneDrive - SOUTEC/Desktop/Soutec/Cisco-UC-automations/AXL/schema/current/AXLAPI.wsdl'
location = 'https://{host}:8443/axl/'.format(host=host)
binding = "{http://www.cisco.com/AXLAPIService/}AXLAPIBinding"

session = Session()
session.verify = False
session.auth = HTTPBasicAuth(username, password)

transport = Transport(cache=SqliteCache(), session=session, timeout=20)
history = HistoryPlugin()
client = Client(wsdl=wsdl, transport=transport, plugins=[history])
service = client.create_service(binding, location)

# Build Client Object for RisPort70 Service

Ris_wsdl = f'https://{host}:8443/realtimeservice2/services/RISService70?wsdl'

Ris_session = Session()
Ris_session.verify = False
Ris_session.auth = HTTPBasicAuth(username, password)

Ris_transport = Transport(cache=SqliteCache(), session=Ris_session, timeout=20)
Ris_client = Client(wsdl=Ris_wsdl, transport=transport, plugins=[history])




def show_history():
    for item in [history.last_sent, history.last_received]:
        print(etree.tostring(item["envelope"], encoding="unicode", pretty_print=True))


#try:
#    time.sleep(5)
#    resp = service.listPhone(searchCriteria={'name': 'SEP%'}, 
#                             returnedTags={'name': '',
#                'description': '',
#                'Status': 'Registered'
#            })
            
#    print(resp)


#except Fault:
#    show_history()

#tems = []
#for phone in phone_list:
#    items.append(phone.name)



CmSelectionCriteria = {
    'MaxReturnedDevices': '10',
    'DeviceClass': 'Phone',
    'Model': '255',
    'Status': 'Registered',
    'NodeName': '',
    'SelectBy': 'Name',
    'SelectItems': {
        'item': items
    },
    'Protocol': 'Any',
    'DownloadStatus': 'Any'
}

StateInfo = ''

try:
    time.sleep(5)
    resp = client.service.selectCmDeviceExt(CmSelectionCriteria=CmSelectionCriteria, StateInfo=StateInfo)
except Fault:
    show_history()

snapshot = {}
CmNodes = resp.SelectCmDeviceResult.CmNodes.item


