a = int(input("1.sayıyı girin"))
b = int(input("2.sayıyı girin"))
c = int(input("3.sayıyı girin"))


if (a<b and a<c):
  enk = a
elif(b<a and b<c):
  enk = b
else:
  enk = c

if (a>b and a>c):
  enb = a
elif(b>a and b>c):
  enb = b
else:
  enb = c

print("Girilen en büyük sayı", enb)    
print("Girilen en küçük sayı", enk)    





## YÖNTEM - I ##

a = int(input("1.sayıyı girin"))
b = int(input("2.sayıyı girin"))
c = int(input("3.sayıyı girin"))

enb = a
enk = a


if (enb<b):
  enb = b
if (enb<c):
  enb = c  

if(enk>b):
  enk = b  
if(enk>c):
  enk = c

print("Girilen en büyük sayı", enb)    
print("Girilen en küçük sayı", enk)    