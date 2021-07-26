"""
Programın içerisindeki cümledeki boşluk sayısını bulup ekrana yazdırın. 
"""

cumle = "Bugün hava kapalı biraz belki yağmur yapabilir."

i=0
bosluk=0
print(len(cumle))
while (i<len(cumle)):
  if(cumle[i]==" "):
    bosluk=bosluk+1
  i=i+1
print("Cümledeki boşluk adeti"+ str(bosluk))