
# Problema Prático 4.4

# Escreva a função par() que toma um inteiro positivo n como entrada
# e exibe na tela todos os números entre 2 (inclusive) e n, 
# que sejam divisíveis por 2 ou por 3, usando este formato de saída:

# >>>par(17)

# 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,

def par(n):
    for i in range(2, n + 1): # para i em um range iniciado por 2 até a definição do valor da função
        if i % 2 == 0 or i % 3 == 0: # calcula se o resto da divisão será zero para 2 e 3
            print(f"{i} -", end=" ")
            
par(100) # definindo o valor da minha função n 