import turtle 
import time

# Agora que o arquivo não se chama mais turtle.py, 
# o 'import turtle' vai buscar a biblioteca correta do Python.

s = turtle.Screen() 
t = turtle.Turtle() 
u = turtle.Turtle()
r = turtle.Turtle()

s.bgcolor("Blue")
t.color("yellow")
u.color("gray")
r.color("white")

t.forward(100)  
t.left(45)
t.forward(100)       # métodos que dão direção as canetas u e 
t.right(90)
t.forward(100)

u.forward(-100)
u.right(45)
u.forward(-100)
u.left(90)
u.forward(-100)

r.goto(0,-180)
r.circle(150)

# -----  Desenhando uma face sorridente com a tartaruga --------

l = turtle.Turtle()
l.pensize(3)

x = -120    # definindo as coordenadas iniciais de x e y.
y = 120
# l.goto(x,y)
# l.undo() 

l.penup()
l.goto(x, y)
l.pendown()
l.circle(100)

l.penup()
l.goto(x - 35, y + 120)
l.pendown()
l.dot(25)

l.penup()
l.goto(x + 35, y + 120)
l.pendown()
l.dot(25)

l.penup()
l.goto(x - 60.62, y+ 65)
l.pendown()
l.setheading(-60)
l.circle(70, 120)


time.sleep(2)
s.clear()