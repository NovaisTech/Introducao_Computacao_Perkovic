# Implemente a função rol(), que recebe uma lista contendo informações de estudantes e
# exibe um rol, como vemos a seguir. As informações do estudante, 
# consistindo em seu sobrenome, nome, nível e nota média, 
# serão armazenadas nessa ordem em uma lista.
# Portanto, a lista de entrada é uma lista de listas. 
# Cuide para que o rol exibido tenha 10 espaços para cada valor de string e 
# 8 para a nota, incluindo 2 espaços para a parte decimal.


def rol(estudantes):
    print("Último   Primeiro    Classe     Nota Média \n") # menu da grade estudantes
   
    for estudante in estudantes:   #iteração dentro da lista principal de estudantes
        print("{:10}{:10}{:10}{:8.2f}".format(estudante[0], estudante[1], estudante[2], estudante[3])) #Formata e imprime as informações dos estudantes
        

estudantes = [] # lista vazia
estudantes.append(['DeMoines', 'Jim', 'Pleno', 3.45]) # adiconando dados a lista
estudantes.append(['Pierre','Sophie', 'Pleno', 4.0])
estudantes.append(['Columbus', 'Maria', 'Sênior', 2.5])
estudantes.append(['Phoenix', 'River','Júnior', 2.45])
estudantes.append(['Olympis', 'Edgar', 'Júnior', 3.99])

rol(estudantes) # chamado da função 