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
            