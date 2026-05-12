# Problema Prático 3.12

# Desenhe um diagrama representando o estado dos nomes e objetos após esta execução:

# >>> a = [5, 6, 7]

# >>> b = a

# >>> a = 3
"""
a -> referencia ao objeto tipo lista 
b -> referencia ao mesmo objeto que a
a -> é reatribuído, ele deixa de apontar para a lista e aponta para 3

print(__doc__) exibe esses informações acima ↑↑↑
"""
a = [5, 6, 7]  
b = a   
a = 3   
 
print(a)
print(b)

print(__doc__) # exibe as informações da Docstring quando o programa é executado