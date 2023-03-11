from datetime import datetime
import openpyxl  
import pprint
pp = pprint.PrettyPrinter(indent=4)
import random
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import folium
import datetime

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame()
main_url = 'https://www.reality.sk'
#'https://mobilne-telefony.heureka.sk', 'https://inteligentne-hodinky.heureka.sk/', 'https://televizor.heureka.sk/', 'https://sluchadla.heureka.sk/'
               
pokus = []
count  = 0
from bs4 import BeautifulSoup
import requests

ALL_data = {}  



import time

# Grab Currrent Time Before Running the Code



# Grab Currrent Time After Running the Code

start = time.time()

start_point = int(input("Print Start Point "))
end_point = int(input("Print End Point "))

https = ' https://'

import pyodbc
conn = pyodbc.connect(
"Driver={SQL Server};"
"Server=DESKTOP-F86F289;"
"Database =byty;"
"Trusted_Connection=yes;")
data = pd.read_sql("SELECT TOP(100000) * FROM byty.dbo.byty_links", conn)
#links = data['Links']
links = []
for x in data['links']:
    links.append(x)

    
    
for link in links[start_point:end_point]:  
    end = time.time()
    total_time = end - start
    #print("\n"+ str(total_time))
    #Subtract Start Time from The End Time
    start = time.time()
    table_data ={} 
    count = count + 1
    print(len(links[start_point:end_point]) -count)
    print(link)
    i = 0
    #browser.get(link)
    try:    
        #browser.find_element_by_class_name("show-more__button d-block").click()  
        #time.sleep(1)
        page = requests.get(https + link)
        soup = BeautifulSoup(page.text, 'html.parser')
        
    except Exception as e:
        pass
   
    try:
        paragraphs = []
        for x in soup:
            paragraphs.append(str(x))

        data_latitude = paragraphs[2][paragraphs[2].index('data-latitude'):paragraphs[2].index('data-longitude')].replace('data-latitude=','').replace('"', '').strip()
        table_data['latitude'] = data_latitude
   
        data_longitude = paragraphs[2][paragraphs[2].index('data-longitude'):paragraphs[2].index('data-zoom-level')].replace('data-longitude=', '').replace('"', '').strip()
        table_data['longitude'] = data_longitude
       
        nazov = soup.findAll(class_ = 'detail-title pt-4 pb-2')[0].get_text()
   
        table_data['Nazov'] = nazov
        text = soup.findAll('span', {'class': 'content-preview'})[0].get_text().replace('\n', '').replace('\xa0','')
        table_data['Text'] = text
   
        price = soup.findAll(class_ = 'contact-title big col-12 col-md-6 mb-0')[0].get_text()
        price = price[0:price.find('€')].strip()
        price = price.replace('\xa0', '')
        table_data['Cena'] = price
 
        



       
    except Exception as e:
        pass


    try:

        for x in soup.findAll('div', {'class' : 'row no-gutters mt-1'})[0]:
            key = soup.findAll('div', {'class' : 'row no-gutters mt-1'})[0].findAll('div', {'class' : 'col-sm-4 col-6 info-title'})[i].get_text()      
            value = soup.findAll('div', {'class' : 'row no-gutters mt-1'})[0].findAll('div', {'class' : 'col-sm-8 col-6'})[i].get_text()
            table_data[key] = value  
            pokus.append(key)
            pokus.append(value)
            i = i+1

    except Exception:
        pass

    i = 0
    try:
        for x in soup.findAll('div', {'class':'row no-gutters content-preview mt-1'})[0]:
            key2 = soup.findAll('div', {'class':'row no-gutters content-preview mt-1'})[0].findAll('div', {'class' : 'col-6 col-sm-4 info-title'})[i].get_text().replace('\n','').strip()
            value2 = soup.findAll('div', {'class':'row no-gutters content-preview mt-1'})[0].findAll('div', {'class' : 'col-6 col-sm-8'})[i].get_text()    
            table_data[key2] = value2
            pokus.append(key2)
            pokus.append(value2)
            i = i+1
           

    except Exception:
       
        pass

    ALL_data[count] = table_data
   

    my_dictionary = table_data



latitude_direction = []
longitude_direction = []
cena = []
Druh = []
Typ = []
Plocha = []
nazov = []
text = []
Nazov = []
Celková_podlahová_plocha = []
Nadzemné_podlažie = []
Stav_nehnuteľnosti = []
Forma_vlastníctva = []
Konštrukcia_bytu = []
Rok_výstavby = []
Terasa = []
Energetický_certifikát_budovy = []
Internet = []
Káblová_televízia = []
Uzitkova_Plocha = []
Pocet_izieb = []
ALL_keys_  = []


Funkčné_využitie=[]
Nazov=[]
Stav_nehnuteľnosti=[]
longitude=[]
Podpivničenie=[]
Vykurovanie=[]
Zastavaná_plocha=[]
latitude=[]
Rok_kolaudácie=[]
Voda=[]
Plyn=[]
Umiestnenie=[]
Terás=[]
Energie=[]
Počet_garáží=[]
Dĺžka_pozemku=[]
Cena=[]
Rok_poslednej_rekonštrukcie=[]
Vybavenie=[]
Elektrina=[]
Orientácia=[]
Prechodová_izba=[]
Šírka_pozemku=[]
Počet_izieb_miestností=[]
Počet_podzemných_podlaži=[]
Odpadové_vody=[]
Počet_nadzemných_podlaží=[]
Podlažie=[]
Telekomunikačné_a_dátové_pripojenie=[]
Typ=[]
Druh_domu=[]
Text=[]
Zariadenie=[]
Voľnočasové_aktivity=[]
Typ_konštrukcie=[]
Pivnica=[]
Počet_kúpeľní=[]
Počet_loggí=[]
Cellar_area=[]
Vlastníctvo=[]
Počet_balkónov=[]
Plocha_pozemku=[]
Bezpečnosť=[]
Druh=[]
Úžitková_plocha=[]
power_costs_in_the_price=[]
Rok_výstavby=[]
Prístupová_komunikácia=[]
Územie=[]




all_the_columns = ['Funkčné využitie:', 'Nazov', 'Nazov', 'Stav nehnuteľnosti:', 'longitude', 'Podpivničenie:', 'Vykurovanie:', 'Zastavaná plocha:', 'latitude', 'Rok kolaudácie:', 'Voda:', 'Plyn:', 'Umiestnenie:', 'Terás:', 'Energie:', 'Počet garáží:', 'Dĺžka pozemku:', 'Cena', 'Rok poslednej rekonštrukcie:', 'Vybavenie:', 'Elektrina:', 'Orientácia:', 'Prechodová izba:', 'Šírka pozemku:', 'Počet izieb / miestností:', 'Počet podzemných podlaži:', 'Odpadové vody:', 'Počet nadzemných podlaží:', 'Podlažie:', 'Telekomunikačné a dátové pripojenie:', 'Typ: ', 'Druh domu:', 'Text', 'Zariadenie:', 'Voľnočasové aktivity:', 'Typ konštrukcie:', 'Pivnica:', 'Počet kúpeľní:', 'Počet loggí:', 'Cellar area:', 'Vlastníctvo:', 'Počet balkónov:', 'Plocha pozemku:', 'Bezpečnosť:', 'Druh: ', 'Úžitková plocha:', 'power_costs_in_the_price:', 'Rok výstavby:', 'Prístupová komunikácia:', 'Územie:']
all_the_lists = [Funkčné_využitie,Nazov,Stav_nehnuteľnosti,longitude,Podpivničenie,Vykurovanie,Zastavaná_plocha,latitude,Rok_kolaudácie,Voda,Plyn,Umiestnenie,Terás,Energie,Počet_garáží,Dĺžka_pozemku,Cena,Rok_poslednej_rekonštrukcie,Vybavenie,Elektrina,Orientácia,Prechodová_izba,Šírka_pozemku,Počet_izieb_miestností,Počet_podzemných_podlaži,Odpadové_vody,Počet_nadzemných_podlaží,Podlažie,Telekomunikačné_a_dátové_pripojenie,Typ,Druh_domu,Text,Zariadenie,Voľnočasové_aktivity,Typ_konštrukcie,Pivnica,Počet_kúpeľní,Počet_loggí,Cellar_area,Vlastníctvo,Počet_balkónov,Plocha_pozemku,Bezpečnosť,Druh,Úžitková_plocha,power_costs_in_the_price,Rok_výstavby,Prístupová_komunikácia,Územie
]

for key in ALL_data:
    
    try:
        for x in ALL_data[key]:
            ALL_keys_.append(x)
    except Exception as e: 
        pass
    

  
   
    ##pg = -1
    ##for x in all_the_columns:
        ##pg += 1
        ##try:
            ##all_the_lists[pg].append(ALL_data[key][all_the_columns[pg]])
            
        ##except Exception as e:
            ##all_the_lists[pg].append("-")
            
    try:
        Funkčné_využitie.append(ALL_data[key]["Funkčné využitie:"])
    except Exception as e:
        Funkčné_využitie.append('-')

    try:
        Nazov.append(ALL_data[key][ 'Nazov'])
    except Exception as e:
        Nazov.append('-')

    try:
        Stav_nehnuteľnosti.append(ALL_data[key][ 'Stav nehnuteľnosti:'])
    except Exception as e:
        Stav_nehnuteľnosti.append('-')

    try:
        longitude.append(ALL_data[key][ 'longitude'])
    except Exception as e:
        longitude.append('-')

    try:
        Podpivničenie.append(ALL_data[key][ 'Podpivničenie:'])
    except Exception as e:
        Podpivničenie.append('-')

    try:
        Vykurovanie.append(ALL_data[key][ 'Vykurovanie:'])
    except Exception as e:
        Vykurovanie.append('-')

    try:
        Zastavaná_plocha.append(ALL_data[key][ 'Zastavaná plocha:'])
    except Exception as e:
        Zastavaná_plocha.append('-')

    try:
        latitude.append(ALL_data[key][ 'latitude'])
    except Exception as e:
        latitude.append('-')

    try:
        Rok_kolaudácie.append(ALL_data[key][ 'Rok kolaudácie:'])
    except Exception as e:
        Rok_kolaudácie.append('-')

    try:
        Voda.append(ALL_data[key][ 'Voda:'])
    except Exception as e:
        Voda.append('-')

    try:
        Plyn.append(ALL_data[key][ 'Plyn:'])
    except Exception as e:
        Plyn.append('-')

    try:
        Umiestnenie.append(ALL_data[key][ 'Umiestnenie:'])
    except Exception as e:
        Umiestnenie.append('-')

    try:
        Terás.append(ALL_data[key]['Terás'])
    except Exception as e:
        Terás.append('-')

    try:
        Energie.append(ALL_data[key][ 'Energie:'])
    except Exception as e:
        Energie.append('-')

    try:
        Počet_garáží.append(ALL_data[key][ 'Počet garáží:'])
    except Exception as e:
        Počet_garáží.append('-')

    try:
        Dĺžka_pozemku.append(ALL_data[key][ 'Dĺžka pozemku:'])
    except Exception as e:
        Dĺžka_pozemku.append('-')

    try:
        Cena.append(ALL_data[key][ 'Cena'])
    except Exception as e:
        Cena.append('-')

    try:
        Rok_poslednej_rekonštrukcie.append(ALL_data[key][ 'Rok poslednej rekonštrukcie:'])
    except Exception as e:
        Rok_poslednej_rekonštrukcie.append('-')

    try:
        Vybavenie.append(ALL_data[key][ 'Vybavenie:'])
    except Exception as e:
        Vybavenie.append('-')

    try:
        Elektrina.append(ALL_data[key][ 'Elektrina:'])
    except Exception as e:
        Elektrina.append('-')

    try:
        Orientácia.append(ALL_data[key][ 'Orientácia:'])
    except Exception as e:
        Orientácia.append('-')

    try:
        Prechodová_izba.append(ALL_data[key][ 'Prechodová izba:'])
    except Exception as e:
        Prechodová_izba.append('-')

    try:
        Šírka_pozemku.append(ALL_data[key][ 'Šírka pozemku:'])
    except Exception as e:
        Šírka_pozemku.append('-')

    try:
        Počet_izieb_miestností.append(ALL_data[key][ 'Počet izieb / miestností:'])
    except Exception as e:
        Počet_izieb_miestností.append('-')

    try:
        Počet_podzemných_podlaži.append(ALL_data[key][ 'Počet podzemných podlaži:'])
    except Exception as e:
        Počet_podzemných_podlaži.append('-')

    try:
        Odpadové_vody.append(ALL_data[key][ 'Odpadové vody:'])
    except Exception as e:
        Odpadové_vody.append('-')

    try:
        Počet_nadzemných_podlaží.append(ALL_data[key][ 'Počet nadzemných podlaží:'])
    except Exception as e:
        Počet_nadzemných_podlaží.append('-')

    try:
        Podlažie.append(ALL_data[key][ 'Podlažie:'])
    except Exception as e:
        Podlažie.append('-')

    try:
        Telekomunikačné_a_dátové_pripojenie.append(ALL_data[key][ 'Telekomunikačné a dátové pripojenie:'])
    except Exception as e:
        Telekomunikačné_a_dátové_pripojenie.append('-')

    try:
        Typ.append(ALL_data[key][ 'Typ: '])
    except Exception as e:
        Typ.append('-')

    try:
        Druh_domu.append(ALL_data[key][ 'Druh domu:'])
    except Exception as e:
        Druh_domu.append('-')

    try:
        Text.append(ALL_data[key][ 'Text'])
    except Exception as e:
        Text.append('-')

    try:
        Zariadenie.append(ALL_data[key][ 'Zariadenie:'])
    except Exception as e:
        Zariadenie.append('-')

    try:
        Voľnočasové_aktivity.append(ALL_data[key][ 'Voľnočasové aktivity:'])
    except Exception as e:
        Voľnočasové_aktivity.append('-')

    try:
        Typ_konštrukcie.append(ALL_data[key][ 'Typ konštrukcie:'])
    except Exception as e:
        Typ_konštrukcie.append('-')

    try:
        Pivnica.append(ALL_data[key][ 'Pivnica:'])
    except Exception as e:
        Pivnica.append('-')

    try:
        Počet_kúpeľní.append(ALL_data[key][ 'Počet kúpeľní:'])
    except Exception as e:
        Počet_kúpeľní.append('-')

    try:
        Počet_loggí.append(ALL_data[key][ 'Počet loggí:'])
    except Exception as e:
        Počet_loggí.append('-')

    try:
        Cellar_area.append(ALL_data[key][ 'Cellar area:'])
    except Exception as e:
        Cellar_area.append('-')

    try:
        Vlastníctvo.append(ALL_data[key][ 'Vlastníctvo:'])
    except Exception as e:
        Vlastníctvo.append('-')

    try:
        Počet_balkónov.append(ALL_data[key][ 'Počet balkónov:'])
    except Exception as e:
        Počet_balkónov.append('-')

    try:
        Plocha_pozemku.append(ALL_data[key][ 'Plocha pozemku:'])
    except Exception as e:
        Plocha_pozemku.append('-')

    try:
        Bezpečnosť.append(ALL_data[key][ 'Bezpečnosť:'])
    except Exception as e:
        Bezpečnosť.append('-')

    try:
        Úžitková_plocha.append(ALL_data[key][ 'Úžitková plocha:'])
    except Exception as e:
        Úžitková_plocha.append('-')
        
    try:
        Druh.append(ALL_data[key]['Druh: '])
    except Exception as e:
        Druh.append('-')    

    try:
        power_costs_in_the_price.append(ALL_data[key][ 'power_costs_in_the_price:'])
    except Exception as e:
        power_costs_in_the_price.append('-')

    try:
        Rok_výstavby.append(ALL_data[key][ 'Rok výstavby:'])
    except Exception as e:
        Rok_výstavby.append('-')

    try:
        Prístupová_komunikácia.append(ALL_data[key]['Prístupová komunikácia'])
    except Exception as e:
        Prístupová_komunikácia.append('-')

    try:
        Územie.append(ALL_data[key][ 'Územie:'])
    except Exception as e:
        Územie.append('-')
            
                           
try:



    df["Funkčné_využitie"]=Funkčné_využitie
    df["Nazov"]=Nazov
    df["Stav_nehnuteľnosti"]=Stav_nehnuteľnosti
    df["longitude"]=longitude
    df["Podpivničenie"]=Podpivničenie
    df["Vykurovanie"]=Vykurovanie
    df["Zastavaná_plocha"]=Zastavaná_plocha
    df["latitude"]=latitude
    df["Rok_kolaudácie"]=Rok_kolaudácie
    df["Voda"]=Voda
    df["Plyn"]=Plyn
    df["Umiestnenie"]=Umiestnenie
    df["Terás"]=Terás
    df["Energie"]=Energie
    df["Počet_garáží"]=Počet_garáží
    df["Dĺžka_pozemku"]=Dĺžka_pozemku
    df["Cena"]=Cena
    df["Rok_poslednej_rekonštrukcie"]=Rok_poslednej_rekonštrukcie
    df["Vybavenie"]=Vybavenie
    df["Elektrina"]=Elektrina
    df["Orientácia"]=Orientácia
    df["Prechodová_izba"]=Prechodová_izba
    df["Šírka_pozemku"]=Šírka_pozemku
    df["Počet_izieb_miestností"]=Počet_izieb_miestností
    df["Počet_podzemných_podlaži"]=Počet_podzemných_podlaži
    df["Odpadové_vody"]=Odpadové_vody
    df["Počet_nadzemných_podlaží"]=Počet_nadzemných_podlaží
    df["Podlažie"]=Podlažie
    df["Telekomunikačné_a_dátové_pripojenie"]=Telekomunikačné_a_dátové_pripojenie
    df["Typ"]=Typ
    df["Druh_domu"]=Druh_domu
    df["Text"]=Text
    df["Zariadenie"]=Zariadenie
    df["Voľnočasové_aktivity"]=Voľnočasové_aktivity
    df["Typ_konštrukcie"]=Typ_konštrukcie
    df["Pivnica"]=Pivnica
    df["Počet_kúpeľní"]=Počet_kúpeľní
    df["Počet_loggí"]=Počet_loggí
    df["Cellar_area"]=Cellar_area
    df["Vlastníctvo"]=Vlastníctvo
    df["Počet_balkónov"]=Počet_balkónov
    df["Plocha_pozemku"]=Plocha_pozemku
    df["Bezpečnosť"]=Bezpečnosť
    df["Druh"]=Druh
    df["Úžitková_plocha"]=Úžitková_plocha
    df["power_costs_in_the_price"]=power_costs_in_the_price
    df["Rok_výstavby"]=Rok_výstavby
    df["Prístupová_komunikácia"]=Prístupová_komunikácia
    df["Územie"]=Územie

except Exception as e:
    pass

links_final = []
mm = 0
for x in links[start_point:end_point]:
    links_final.append(x)
    mm +=1
df['Links_Final'] = links_final



date = []
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
df['date'] = current_time




df['Zastavaná_plocha']  = [x.replace(' m²','').replace('\xa0','').replace(',','.') for x in df['Zastavaná_plocha']]
df['Energie']  = [x.replace(' €','').replace('\xa0','').replace(',','.') for x in df['Energie']]
df['Cellar_area']  = [x.replace(' m²','').replace('\xa0','').replace(',','.') for x in df['Cellar_area']]
df['Úžitková_plocha']  = [x.replace(' m²','').replace('\xa0','').replace(',','.') for x in df['Úžitková_plocha']]
df['Plocha_pozemku']  = [x.replace(' m²','').replace('\xa0','').replace(',','.') for x in df['Plocha_pozemku']]
df['Cena']  = [x.replace(',','.') for x in df['Cena']]
df.to_csv(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\byty\Byty.csv', encoding = 'utf-8-sig')
