import csv
import json
import sys
import os
from pathlib import Path
from datetime import datetime
from ciscoaxl import axl
import argparse


CUCM = '10.200.160.30'
CUCM_USER = "axl-phones"
CUCM_PASSWORD = "Cisc0123."
CUCM_VERSION = '10.5'

ucm = axl(
username=CUCM_USER,
password=CUCM_PASSWORD,
cucm=CUCM,
cucm_version=CUCM_VERSION)

#for phone in ucm.get_phones():
#    print(phone.name)

#def export_users(ucm_axl):
#    """
#    retrieve users from ucm
#    """
#    user_list = ucm_axl.get_users(
#        tagfilter={
#            "userid": "",
#            "firstName": "",
#            "lastName": "",
#            "directoryUri": "",
#            "telephoneNumber": "",
#            "enableCti": "",
#            "mailid": "",
#            "primaryExtension": {"pattern": "", "routePartitionName": ""},
#            "enableMobility": "",
#            "homeCluster": "",
#            "associatedPc": "",
#            "enableEmcc": "",
#            "imAndPresenceEnable": "",
#            "serviceProfile": {"_value_1": ""},
#            "status": "",
#            "userLocale": "",
#            "title": "",
#            "subscribeCallingSearchSpaceName": "",
#        }
#    )
#    all_users = []

#    for user in user_list:
        # print(user)
#        user_details = {}
#        user_details['userid'] = user.userid
#        user_details['firstName'] = user.firstName
#        user_details['lastName'] = user.lastName
#        user_details['telephoneNumber'] = user.telephoneNumber
#        user_details['primaryExtension'] = user.primaryExtension.pattern
#        user_details['directoryUri'] = user.directoryUri
#        user_details['mailid'] = user.mailid
#        user_details['status'] = user.status

#        all_users.append(user_details)
#        print(
#            f"{user_details.get('userid')} -- {user_details.get('firstName')} {user_details.get('lastName')}:  {user_details.get('status')}"
#        )

#    print("-" * 35)
#    print(f"number of users: {len(all_users)}")
    #print(user_list)
    # print(json.dumps(all_users, indent=2))
#    return all_users

#export_users(ucm)