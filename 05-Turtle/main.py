import turtle 
import random

cumle = "Bugün hava ve araba araba araba çok güzel Tam benlik"
kelime_grubu1 = ["hava","araba"]
kelime_grubu2 = ["çok","güzel"]

cumle = cumle.casefold()
k = cumle.split(" ")

t = turtle.Turtle()

for a in range(0,len(k)):
  if k[a] in kelime_grubu1:
    x = int(random.uniform(-200,200))
    y = int(random.uniform(-200,200))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('red')
    t.circle(10)
    t.end_fill()
  if k[a] in kelime_grubu2:
    x = int(random.uniform(-200,200))
    y = int(random.uniform(-200,200))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('blue')
    for b in range(0,5):
      t.left(144)
      t.forward(50)
    t.end_fill()    

