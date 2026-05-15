# Problema Prático 3.15

# Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos mostrados a seguir. Use a função jump() do módulo ch3. Você conseguirá obter a imagem desenhada executando:

# >>> import turtle

# >>> s = turtle.Screen()

# >>> t = turtle.Turtle()

# >>> olimpíadas(t)

import turtle

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed(5) # velocidade da caneta para desenhar os anéis.
    
def olimpíadas(t):
    # Anéis de cima
    jump(t, -110, 0)
    t.circle(50)
    
    jump(t, 0, 0)
    t.circle(50)
    
    jump(t, 110, 0)
    t.circle(50)
    
    # Anéis de baixo
    jump(t, -55, -50)
    t.circle(50)
    
    jump(t, 55, -50)
    t.circle(50)

# Para rodar:
t = turtle.Turtle()
olimpíadas(t)
turtle.done()