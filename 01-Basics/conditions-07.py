s1 = input("1.sayıyı girin")
s2 = int(input("2.sayıyı girin"))
islem = input("Yapmak istediğiniz işlemi girin")

s1 = int(s1)
s2 = int(s2)

if (islem == "+"):
  sonuc = s1+s2
elif (islem == "-"):
  if (s1>s2):
    sonuc = s1-s2
  else:
    sonuc = s2-s1
elif (islem == "*"):
  sonuc = s1*s2
elif(islem=="/"):
  if (s1>s2):
    sonuc = s1/s2
  else:
    sonuc = s2/s1
else:
  sonuc = "Bilinmeyen işlem"

print(sonuc)
