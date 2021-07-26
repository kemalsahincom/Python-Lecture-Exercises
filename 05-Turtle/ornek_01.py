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

y = 10
for i in range(100,0,-10):
  renk = rgb2hex()
  t.color(renk)
  t.begin_fill()
  t.fillcolor(renk)
  t.circle(i)
  t.end_fill()
  t.penup()
  t.goto(0,y)
  t.pendown()
  y = y + 10