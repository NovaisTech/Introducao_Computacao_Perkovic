# ============================  Problema Prático 3.7  ===================================
#========================================================================================

# Escreva um laço for que exiba a seguinte sequência de números, um por linha.

# (a)Inteiros de 3 até 12, inclusive este.

a = [3, 4 , 5, 6, 7, 8, 9, 10, 11, 12]
for i in a:
    print(i)

# (b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).

for i in range(0,9,2):
    
    print(i)


# (c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.

for i in range(0,24,3):
    print(i)


# (d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.

for r in range(3,12,5):
    print(r)