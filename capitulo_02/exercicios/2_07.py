# ------------------ Problema Prático 2.7 -------------------------------

# Dada a lista de notas de trabalho de casa dos alunos

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] # escreva:
print(8 in notas)

# (a)Uma expressão que avalia para o número de 7 notas.
print(notas.count(7))  # Retorna o número de ocorrências de item na lista lst

# (b)Uma instrução que muda a última nota para 4.
notas[-1] = 4 
print(notas)

# (c)Uma expressão que avalia para a nota mais alta.
print(max(notas))

# (d)Uma instrução que classifica as notas da lista.
notas.sort() # Classifica a lista
print(notas)

# (e)Uma expressão que avalia para a média das notas.
print(sum(notas) / 9 ) 

# ==============================================================

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
