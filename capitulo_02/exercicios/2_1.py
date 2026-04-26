# ------------------------2.1 Expressões, Variáveis e Atribuições----------------------------------#

# Foca na sintaxe de operadores matemáticos e na criação de variáveis para armazenar resultados.
# Os exercícios buscam fixar a precedência de operadores e o uso do sinal de igual (=) para atribuição.
# -------------------------------------------//-------------------------------------------------#

#  Escreva expressões algébricas em Python que correspondam ao seguinte:

# A soma dos 5 primeiros números inteiros positivos.
print(1+2+3+4+5)
print("*********************************************************************")

# A idade média de três pessoas (ex: 23, 19 e 31).
mediaIdade = (23 + 19 + 31) /6
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

valores = 34.99, 29.95, 31.50
print(min(valores))
print("*********************************************************************")


#========================================================================================================

# -----------------------Problema Prático 2.2------------------------------#

#Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

# A soma de 2 e 2 é menor que 4.
soma = 2 + 2 
print(f"A soma de 2 e 2 é menor que 4",soma > 4)
print("*********************************************************************")

# O valor de 7 // 3 é igual a 1 + 1.
   # Nesse problema quer saber se a quantidade de vezes que o número 3 cabe no 7 será igual a soma 1 + 1

print("A quantidade de vezes que o número 3 cabe no é igual a 1 + 1",7//3 == 1 + 1)
print("*********************************************************************")

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
soma_Quadrado = 3 **2 + 4 ** 2

if soma_Quadrado == 25:
    print("A soma de 3² + 4² é igual a 25") 
else:
    print("Os valores são")    
print("*********************************************************************")
# A soma de 2, 4 e 6 é maior que 12.

numeros = 2, 4, 6
print("A soma dos núumeros 2,4 e 6 é maiors que 12", sum(numeros) > 12)
if sum(numeros) > 12:
    print(" soma maior que 12")
elif sum(numeros) == 12:
    print("Os valores são iguais!")
else:
    print("A soma é menor que 12")        
print("*********************************************************************")

# 1387 é divisível por 19.

n_divisivel = 1387 / 19
print("Divisão de 1387 por 19 =",n_divisivel)



print("*********************************************************************")
# 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)

print(31 % 2 == 0) 


print("*********************************************************************")
# O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*

lista_precos = [34.99, 29.95, 31.50]
print("Saber se o menor número da lista de preços é menor que R$30 )", min(lista_precos) < 30.00)

print("*********************************************************************")

#===========================================================================================================
#---------------------------------Problema Prático 2.3---------------------------------#

#screva instruções Python que correspondem às ações a seguir e execute-as:
# Atribuir o valor inteiro 3 à variável a.

a = 3
print(a)
print("*********************************************************************")
# Atribuir o valor 4 à variável b.

b = 4
print(b)
print("*********************************************************************")

# Atribuir à variável c o valor da expressão a * a + b * b.
c = (a * a) + (b * b)
# print((a * a) + (b * b))
print(c)
print("*********************************************************************")