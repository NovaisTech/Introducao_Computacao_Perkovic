# Problema Prático 3.13

# Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista original for:

# >>> time = ['Ava', 'Eleanor', 'Clare', 'Sarah']

# então a lista resultante deverá ser:

# >>> time

# ['Sarah', 'Eleanor', 'Clare', 'Ava']

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
print(time)
print('=='*50)

time[0], time[-1] = time[-1], time[0] # atribuição multipla, troca de valores 
print(time)
print('=='*50)

# time = time[-1], time[1], time[2], time[0] 
# print(time)
# print('=='*50)