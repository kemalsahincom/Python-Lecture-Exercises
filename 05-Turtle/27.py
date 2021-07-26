import turtle

def rgb2hex(r,g,b):
  return "#{:02x}{:02x}{:02x}".format(r,g,b)

a = turtle.Turtle()

renk = rgb2hex(255,160,0)

turtle.Screen().bgcolor(renk)
a.color("red")
a.pensize(5)

a.begin_fill()
a.fillcolor("yellow")
for i in range(0,5):
  a.left(144)
  a.forward(100)
a.end_fill()
