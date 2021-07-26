import requests
from bs4 import BeautifulSoup

x = requests.get('https://bigumigu.com/', headers={"User-Agent":"kemal-Chrome"})

icerik = x.content

c = BeautifulSoup(icerik,"html.parser")
data = c.find_all("h1",{"class":"entry-title"})

i=1
for a in data:
  print(str(i)+". "+a.text)
  i=i+1


