"""
Rastgele 10 tane sayı üretin. 
Bu sayılardan hareket ile 10 tane farklı konumlarda 
daireler ekrana çizdirin. 
"""
import random
import turtle
from turtle import Screen

ekran = Screen()
ekran.setup(150,150)

daireCaplari = []
t = turtle.Turtle()

for a in range(0,10):
  daireCaplari.append(int(random.uniform(20,50)))

print(daireCaplari)

for a in range(0,10):
  t.penup()
  x = random.uniform(-150,150)
  y = random.uniform(-150,150)
  t.goto(x,y)
  t.pendown()
  t.circle(daireCaplari[a])
  t.penup()
  t.goto(x,y+10)
  t.pendown()
  t.circle(daireCaplari[a]-10)