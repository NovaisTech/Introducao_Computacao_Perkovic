#======================    Problema Prático 3.2   ==============================
#===============================================================================

# Traduza estas instruções condicionais em instruções if do Python:

# (a) Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
idade = eval(input("Digite sua idade: "))
if idade > 62:
    print("Você pode oter benefícios de pensão")
print("Adeus.")    

# (b) Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.

list = ['Musial', 'Aaraon', 'Williams','Gehrig', 'Ruth']
nome = 'Musial'

if nome in list:
    print("Um dos 5 maiores jogadores de baisebol de todos os tempos! ")


# (c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.

golpes = eval(input("Digite a quantidade de golpes: "))

if golpes > 10:
    print("Você está morto!!")
else:
    print("Ainda estou vivo! ")
print("Bom jogo!")

# (d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.

norte = True
sul = False
leste = False
oeste = False

if norte or sul or leste or oeste == True:
    print("Posso escapar.")
    
    
# ============================   Problema Prático 3.3     ==========================================
# ==================================================================================================
# Traduza estas declarações em instruções if/else do Python:

# (a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'

ano = eval(input("Digite em que ano estamos para saber se é Bissexto: ")) # inpute que pergunta para o usuário digitar que ano ele quer sabe se pode ser bissexto

if ano % 4 == 0:
    print("Pode ser ano bissexto! ")
else:
    print("Definitivamente não é ano bissexto!")

# (b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.

bilhete = [50, 10, 42, 22, 35]
loteria = [10, 22, 35, 42, 50]

# sorted() organiza os números do menor para o maior antes de comparar
if sorted(bilhete) == sorted(loteria):
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez...')
    
    
# =============================   Problema Prático 3.4   ===========================
# ==================================================================================

# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos.
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
# Aqui está um exemplo de um login bem-sucedido:


lista  = ['joe', 'sue', 'hani', 'shopie']
login = input("Digite sua identificação de login: ")

if login in lista:
    print(f"Login: {login}")
    print("Você entrou!")
else:
    print(f"Login: {login}")
    print("Usuário desconhcido")
    
    
# ===========================  Problema Prático 3.5   ===================================
# =======================================================================================
# Implemente um programa que solicite do usuário uma lista de palavras
# (ou seja, strings) e depois exiba na tela, uma por linha, 
# todas as strings de quatro letras nessa lista.


# Digite a lista de palavras:
    
# Solicita a lista de palavras (o usuário deve digitar no formato ['a', 'b'])
lista = eval(input('Digite a lista de palavras: '))

# O laço for percorre cada palavra na lista fornecida
for palavra in lista:
    # A instrução if verifica se o comprimento da palavra é igual a 4
    if len(palavra) == 4:
        # Se for verdadeiro, imprime a palavra
        print(palavra)



nome = input("Digite seu nome :")


print("Palavra soletrada! ")
for char in nome:
    print(char)



animais = ['peixe', 'gato','cão']
for animal in animais:
    print(animal)
print("Fim da lista de animais!")


frase = input("Digite uma frase: ")
for c in frase:
        if c in 'áãéêóôaeiouAEIOU':
            print(c)
            
            
# ===========================   Problema Prático 3.6 ===================================
#=======================================================================================

# Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.

# (a) Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for s in n:
    print(s)



#  (b)Inteiros de 0 a 1 (isto é, 0, 1).

n2 = 0, 1
for i in n2:
    print(i)


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