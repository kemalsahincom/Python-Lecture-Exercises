"""
Kullanıcıdan sayı isteyin. Girilen sayının çift mi tek mi olduğunu bulup ekrana yazdırın. 
"""

sayi = input("sayı giriniz: ")
sonuc = int(sayi) % 2

if (sonuc == 0):
  print("Girdiğiniz sayı çifttir.")
else:
  print("Girdiğiniz sayı tekdir.")


"""
Kullanıcıdan sayı isteyin. Girilen sayının 3 bölünüp bölünmediğini bulup ekrana yazdırınız.
"""