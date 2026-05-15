# t.penup()

# t.goto(x, y)

# t.pendown()

# Essa sequência de chamadas do método Turtle foi usada para mover o objeto Turtle t (com coordenadas (x, y)) sem deixar um rastro;
# em outras palavras, ela foi usada para fazer o objeto Turtle saltar para um novo local.

# Gastaríamos muito menos digitação se pudéssemos substituir essa sequência de instruções Python por apenas uma. 
# É exatamente para isso que servem as funções.
# O que queremos fazer é desenvolver uma função que tome um objeto Turtle e coordenadas x e y como argumentos de entrada e faça o objeto Turtle saltar para a coordenada (x, y).
# Aqui está essa função:

#def jump(t,x, y):

# 2 'faz tartaruga saltar para coordenadas (x, y)'
# 3
# 4 t.penup()
# 5 t.goto(x,y)
# 6 t.pendown()

import turtle 

s = turtle.Screen()
t = turtle.Turtle()
t.speed(7) # Aumenta um pouco a velocidade para desenhar as duas rápido

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def emoticon(t, x, y):
    # Definindo as configurações de desenho
    t.pensize(3)
    t.setheading(0)
    
    # Rosto
    jump(t, x, y)
    t.circle(100)
    
    # Olho Esquerdo
    jump(t, x - 40, y + 120)
    t.dot(25)
    
    # Olho Direito
    jump(t, x + 40, y + 120)
    t.dot(25)
    
    # Boca (Sorriso)
    jump(t, x - 60, y + 65)
    t.setheading(-60)
    t.circle(70, 120)

# --- CHAMADAS DAS FUNÇÕES (FORA DA DEF) ---

# Primeira carinha na posição original (centro)
emoticon(t, -150, 0)

# Segunda carinha em outra posição (mais à direita)
emoticon(t, 150, 0)

# Mantém a janela aberta
s.exitonclick()