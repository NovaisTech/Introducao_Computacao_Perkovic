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
    
    
