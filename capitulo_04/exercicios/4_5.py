# Problema Prático 4.5

# Suponha que as variáveis primeiro, último, rua, número, cidade, estado, codPostal
# já tenham sido atribuídas. 
# Escreva uma instrução print que crie uma etiqueta de correspondência:

# John Doe

# 123 Main Street

# AnyCity, AS 09876

# supondo que:

primeiro = 'John' #{0}
último = 'Doe' #{1}
rua = 'Main Street' #{2}
número = 123  #{3}
cidade = 'AnyCity'  #{4}
estado = 'AS'   #{5}
codPostal = '09876'  #{6}

print('{0} {1}\n{3} {2}\n{4}, {5} {6}'.format(primeiro, último,rua, número, cidade, estado, codPostal))
  
  
objeto = 'Fone'

print('{}'.format(objeto))