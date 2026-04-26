# 2.5 Biblioteca Padrão Python:
# Apresenta módulos embutidos que expandem as capacidades da linguagem sem precisar instalar nada extra.
# -------------------------------------------//-------------------------------------------------#

# =========================   Problema Prático 2.10   =========================================
# Escreva expressões Python correspondentes ao seguinte:
import math

# (a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
# Hipotenusa igual raiz quadrada da soma dos catetos elevados ao quadrado.
c1 = int(input("Digite o valor do primeiro cateteos:"))
c2 = int(input("Digite o valor do segundo cateto:"))

h = (c1 ** 2 + c2 ** 2)**0.5   
print(h)
# -------   0.5 elevar um número a potência 1/5 (ou 0.5)é o mesmo que tirar sua raiz quadrada ---
print(144**0.5)


# (b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
resultado_expressao = (h == 5)

print(f"O valor da expressão é igual a 5? {resultado_expressao}")

# (c)A área de um disco com raio a
# fórmula de cálculo do Círculo (A = π * r²)

raio = float(input("Digite o valor do raio"))
pi = 3.1415
area = pi * (raio)**2

print(f"O valor da área é:{area:.2f} cm²")

# (d)  O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro (a, b) e raio r
x = float(input("digite as coordenadas de x:"))
y = float(input("digite as coordenadas de Y:"))

a = float(input("Digite as coordenadas de a e b:"))
b = float(input("Digite as coordenadas de a e b:"))

r = float(input("Digite o valor do Raio: "))

dentroCirculo = (x - a)**2 + (y - b)**2 <= (r**2)
print(f"O ponto de ({x}, {y}) está dentro do círculo {dentroCirculo}")

print(math.pi) 

print(math.e)

# ----------------- Módulo fractions -----------------------------

# O tipo Fraction é usado para representar frações e realizar aritmética racional
import fractions

a = fractions.Fraction(3,4)
b = fractions.Fraction(1,2)

c = a * b
d = a + b
e = a - b

print(c,d,e)