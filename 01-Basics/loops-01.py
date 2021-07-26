"""
Kullanıcı N harfine basana kadar sayı isteyin. Girilen sayıların toplamını ve adetini ekrana yazdırın.
"""
toplam = 0
adet = 0
s = input("Sayı giriniz:")
while (s != "n" and s !="N"):
  toplam = toplam + int(s)
  adet = adet + 1
  s = input("Sayı giriniz:")


print("girilen sayıların toplamı",toplam)
print("girilen sayıların adeti",adet)

"""
Kullanıcı N harfine basana kadar sayı isteyin. Girilen sayıların çift ve tek adetlerini ekrana yazın. 
"""
