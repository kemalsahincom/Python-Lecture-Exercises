"""
Kullanıcıya kaç doları olduğunu sorup güncel kur üzerinden TL değerini ekrana yazdırın. 
"""

import requests
from bs4 import BeautifulSoup


butunSayfa = requests.get("https://www.doviz.com/")

icerik = butunSayfa.text

c = BeautifulSoup(icerik,"html.parser")

kur = c.find_all("span",{"data-socket-key":"USD"})

dolarMiktari = input("kaç dolarınız var: ")
kurAmerikanFormat = kur[0].text
kurAmerikanFormat = kurAmerikanFormat.replace(",",".")

trTutari = float(kurAmerikanFormat) * int(dolarMiktari)

print("Güncel Dolar Kuru",kur[0].text)
print("Dolar miktarınızın TL karşılığı = ", trTutari)





