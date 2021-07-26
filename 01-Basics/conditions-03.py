"""
Kullanıcıdan yaşını isteyin, doğum yılını bulun. 
2000'den sonra doğanlara siz Z kuşağısınız diye mesaj gösterin. 
1980'den sonra doğanlara siz Y kuşağısınız diye mesaj gösterin. 
1980 öncesi doğanlara da siz boomer'sınız diye mesaj gösterin. 

"""

yas = input("yaşınızı girin")
dogumYili = 2021 - int(yas)

print("Doğum yılınız:"+str(dogumYili))

if (dogumYili>1999):
  print("Z kuşağısın.")
elif (dogumYili>1980):
  print("Y kuşağısın.")
else:
  print("Sen boomer'sın.")