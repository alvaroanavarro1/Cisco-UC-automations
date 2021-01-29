import pandas as pd
import os as os
import re
import time, threading
import schedule
import datetime as dt
import pytz as pytz
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import io
from io import StringIO


client = 'CAF'

# SOURCE FILES #
folder  = r'C:\Users\anavarro\OneDrive - SOUTEC\Desktop\Soutec\Cisco-UC-automations'
file_phone = pd.read_csv("phone.csv", low_memory=False)
file_gw = pd.read_csv("gateway.csv", low_memory=False)
file_dp = pd.read_csv("devicepool.csv", low_memory=False)
file_cfb = pd.read_csv("conferencebridge.csv", low_memory=False)
file_xcode = pd.read_csv("transcoder.csv", low_memory=False)

folder_data = r'C:\Users\anavarro\OneDrive - SOUTEC\Desktop\Soutec\Cisco-UC-automations\data'

# CMR DATA #
filter_colum_metrics =[

'orignumberPacketsSent',
'orignumberPacketsReceived','orignumberPacketsLost','origjitter','origlatency','destnumberPacketsSent',
'destnumberPacketsReceived','destnumberPacketsLost','destjitter','destlatency'
]

# OUTPUT DATA #


# TIME ZONES #

Argentina = {'site':'Argentina', 'timezone': 'America/Argentina/Buenos_Aires'}
Brasil = {'site':'Brasil', 'timezone':'Etc/GMT+3'}
Bolivia = {'site':'Bolivia', 'timezone': 'America/La_Paz'}
Colombia = {'site':'Colombia', 'timezone': 'America/Bogota'}
Espana = {'site':'Espana', 'timezone': 'Europe/Madrid'}
Ecuador = {'site':'Ecuador', 'timezone':'America/Guayaquil'}
Mexico = {'site':'Mexico', 'timezone': 'America/Cancun'}
Peru = {'site':'Peru', 'timezone': 'America/Lima'}
Paraguay = {'site':'Paraguay', 'timezone':'America/Asuncion'}
Panama = {'site':'Panama', 'timezone':'America/Panama'}
TYT =  {'site':'TYT', 'timezone':'America/Port_of_Spain'}
Uruguay = {'site':'Uruguay', 'timezone':'America/Argentina/Buenos_Aires'}
Venezuela = {'site':'Venezuela', 'timezone':'Etc/GMT+4'}
Miami =  {'site':'Miami', 'timezone':'America/New_York'}
sites = [Argentina,Brasil,Bolivia,Colombia,Espana,Ecuador,Mexico,Peru,Paraguay,Panama,TYT,Uruguay,Venezuela,Miami]


def get_location(DeviceName):
    value = str(DeviceName)
    print(value)

    if value == 'csfms38680':
        aux_value = 'Venezuela'
        return aux_value
        
    if re.match('^SEP.*$|^[Cc][Ss][Ff].*$|^[Tt][Cc][Tt].*$|^BOT.*$', value):
        #print('1')
        # Busco DeviceName en archivo phone.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_phone.loc[file_phone['Device Name'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'Device Pool'])
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|^AALN.*$|^AN.*$|^VG.*$|^Trunk.*$|^SIP.*', value):
        #print('2')
        # Busco DeviceName en archivo gateway.csv, mapeo el Device Pool. Luego Busco Device Pool en archivo devicepool.csv y mapeo DATE/TIME GROUP.
        file_temp = file_gw.loc[file_gw['DEVICE NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value


    elif re.match('^CFB_[0-9].*$|^ANN_[0-9].*$|^MTP_[0-9].*$|^EXTMTP.*$', value):
        #print('3')
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^Conductor.*$|^HD_bridge.*$|^MCU.*$', value):
        #print('4')
        aux_value = 'Miami'
        
        return aux_value
    
    elif re.match('^CFB.*$', value):
        #print('5')
        file_temp = file_cfb.loc[file_cfb['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL'] 
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]
        return aux_value

    elif re.match('^XCODE.*$', value):
        #print('6')
        file_temp = file_xcode.loc[file_xcode['NAME'].str.contains(value, case=False)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = file_reindex.at[0, 'DEVICE POOL']
        file_temp = file_dp.loc[file_dp['DEVICE POOL NAME'].str.contains(aux_value)]
        file_reindex = file_temp.reset_index(drop=True)
        aux_value = str(file_reindex.at[0, 'DATE/TIME GROUP']).split(sep='_')[1]

        return aux_value
    
    elif re.match('^Parking.*$|^CAF.*$|^CiscoUM1.*', value):
        #print('7')
        aux_value = 'Miami'
        
        return aux_value


def get_time(x):

    source = str(x.source)

    for aux in sites:
        if source == aux['site']:
            time_zone = pytz.timezone(aux['timezone'])
            x_new = x
            try:
                x_new.dateTimeOrigination1 = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone)
                x_new.month = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%B')
                x_new.year = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%Y')
                x_new.day = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%d')
                x_new.hour = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime('%I %p')
                x_new.dateTimeOrigination = dt.datetime.fromtimestamp(x_new.dateTimeOrigination).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
            except:
                pass
            try:
                x_new.dateTimeConnect1 = dt.datetime.fromtimestamp(x_new.dateTimeConnect).astimezone(time_zone)
                x_new.dateTimeConnect = dt.datetime.fromtimestamp(x_new.dateTimeConnect).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
            except:
                pass
            try:
                x_new.dateTimeDisconnect1 = dt.datetime.fromtimestamp(x_new.dateTimeDisconnect).astimezone(time_zone)
                x_new.dateTimeDisconnect = dt.datetime.fromtimestamp(x_new.dateTimeDisconnect).astimezone(time_zone).strftime(r'%d/%b/%Y, %I:%M, %p')
                x_new.source = x.source
                return x_new
                break
            except:
                pass
                return x_new
                break
        else:
            None

def change(file_cdr):
    
    file_cdr['dateTimeOrigination1'] = file_cdr['dateTimeOrigination']
    file_cdr['dateTimeConnect1'] = file_cdr['dateTimeConnect']
    file_cdr['dateTimeDisconnect1'] = file_cdr['dateTimeDisconnect']
    file_cdr.insert(4, 'year', 0)
    file_cdr.insert(5, 'month', 0)
    file_cdr.insert(6, 'day', 0)
    file_cdr.insert(7, 'hour', 0)
    file_cdr.insert(8, 'source', 0)
    file_cdr.insert(9, 'destination', 0)
    file_cdr.insert(10, 'concurrency', 0)
    
    print("Step 1. Please wait. Mapping source/destination and verifying timezones.\n")
    #file_cdr.to_csv(r'D:\Desktop-Backup\Temp\ProjectCDR-CMR\Sub-Import-Project\CAF\result-test.csv')
    file_cdr['source'] = file_cdr['origDeviceName'].apply(lambda x: get_location(x))
    file_cdr['destination'] = file_cdr['destDeviceName'].apply(lambda x: get_location(x))
    # Mapping Time:
    time_values_loc = ['year','month', 'day', 'hour', 'dateTimeOrigination1', 'dateTimeConnect1', 'dateTimeDisconnect1','dateTimeOrigination', 'dateTimeConnect', 'dateTimeDisconnect', 'source']
    file_cdr[time_values_loc] = file_cdr[time_values_loc].apply(get_time, axis=1)
    print("Step 1. Done!")
    
    return file_cdr


def copy_func(file_cdr):
    
    print("Step 2. Creating Month Files")
    file_month = file_cdr['month']
    file_month = file_month.drop_duplicates()
    file_month = file_month.reset_index(drop=True)
    file_month = file_month.dropna()
    file_year = file_cdr['year']
    file_year = file_year.drop_duplicates()
    file_year = file_year.reset_index(drop=True)
    file_year = file_year.dropna()

    for year in file_year:
    
        for month in file_month:
        
            file_aux = file_cdr.loc[(file_cdr['month']== month) & (file_cdr['year']== year)]
            path = os.path.join(folder_data,'{0}-CDR-{1}-{2}.csv'.format(client,month,year))
            #print(path)
            if os.path.exists(folder_data):

                try:
                    filea = pd.read_csv(path, low_memory=False)
                    filea = pd.concat([filea,file_aux]).drop_duplicates(subset=['globalCallID_callId','origLegCallIdentifier','destLegIdentifier'], keep="first", sort=False).reset_index(drop=True)
                    filea = filea.to_csv(path, index=False)
                except:
                    file_aux = file_aux.to_csv(path, index=False)
            else:
                os.mkdir(folder_data)
                file_aux = file_aux.to_csv(path,index=False)
        
    print("Step 2. Done!")
        

def execute():
    
    global Flag
    
    cucmip= '10.200.160.30'
    driver = webdriver.Firefox(executable_path=r'C:\Users\anavarro\OneDrive - SOUTEC\Desktop\Soutec\Cisco-UC-automations\geckodriver.exe')
    driver.get(r'https://{0}/car/'.format(cucmip))
    driver.find_element_by_name('j_username').send_keys('administrator')
    driver.find_element_by_name('j_password').send_keys('ccmcaf2015')
    act = ActionChains(driver)
    act.click(driver.find_element_by_xpath(r'//*[@id="cmdLogin"]')).perform()
    time.sleep(10)
    driver.switch_to.window('WarningMessage')
    time.sleep(5)
    
    #Get Oldest Information

    oldest_record = driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[8]/td/font/b')
    print('Oldest record is {0}'.format(oldest_record.text))
    oldest_month = oldest_record .text.split(sep=',')[0].split(sep=' ')[0]
    oldest_day =  oldest_record .text.split(sep=',')[0].split(sep=' ')[1]
    oldest_year = oldest_record .text.split(sep=',')[1].split(sep=' ')[1]

    #Get Latest Information

    latest_record = driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[7]/td/font/b')
    print('Latest record is {0}'.format(latest_record.text))
    latest_month = latest_record.text.split(sep=',')[0].split(sep=' ')[0]
    latest_day =  latest_record.text.split(sep=',')[0].split(sep=' ')[1]
    latest_year = latest_record.text.split(sep=',')[1].split(sep=' ')[1]


    #driver.get(r'https://{0}/car/'.format(cucmip))
    #driver.switch_to.window('WarningMessage')

    driver.get(r'https://{0}/car/CallDetailExport.jsp'.format(cucmip))
    driver.refresh()
    time.sleep(10)


    #Selecting Latest
    #print('Latest month is {0}'.format(latest_month))
    select2 = Select(driver.find_element_by_id('cboMonthTo'))
    select2.select_by_visible_text(latest_month)
    #print('Latest year is {0}'.format(latest_year))
    select2 = Select(driver.find_element_by_id('cboYearTo'))
    select2.select_by_value(latest_year)
    #print('latest day is {0}'.format(latest_day))
    driver.find_element_by_xpath('//*[@id="txtDateTo"]').clear()
    driver.find_element_by_xpath('//*[@id="txtDateTo"]').send_keys(latest_day)
    
    #Selecting Oldest
        
    #print('Oldest month is {0}'.format(oldest_month))
    select1 = Select(driver.find_element_by_id('cboMonthFrom'))
    select1.select_by_visible_text(oldest_month)
    #print('Oldest year is {0}'.format(oldest_year))
    select1 = Select(driver.find_element_by_id('cboYearFrom'))
    select1.select_by_visible_text(oldest_year)
    #print('Oldest day is {0}'.format(oldest_day))
    driver.find_element_by_xpath('//*[@id="txtDateFrom"]').clear()
    driver.find_element_by_xpath('//*[@id="txtDateFrom"]').send_keys(oldest_day)
    
    button = driver.find_element_by_xpath("//input[contains(@id,'cmdExportDump')]")
    button.click()
    time.sleep(10)

    #Find href links:
    html = driver.page_source
    soup = BeautifulSoup(html,features='html.parser')
    tags = soup('a')
    main_report_path = 'https://{0}'.format(cucmip)

    for tag in tags:
    
        if re.match(r'.*CDR\.txt.*', str(tag.get('href'))):
           record_path = tag.get('href')
           cdr_path = main_report_path + record_path
           print(cdr_path)
           driver.get(cdr_path)
           htmlaux = driver.page_source
           soupaux = BeautifulSoup(htmlaux,features='html.parser')
           dataux = soupaux.find('pre').contents[0]
           file_cdr = pd.read_csv(StringIO(dataux),low_memory=False)
        elif re.match(r'.*CMR\.txt.*', str(tag.get('href'))):
           record_path = tag.get('href')
           cmr_path = main_report_path + record_path
           print(cmr_path)
           driver.get(cmr_path)
           htmlaux = driver.page_source
           soupaux = BeautifulSoup(htmlaux,features='html.parser')
           dataux = soupaux.find('pre').contents[0]
           file_cmr = pd.read_csv(StringIO(dataux),low_memory=False)
        else:
            None
    driver.quit()
    
    file_cmr = file_cmr[filter_colum_metrics]
    file_cdr = pd.concat([file_cdr, file_cmr], axis=1, sort=False)
    file_cdr.to_csv('CAF-CDR3.csv')
    #file_cdr = pd.read_csv('CAF-CDR3.csv',low_memory=False)
    #file_cdr = change(file_cdr)
    #file_cdr.to_csv('file_cdr.csv')
    #copy_func(file_cdr)


#execute()









