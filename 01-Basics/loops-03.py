"""
Kullanıcının girdiği cümledeki boşluk adetini bulup ekrana yazdırın. 
Kullanıcının girdiği cümledeki nokta adetini bulup ekrana yazdırın. 
Kullanıcının girdiği cümledeki a harfi ve e harfi adetini bulup ekrana yazdırın. 
"""

cumle = input("Bir cümle girin")
i=0
bosluk = 0
nokta = 0
aHarfi = 0
eHarfi = 0
while(i<len(cumle)):
  if (cumle[i] == " "):
    bosluk = bosluk +1 
  if (cumle[i] == "."):
    nokta = nokta + 1
  if (cumle[i] == "a" or cumle[i] == "A"):
    aHarfi = aHarfi + 1
  if (cumle[i] == "e" or cumle[i] == "E"):
    eHarfi = eHarfi + 1  
  i=i+1
print("Boşluk adeti", bosluk)
print("Nokta adeti", nokta)
print("A Harfi adeti", aHarfi)
print("E Harfi adeti", eHarfi)
