import turtle

t = turtle.Turtle()

kenar = 5
uzaklasma = 2

for j in range(0,15):
  for i in range(0,4):
    t.forward(kenar)
    t.left(90)
  t.penup()
  t.goto(0,uzaklasma)
  t.left(30)
  t.pendown()
  uzaklasma = uzaklasma + 2
  kenar = kenar + 5
