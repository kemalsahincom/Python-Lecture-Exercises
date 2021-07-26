from turtle import Screen
import turtle
ekran=Screen()
ekran.setup(500,500)
t = turtle.Turtle()
t.color("purple")


# YÖNTEM - 2 

for a in range(0,2):
  for b in range(0,5):
    t.left(144)
    t.forward(100)
  t.penup()
  t.goto(0,30)
  t.left(30)
  t.pendown()


t.penup()
t.goto(100,100)
t.pendown()
t.color("blue")

# YÖNTEM - 1


for a in range(0,25):
  t.left(150)
  t.forward(100)
