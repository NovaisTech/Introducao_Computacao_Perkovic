#====================== Problema Prático 3.8  ============================

# Defina, diretamente no shell interativo, a função média(),
# que aceita dois números como entrada e retorna a média dos números. 
# Um exemplo de uso é:

def media(a, b):
    return(a + b) / 2

resultado = media(2, 3.5)
print(f"A média {resultado}")
# >>> average(2, 3.5)
# 2.75


# ====================  Problema Prático 3.9  =====================

# Implemente a função perímetro(), que aceita, como entrada,# o raio de um círculo (um número não negativo) 
# e retorna o perímetro do círculo. # Você deverá escrever sua implementação em um módulo chamado perímetro.py.
# Um exemplo de uso é:

# >>> perimeter(1)
# 6.283185307179586
import math  # aqui está sendo usado a biblioteca math pra cálculo mais preciso
def perimetro(r):
    return(2 * math.pi * r)

perCirculo = perimetro(10)
print(f"O perímetro da circuferência é {perCirculo:.2f}")