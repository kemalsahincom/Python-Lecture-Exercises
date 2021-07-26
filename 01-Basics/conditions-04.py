"""
Kullanıcıdan 5 sayı isteyin. 
Bu sayılardan kaçı 3e, kaç tanesi 5e, kaç tanesi de 7e bölünebildiğini 
bulup adetini ekrana yazdırın. 
"""
ucAdet = 0
besAdet = 0
yediAdet = 0

s = input("1.Sayıyı giriniz:")
if (int(s) % 3 == 0):
  ucAdet = ucAdet + 1
elif (int(s) % 5 == 0):
  besAdet = besAdet + 1 
elif (int(s) % 7 == 0):
  yediAdet = yediAdet + 1

s = input("2.Sayıyı giriniz:")
if (int(s) % 3 == 0):
  ucAdet = ucAdet + 1
elif (int(s) % 5 == 0):
  besAdet = besAdet + 1 
elif (int(s) % 7 == 0):
  yediAdet = yediAdet + 1

s = input("3.Sayıyı giriniz:")
if (int(s) % 3 == 0):
  ucAdet = ucAdet + 1
elif (int(s) % 5 == 0):
  besAdet = besAdet + 1 
elif (int(s) % 7 == 0):
  yediAdet = yediAdet + 1    

s = input("4.Sayıyı giriniz:")
if (int(s) % 3 == 0):
  ucAdet = ucAdet + 1
elif (int(s) % 5 == 0):
  besAdet = besAdet + 1 
elif (int(s) % 7 == 0):
  yediAdet = yediAdet + 1      

s = input("5.Sayıyı giriniz:")
if (int(s) % 3 == 0):
  ucAdet = ucAdet + 1
elif (int(s) % 5 == 0):
  besAdet = besAdet + 1 
elif (int(s) % 7 == 0):
  yediAdet = yediAdet + 1      

print("Girilen sayılardan üçe bölünebilenlerin adeti", ucAdet)
print("Girilen sayılardan beş bölünebilenlerin adeti", besAdet)
print("Girilen sayılardan yedi bölünebilenlerin adeti", yediAdet)