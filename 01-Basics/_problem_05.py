"""
Kullanıcı adını ve soyadını girsin. 
Adı kaç harften oluştuğunu bulup ekrana yazdırın. Soyadını ekrana yazdırın. Kullanıcının ad ve soyadında geçen A ve E harfi saysını ekrana yazdırın. A ve E harfi dışında kaç tane harf olduğu ekrana yazdırın. 

"""

isimSoyisim = input("Adınızı soyadınızı giriniz:")

h = 0
aHarfiSayisi = 0
eHarfiSayisi = 0
A_e_haricHarfler = 0
sesliHarf = 0

while (h<len(isimSoyisim)):
  if (isimSoyisim[h] == " "):
    boslukKarakteriNo = h
  elif (isimSoyisim[h] == "a" or isimSoyisim[h] == "A" ):
    aHarfiSayisi = aHarfiSayisi + 1
  elif (isimSoyisim[h] == "e" or isimSoyisim[h] == "E"):
    eHarfiSayisi = eHarfiSayisi + 1
  else:
    A_e_haricHarfler = A_e_haricHarfler + 1

  h = h + 1

if (aHarfiSayisi>0):
  sesliHarf = sesliHarf + 1  
if (eHarfiSayisi>0):
  sesliHarf = sesliHarf + 1    
  
isim = ""
h=0
while(h<boslukKarakteriNo):
  isim = isim + isimSoyisim[h] 
  h = h + 1

soyisim = ""
h = boslukKarakteriNo + 1
while(h<len(isimSoyisim)):
  soyisim = soyisim + isimSoyisim[h]
  h = h +1

print(isim)
print(soyisim)
print("A harfi sayısı", aHarfiSayisi)
print("E harfi sayısı", eHarfiSayisi)
print("A ve E hariç harfi sayısı", A_e_haricHarfler)
print("Farklı sesli harf sayısı", sesliHarf)