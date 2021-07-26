"""
Paragrafın içerisinde geçen ac,mauris, quis, est kelimelerinin kaç adet
geçtiğini bulup ekrana yazdırın.
Kelime adetlerine göre ekrana iç içe daireler çizin. 
"""

parag = "Phasellus tempor elit quis urna ultricies egestas. Praesent ut luctus est. Curabitur ac ligula interdum, varius felis non, sollicitudin dolor. Proin sit amet nunc eleifend, auctor quam quis, auctor enim. Etiam luctus sem vel tincidunt porta. Etiam malesuada, tellus nec lobortis tristique, neque lectus iaculis arcu, condimentum pretium libero mauris quis est. Nullam ut purus non nisi cursus dapibus. Curabitur cursus sollicitudin felis a maximus. Integer vel consequat sapien. Phasellus condimentum feugiat vestibulum."

from turtle import Screen
import turtle
import random

def rgb2hex():
  r = int(random.uniform(0,255))
  g = int(random.uniform(0,255))
  b = int(random.uniform(0,255))
  return "#{:02x}{:02x}{:02x}".format(r,g,b)

ekran = Screen()
ekran.setup(600,600)
t = turtle.Turtle()

aranacak_kelimeler = ["ac","mauris","quis", "est","elit","nullam","ut"]
noktalama_isaretleri = [".",",",":","?","!"]

yeni_parag = []

adetler = []

parag = parag.casefold()

for harf in parag:
  if harf in noktalama_isaretleri:
    yeni_parag.append("")
  else:
    yeni_parag.append(harf)

yeni_parag = "".join(yeni_parag)    
# print(yeni_parag)

for kelime in aranacak_kelimeler:
  adet = yeni_parag.count(kelime)
  adetler.append(adet)
#  print(kelime, adet)

adetler.sort()
print(aranacak_kelimeler)
print(adetler)

## BÜYÜKTEN KÜÇÜĞE ÇİZİM 
for i in range(len(adetler)-1,0,-1):
  r = rgb2hex()
  t.begin_fill()
  t.fillcolor(r)
  t.circle(adetler[i]*15)
  t.end_fill()

t.penup()
t.goto(120,0)
t.pendown()

## KÜÇÜKTEN BÜYÜĞE ÇİZİM 
for i in range(0,len(adetler)):
  r = rgb2hex()
  t.color(r)
  t.circle(adetler[i]*15)
