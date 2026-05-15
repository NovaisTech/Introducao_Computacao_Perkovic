# Problema Prático 3.14

# Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.

# >>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

# >>> trocaPU(ingredientes)

# >>> ingredientes

# ['maçãs', 'açúcar', 'manteiga', 'farinha']


def trocaPU(lista): # identificamos o índice e fazemos a troca simutânea 
    lista[0], lista[-1] = lista[-1], lista[0]


ingredientes = ['farinha',' açucar', 'manteiga', 'maçãs'] #nossa lista

trocaPU(ingredientes) # Chama a função pra executar a troca simultânea
print(ingredientes) # Imprime resultado


# Outro exemplo com a mesma função
itens = ['casa', 'masão', 'barraco', 'hotel']

trocaPU(itens)
print(itens)