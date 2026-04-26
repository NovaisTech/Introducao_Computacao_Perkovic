# ------------------------2.1 Expressões, Variáveis e Atribuições----------------------------------#

# Foca na sintaxe de operadores matemáticos e na criação de variáveis para armazenar resultados.
# Os exercícios buscam fixar a precedência de operadores e o uso do sinal de igual (=) para atribuição.
# -------------------------------------------//-------------------------------------------------#

#  Escreva expressões algébricas em Python que correspondam ao seguinte:

# A soma dos 5 primeiros números inteiros positivos.
print(1+2+3+4+5)
print("*********************************************************************")

# A idade média de três pessoas (ex: 23, 19 e 31).
mediaIdade = (23 + 19 + 31) /3
print(mediaIdade)
print("*********************************************************************")

# O número de vezes que 73 cabe em 403.
print("Para saber quantas vezes o npumero 73 cabe em 403 ")
print("O 73 cabe", 403 // 73, " vezes em 403")
print("*********************************************************************")

# O resto da divisão de 403 por 73.

print("O resto da divisão de 403 por 73 é calculado usando o operador de %, e será iagual a:", 403 % 73)
print("*********************************************************************")
# 2 elevado à 10ª potência.

print(2**10)
print("*********************************************************************")

# O valor absoluto da diferença entre a altura de duas pessoas (ex: 54 e 57).
# nesse caso pra encontra o valor absoluto precisamos usa a função abs() 

print("O valor absoluto entre a diferença de 54 - 57 é igaul a ", abs(54 - 57))
print("*********************************************************************")


# O menor preço entre uma lista de valores (ex: 34.99, 29.95 e 31.50).
#aqui é definido uma variável lista com os valores e usado a função min(valores) que verifica dentro da lista qual menor valor

valores = [34.99, 29.95, 31.50]
print(min(valores))
print("*********************************************************************")




