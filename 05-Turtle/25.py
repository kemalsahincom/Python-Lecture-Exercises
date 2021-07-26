from turtle import Screen
import turtle

ekran = Screen()

ekran.setup(450,450)

kenar = 400
a = turtle.Turtle()

a.penup()
a.goto(-200,-200)
a.pendown()
for i in range(0,100):
  a.forward(kenar)
  a.left(90)
  kenar = kenar - 4