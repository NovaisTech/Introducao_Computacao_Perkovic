# 2.4 Objetos e Classes:
# Aborda a teoria por trás do Python, onde "tudo é um objeto".
# Os exercícios começam a introduzir o conceito de métodos (funções que pertencem a um objeto).
# -------------------------------------------//-------------------------------------------------#


# Dada a lista de nomes 
s = ['Sara', 'Chen', 'Jake', 'Anne']
#escreva expressões para:

# Verificar se 'Jake' está na lista.
print('Jake' in s)
# Adicionar 'Tariq' ao final da lista.
s.append('Tariq')
print(s)

# Encontrar o índice de 'Chen'.
print(s[1])

# Remover o primeiro elemento.
s.remove('Sara')
print(s)


# ======================  Problema Prático 2.8  ====================================

# Em que ordem os operadores nas expressões a seguir são avaliados?
# A ordem é indicada por meio de parênteses:

# (a) 2 + 3 == 4 or a >= 5

a =2
print((2 + 3) == 4) or (a >= 5) # defini um valor para 'a' pra não gerar erro

# (b) lst[1] * -3 < -10 == 0

lst = [1 , 2, 3]
print(((lst[1]) * (-3)) < (-10 ))== 0

# (c) (lst[1] * -3 < -10) in [0, True]

print(((lst[1]) * (-3)) < (-10)) in [0, True]
# (d) 2 * 3**2
print(2 * (3**2))

# (e) 4 / 2 in [1, 2, 3]
print((4 / 2) in ([1, 2, 3]))


# -------------------------- Problema Prático 2.9 ---------------------------------

#  Qual é o tipo do objeto ao qual essas expressões são avaliadas?

# (a)False + False
print(False + False) # tipo int retorno 0 


# (b)2 * 3**2.0
print(2 * 3**2.0) # tipo float  retorno 18.0 


# (c)4 // 2 + 4 % 22 
print(4 // 2 + 4 % 22) # tipo Int retorno 6


# (d)2 + 3 == 4 or 5 >= 5
print(2 + 3 == 4 or 5 >= 5) # tipo boolean retorno True