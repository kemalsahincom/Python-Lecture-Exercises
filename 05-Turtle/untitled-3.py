import turtle 

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

t = turtle.Turtle()

turtle.screensize(400,400)
t.pensize(3)
t.penup()
t.goto(0,-200)
t.pendown()
renk = 0
for i in range(200,0,-10):
  t.pencolor(rgb2hex(i,0,0))
  t.fillcolor(rgb2hex(renk,renk,renk))
  t.begin_fill()
  t.circle(i)
  t.end_fill()  
  t.penup()
  t.goto(0,i*-1+10)
  t.pendown()  
  renk = renk + 10