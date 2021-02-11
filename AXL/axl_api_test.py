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

def show_history():
    for item in [history.last_sent, history.last_received]:
        print(etree.tostring(item["envelope"], encoding="unicode", pretty_print=True))

try:
    time.sleep(5)
    resp = service.listPhone(searchCriteria={'name': '%'}, 
                             returnedTags={'name': '', 'description': ''})
                            
    print(resp)
    phone_list = resp['return'].phone
    #for phone in phone_list:
        #print(phone.name)
        
except Fault:
    show_history()
