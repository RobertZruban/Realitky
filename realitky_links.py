import openpyxl  
import pprint
pp = pprint.PrettyPrinter(indent=4)
import random
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import folium

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame()
url = 'https://www.reality.sk/nitriansky-kraj/?page='
main_url = 'https://www.reality.sk'
#'https://mobilne-telefony.heureka.sk', 'https://inteligentne-hodinky.heureka.sk/', 'https://televizor.heureka.sk/', 'https://sluchadla.heureka.sk/'
               
kraje = ['https://www.reality.sk/bratislavsky-kraj/?page=', 'https://www.reality.sk/kosicky-kraj/?page=', 'https://www.reality.sk/nitriansky-kraj/?page=', 'https://www.reality.sk/trnavsky-kraj/?page=', 'https://www.reality.sk/trenciansky-kraj/?page=', 'https://www.reality.sk/zilinsky-kraj/?page=', 'https://www.reality.sk/banskobystricky-kraj/?page=', 'https://www.reality.sk/presovsky-kraj/?page=']

    
    
   
Values_all = []   
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
ALL_data = {}  
Region = []


 
l = 0
j = 0



browser = webdriver.Chrome(r'C:\Users\roboz.DESKTOP-F86F289\Desktop\chromedrive\chromedriver')
links = []
 
count  = 0
pokus = []  

for l in range(0,len(kraje)):

    for x in range(0,500):
        try:

            browser.get(kraje[l] + str(x))
            ###### TO CLICK I ACCEPT COOKIES ######s
            try:
                browser.find_element_by_class_name("fc-button-label").click()
            except Exception as e:
                pass
            ###################################    
            #time.sleep(1)

            html_source = browser.page_source  
            soup = BeautifulSoup(html_source,'html.parser')
            offers = soup.findAll('div', {'class' : 'offer_list'})


            ##### TO GET ALL OF THE LINKS WITH FLATS#######
            lol = offers[0].findAll('div', {'class': 'offer-item-in'})
            i = 0
            for lol in lol:
                wtf = lol.findAll('div', {'class', "col-sm ml-sm-3 mr-sm-3 offer-body"})[0].findAll('a', href=True)[0].get('href')
                links.append(wtf)
                Region.append(kraje[l])
                i = i +1
        except:
            pass
    ###################################
