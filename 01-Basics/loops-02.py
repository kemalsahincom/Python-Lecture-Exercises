s=input("Sayı giriniz:")
cift=0
tek=0

while (s != "n" and s != "N"):
  if int(s)%2==0:
    cift=cift+1
  else:
    tek=tek+1
  s=input("Sayı giriniz:")

print(str(cift))
print(str(tek))