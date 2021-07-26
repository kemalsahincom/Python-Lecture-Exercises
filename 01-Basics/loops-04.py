"""
Kullanıcıdan bir cümle isteyin. Kullanıcının girdiği cümledeki
a harfini yıldıza çevirip yeni oluşan cümleyi ekrana yazdırın. 
"""

cumle = input("Bir cümle giriniz : ")

i=0
yeni_cumle = ""
while(i<len(cumle)):
  if (cumle[i] == "a" or cumle[i] == "A"):
    yeni_cumle = yeni_cumle + "*"
  else:
    yeni_cumle = yeni_cumle  + cumle[i]
  i=i+1

print(yeni_cumle)