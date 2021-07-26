"""
rastgele 10 sayı üretin. 
Kullanıcıdan bir sayı isteyin. 
Kullanıcının girdiği sayıdan 
büyük olanların adetini ve sayıları ekrana yazdırın. 
Küçük olanların adetini ve sayılarını ekrana yazdırın. 
"""

import random 

kume = []
buyukSayilar = []

for b in range(0,10):
  a = int(random.uniform(0,100))
  kume.append(a)
print(kume)
adet = 0
sayi = input("Sayı girin")
for b in range(0,10):
  if (int(sayi) < kume[b]):
    adet = adet + 1
    buyukSayilar.append(kume[b])

print("Girdiğiniz sayıdan büyük rastgele sayı adeti = ",adet)
print("Girdiğiniz sayıdan büyük sayılar", buyukSayilar)
