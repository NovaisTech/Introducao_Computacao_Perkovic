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
    
    
