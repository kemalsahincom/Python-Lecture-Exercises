cumle = "Güzel günler göreceğiz, güzel günler..."

print(cumle[0])
print(cumle[1])

cumle = cumle.casefold()

kelimeler = cumle.split(" ")

print(kelimeler)

print("Cümledeki güzel kelimesi adeti :", kelimeler.count("güzel"))
print("Cümledeki toplam kelime sayısı :", len(kelimeler))

print(cumle)

cumle = cumle.replace("günler","havalar")

print(cumle)