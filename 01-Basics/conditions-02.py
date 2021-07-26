"""
Kullanıcıdan 5 sayı isteyin. Girilen tek sayıların toplamını,
çift sayıların ise ortalamasını bulup ekrana yazdırın. 
"""

toplamCift = 0
ciftAdeti = 0
toplamTek = 0

s1 = input("1.sayıyı giriniz: ")
s2 = input("2.sayıyı giriniz: ")
s3 = input("3.sayıyı giriniz: ")
s4 = input("4.sayıyı giriniz: ")
s5 = input("5.sayıyı giriniz: ")

if ( int(s1)%2 == 0):
  toplamCift = toplamCift + int(s1)
  ciftAdeti = ciftAdeti + 1
else:
  toplamTek = toplamTek + int(s1)

if ( int(s2)%2 == 0):
  toplamCift = toplamCift + int(s2)
  ciftAdeti = ciftAdeti + 1  
else:
  toplamTek = toplamTek + int(s2)

if ( int(s3)%2 == 0):
  toplamCift = toplamCift + int(s3)
  ciftAdeti = ciftAdeti + 1  
else:
  toplamTek = toplamTek + int(s3)

if ( int(s4)%2 == 0):
  toplamCift = toplamCift + int(s4)
  ciftAdeti = ciftAdeti + 1  
else:
  toplamTek = toplamTek + int(s4)

if ( int(s5)%2 == 0):
  toplamCift = toplamCift + int(s5)
  ciftAdeti = ciftAdeti + 1  
else:
  toplamTek = toplamTek + int(s5)

print("Girilen tek sayıların toplamı", toplamTek)
ortalama = toplamCift/ciftAdeti
print("Girilen çift sayıların ortalaması", ortalama)