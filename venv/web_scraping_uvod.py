#nase knihovny
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
import pandas as pd


#definice promennych
#url = "https://www.superhry.cz/skakacky/" #".Glist a.screenLink"
url = "https://www.smartprague.eu/news" #
odelovac = "-" * 80


#akcni cast kodu
def stahni_list_odkazu(url:str, selector:str) -> list:
    """Tato funkce stahne url adresy ze zvoleneho slectoru"""
    r = requests.get(url)
    print("Prosim vypis mi 200: ", r.status_code)
    html = r.text
    #print(html)
    soup = BeautifulSoup(html, "html.parser")
    href_list = []
    for i, a_elem in enumerate(soup.select(selector)[:5], 1):
        #print(odelovac)
        #print(i, a_elem["href"], a_elem["title"]) #tohle vypise poradi, href a title
        #print(odelovac)
        #print(urljoin(url, a_elem["href"]))
        href_list.append(urljoin(url, a_elem["href"]))
    return href_list

list_url_adres =  stahni_list_odkazu(url, selector = "a.tile.scale-anm")
#print(list_url_adres)
#slovnik, pro upravu
#dict_url = {datetime.now().strftime("%m/%d/%Y, %H:%M:%S"): list_url_adres}
#data = pd.DataFrame(dict_url.items())
#data.to_csv("smartprague.csv")










