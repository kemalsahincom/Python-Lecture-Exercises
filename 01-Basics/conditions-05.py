"""
Kullanıcıdan 5 sayı isteyin. Bu sayılardan kaç tanesi çift kaç tanesi tek olduğunu bulup ekrana yazdırın. 
"""
ciftAdet = 0
tekAdet = 0
s = input("1.sayıyı isteyin: ")
if(int(s)%2 == 0):
  ciftAdet = ciftAdet + 1 
else:
  tekAdet = tekAdet + 1

s = input("2.sayıyı isteyin: ")
if(int(s)%2 == 0):
  ciftAdet = ciftAdet + 1 
else:
  tekAdet = tekAdet + 1

s = input("3.sayıyı isteyin: ")
if(int(s)%2 == 0):
  ciftAdet = ciftAdet + 1 
else:
  tekAdet = tekAdet + 1

s = input("4.sayıyı isteyin: ")
if(int(s)%2 == 0):
  ciftAdet = ciftAdet + 1 
else:
  tekAdet = tekAdet + 1

s = input("5.sayıyı isteyin: ")
if(int(s)%2 == 0):
  ciftAdet = ciftAdet + 1 
else:
  tekAdet = tekAdet + 1

print("Girilen tek sayıların adeti", tekAdet)
print("Girilen çift sayıların adeti", ciftAdet)

  