"""
Ahmet Hakan'ın en son yazdığı köşe yazısını metin bulutu olarak görselleştirin.  
"""
import requests
from bs4 import BeautifulSoup
import wordcloud

yazi = requests.get("https://www.hurriyet.com.tr/yazarlar/ahmet-hakan/liyakatsiz-dis-politika-iste-buna-yol-acar-41797544")

bs = BeautifulSoup(yazi.text,"html.parser")

makale = bs.find_all("p")

temiz_makale = ""
for p in makale:
    temiz_makale = temiz_makale + p.text

wc = wordcloud.WordCloud(width=1024,height=1024,background_color="white",stopwords=["bu","bir","ve","da","diye","Ama","çok","ne","de","daha"])
wc.generate(temiz_makale)
wc.to_file("ahmet_hakan01.jpg")
