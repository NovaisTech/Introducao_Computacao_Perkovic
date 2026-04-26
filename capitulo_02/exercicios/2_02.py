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




