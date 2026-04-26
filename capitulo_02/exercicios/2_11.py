import turtle 
import time

# ========================  Problema Prático 2.11 ==================================
# Comece executando estas instruções:

r = turtle.Screen()
r.bgcolor("yellow")
t = turtle.Turtle(shape="turtle")
t.pensize(3)
t.penup()
t.goto(-300, 90)
t.pendown()
t.circle(100)
t.penup()
t.goto(-350,-250 )
t.pendown()
t.setheading(-60)
t.circle(90, 120)
t.setheading(-60)
t.circle(90, 120)
t.setheading(-60)
t.circle(90, 120)
t.setheading(-60)
t.circle(90, 120)
t.setheading(-60)
t.circle(90, 120)
t.penup()
t.goto(-100,-350)
turtle.exitonclick()   