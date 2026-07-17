
# # Exercícios de Funções em Python - Nível Iniciante

# # Instruções:
# # Resolva cada exercício preenchendo o corpo da função.
# # Para testar, basta executar o arquivo no VS Code.



# 1. Crie uma função chamada 'saudar' que retorne a frase "Olá, Mundo!"
def saudar():
    return "Olá, mundo!"

print(saudar()) 

# 2. Crie uma função chamada 'dobro' que receba um número e retorne o dobro dele.
def dobro(n):
    return n + n
   
print(dobro(50))

# 3. Crie uma função 'soma' que receba dois números e retorne a soma deles.
def soma(n1, n2):
    return n1 + n2
   
print(soma(14 , 15))    



# 4. Crie uma função 'area_retangulo' que receba base e altura e retorne a área.
# Seudef area_retangulo(base, altura):
def area_retangulo(base, altura):
    return base * altura /2

print(area_retangulo(3 , 5))



# # 5. Crie uma função 'e_par' que receba um número e retorne True se for par e False se for ímpar.
def even(n):
    if n % 2 == 0:
        return "É par!"
    
    return "não é par!" # dispensa uso do Else, mas precisa manter a indentação 
print(even(101))         



# # 6. Crie uma função 'maior_numero' que receba dois números e retorne o maior deles.
def maiorNumero(a, b):
    if a > b:
        return f" o número {a} é maior que {b}"
    
    return    f"O núemro {b} é maior que {a}"
print(maiorNumero(23, 5))     


       
# # 7. Crie uma função 'contar_letras' que receba uma palavra e retorne a quantidade de caracteres dela.
def contar_letras(palavra):
    return len(palavra)
    
print(contar_letras("Paralelepipedo"))        


# # 8. Crie uma função 'converter_celsius' que receba uma temperatura em Celsius e retorne em Fahrenheit.
# # Dica: (C * 9/5) + 32
def conversor_temperatura(tempC):
    fahrenheit = ((tempC * 9 ) / 5 ) + 32
    
    return f"A temperatura em {tempC} convertida para fahrenheit é igual: {fahrenheit} "
    # return f"A temperatura em {tempC} convertida para fahrenheit é {((tempC * 9 ) / 5 ) + 32}"
print(conversor_temperatura(18))    


# # 9. Crie uma função 'saudacao_personalizada' que receba um nome e retorne "Olá, [nome]! Seja bem-vindo."
def saudacao_personalizada(nome):
    return f"Olá, {nome} seja bem-vindo"

print(saudacao_personalizada("Fábio"))    
  
  
    
# # 10. Crie uma função 'calcular_desconto' que receba o valor de um produto e a porcentagem de desconto.
# # A função deve retornar o valor final com o desconto aplicado.  
def calcular_desconto(valor_produto):
       desconto = valor_produto * 0.9
       return f"O valor do produto com desconto de 10 % é igual {desconto}"
print(calcular_desconto(59))       