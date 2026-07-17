
# Exercícios de Funções em Python - Nível Iniciante

# Instruções:
# Resolva cada exercício preenchendo o corpo da função.
# Para testar, basta executar o arquivo no VS Code.



# 1. Crie uma função chamada 'saudar' que retorne a frase "Olá, Mundo!"
def saudar():
    print("Olá, mundo!")
saudar()   

# 2. Crie uma função chamada 'dobro' que receba um número e retorne o dobro dele.
def dobro(n):
    dobrado = n + n
    print(dobrado)

dobro(50)

# 3. Crie uma função 'soma' que receba dois números e retorne a soma deles.
# def soma(n1, n2):
def soma(n1, n2):
    resultado = n1 + n1
    print(resultado)
soma(14 , 15)    



# 4. Crie uma função 'area_retangulo' que receba base e altura e retorne a área.
# Seudef area_retangulo(base, altura):
def area_retangulo(base, altura):
    area = base * altura /2
    print(area)
area_retangulo(3 , 5)    


# 5. Crie uma função 'e_par' que receba um número e retorne True se for par e False se for ímpar.
def even(n):
    if n % 2 == 0:
        print("É par")
    else:
        print("não é par!") 
even(10)           



# 6. Crie uma função 'maior_numero' que receba dois números e retorne o maior deles.
def maiorNumero(a, b):
    if a > b:
        print(f" o número {a} é maior que {b}")
    else:
        print(f"O núemro {b} é maior que {a}")
maiorNumero(23, 5)     


       
# 7. Crie uma função 'contar_letras' que receba uma palavra e retorne a quantidade de caracteres dela.
def contar_letras(palavra):
    print(len(palavra))
    
contar_letras("Paralelepipedo")        


# 8. Crie uma função 'converter_celsius' que receba uma temperatura em Celsius e retorne em Fahrenheit.
# Dica: (C * 9/5) + 32
def conversor_temperatura(tempC):
    fahrenheit = ((tempC * 9 ) / 5 ) + 32
    print(f"A temperatura em {tempC} convertida para é igual: ", fahrenheit)
conversor_temperatura(18)    


# 9. Crie uma função 'saudacao_personalizada' que receba um nome e retorne "Olá, [nome]! Seja bem-vindo."
def saudacao_personalizada(nome):
    print(f"Olá, {nome} seja bem-vindo")
saudacao_personalizada("Fábio")    
  
  
    
# 10. Crie uma função 'calcular_desconto' que receba o valor de um produto e a porcentagem de desconto.
# A função deve retornar o valor final com o desconto aplicado.  
def calcular_desconto(valor_produto):
       desconto = valor_produto * 0.9
       print(f"O valor do produto com desconto de 10 % é igual {desconto}")
calcular_desconto(59)       