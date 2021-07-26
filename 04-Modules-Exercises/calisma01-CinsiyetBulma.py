"""
Kullanıcıya adını sorun. 
Cinsiyetini bulup göre hanım veya bey olarak selamlayın. 

"""
import urllib.request
import json 
name = input("Adınızı yazınız :")
name = name.lower()
name = name.replace('ş','s')
name = name.replace('ö','o')
name = name.replace('ü','u')
name = name.replace('i','i')

url = "https://gender-api.com/get?name="+name+"&"
key = "key=caRePpPTUqCLaQCsYt&locale=tr_TR"

url = url + key


x = urllib.request.urlopen(url)

gelen = x.read()
sonuc = json.loads(gelen);

if (sonuc["accuracy"]>90):
    if (sonuc["gender"] == "male"):
        print("Merhaba, "+name+" Bey")
    elif (sonuc["gender"] == "female"):
        print("Merhaba, "+name+" Hanım")        
