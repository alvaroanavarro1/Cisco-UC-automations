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


try:
    time.sleep(5)
    resp = service.listPhone(searchCriteria={'name': 'SEP%'}, 
                             returnedTags={'name': '',
                'description': '',
                'product': '',
                'model': '',
                'class': '',
                'protocol': '',
                'protocolSide': '',
                'callingSearchSpaceName': '',
                'devicePoolName': '',
                'commonDeviceConfigName': '',
                'commonPhoneConfigName': '',
                'networkLocation': '',
                'locationName': '',
                'mediaResourceListName': '',
                'networkHoldMohAudioSourceId': '',
                'userHoldMohAudioSourceId': '',
                'automatedAlternateRoutingCssName': '',
                'aarNeighborhoodName': '',
                'loadInformation': '',
                'traceFlag': '',
                'mlppIndicationStatus': '',
                'preemption': '',
                'useTrustedRelayPoint': '',
                'retryVideoCallAsAudio': '',
                'securityProfileName': '',
                'sipProfileName': '',
                'cgpnTransformationCssName': '',
                'useDevicePoolCgpnTransformCss': '',
                'geoLocationName': '',
                'geoLocationFilterName': '',
                'sendGeoLocation': '',
                'numberOfButtons': '',
                'phoneTemplateName': '',
                'primaryPhoneName': '',
                'ringSettingIdleBlfAudibleAlert': '',
                'ringSettingBusyBlfAudibleAlert': '',
                'userLocale': '',
                'networkLocale': '',
                'idleTimeout': '',
                'authenticationUrl': '',
                'directoryUrl': '',
                'idleUrl': '',
                'informationUrl': '',
                'messagesUrl': '',
                'proxyServerUrl': '',
                'servicesUrl': '',
                'softkeyTemplateName': '',
                'loginUserId': '',
                'defaultProfileName': '',
                'enableExtensionMobility': '',
                'currentProfileName': '',
                'loginTime': '',
                'loginDuration': '',
                'currentConfig': '',
                'singleButtonBarge': '',
                'joinAcrossLines': '',
                'builtInBridgeStatus': '',
                'callInfoPrivacyStatus': '',
                'hlogStatus': '',
                'ownerUserName': '',
                'ignorePresentationIndicators': '',
                'packetCaptureMode': '',
                'packetCaptureDuration': '',
                'subscribeCallingSearchSpaceName': '',
                'rerouteCallingSearchSpaceName': '',
                'allowCtiControlFlag': '',
                'presenceGroupName': '',
                'unattendedPort': '',
                'requireDtmfReception': '',
                'rfc2833Disabled': '',
                'certificateOperation': '',
                'authenticationMode': '',
                'keySize': '',
                'authenticationString': '',
                'certificateStatus': '',
                'upgradeFinishTime': '',
                'deviceMobilityMode': '',
                'roamingDevicePoolName': '',
                'remoteDevice': '',
                'dndOption': '',
                'dndRingSetting': '',
                'dndStatus': '',
                'isActive': 'true',
                'isDualMode': '',
                'mobilityUserIdName': '',
                'phoneSuite': '',
                'phoneServiceDisplay': '',
                'isProtected': '',
                'mtpRequired': '',
                'mtpPreferedCodec': '',
                'dialRulesName': '',
                'sshUserId': '',
                'digestUser': '',
                'outboundCallRollover': '',
                'hotlineDevice': '',
                'secureInformationUrl': '',
                'secureDirectoryUrl': '',
                'secureMessageUrl': '',
                'secureServicesUrl': '',
                'secureAuthenticationUrl': '',
                'secureIdleUrl': '',
                'alwaysUsePrimeLine': '',
                'alwaysUsePrimeLineForVoiceMessage': '',
                'featureControlPolicy': '',
                'deviceTrustMode': '',
                'earlyOfferSupportForVoiceCall': '',
                'requireThirdPartyRegistration': '',
                'blockIncomingCallsWhenRoaming': '',
                'homeNetworkId': '',
                'AllowPresentationSharingUsingBfcp': '',
                'confidentialAccess': '',
                'requireOffPremiseLocation': '',
                'allowiXApplicableMedia': '',
                'enableCallRoutingToRdWhen':''
            })
            
    print(resp)


except Fault:
    show_history()

items = []
#for phone in phone_list:
#    items.append(phone.name)



CmSelectionCriteria = {
    'MaxReturnedDevices': '10',
    'DeviceClass': 'Phone',
    'Model': '255',
    'Status': 'Any',
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
    #time.sleep(5)
    resp = client.service.selectCmDeviceExt(CmSelectionCriteria=CmSelectionCriteria, StateInfo=StateInfo)
except Fault:
    show_history()

snapshot = {}
CmNodes = resp.SelectCmDeviceResult.CmNodes.item


