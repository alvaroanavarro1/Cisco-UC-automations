from ciscoaxl import axl
import time


CUCM = '10.200.160.30'
CUCM_USER = "administrator"
CUCM_PASSWORD = "Caf.2019"
CUCM_VERSION = '10.5'

ucm = axl(username=CUCM_USER,password=CUCM_PASSWORD,cucm=CUCM,cucm_version=CUCM_VERSION)
for phone in ucm.get_phones():
    print(phone.name)