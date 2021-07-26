cumle = "ISIK UNIVERSITESI"

cumle = cumle.casefold()

kelimeler = cumle.split(" ")

print(kelimeler)

for a in range(0,len(kelimeler)):
  for b in range(0,len(kelimeler[a])):
    print(kelimeler[a][b])