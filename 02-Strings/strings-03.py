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

for a in range(0,10):
  r = rgb2hex()
  t.color(r)
  t.forward(30)