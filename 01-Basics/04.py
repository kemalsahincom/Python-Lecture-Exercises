"""
Size verilen paragrafda 'A' harfi içeren kelime sayısı bulup ekrana yazdırın. 
"""

cumle = "Nullam ultrices mi a nunc aliquet ultrices. Proin rutrum lectus vel est elementum cursus. Sed sed venenatis massa. Aliquam laoreet pharetra posuere. Phasellus leo mauris, viverra eu lacus imperdiet, facilisis vehicula mauris. Maecenas posuere ipsum id felis luctus, ut rutrum enim pharetra. Praesent euismod commodo neque, auctor molestie purus egestas at. Donec vitae felis dignissim, commodo arcu eu, finibus diam."

cumle = cumle.casefold()
kelimeler = cumle.split(" ")
buldugumKelimeler = []
kelimeSayisi = len(kelimeler)

for a in range(0,kelimeSayisi):
  for b in range(0, len(kelimeler[a])):
    if (kelimeler[a][b] == "a"):
      buldugumKelimeler.append(kelimeler[a])

print(buldugumKelimeler)
