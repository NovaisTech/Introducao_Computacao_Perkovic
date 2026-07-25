# Problema Prático 4.8

# Escreva a função palavras() que aceita um argumento de entrada
# um nome de arquivo 
# e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.

# >>> palavras('example.txt')

# ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',

#  'the', 'new', 'line', 'character', 'There', 'is', 'a',

#  'blank', 'line', 'above', 'this', 'line']


def palavras(exemple_txt):
    
    # 1. Abre e lê o arquivo
    arquivo = open(exemple_txt, 'r', encoding='utf-8')
    conteudo = arquivo.read()
    arquivo.close()
    
    # 2. Lista de pontuações mencionadas no enunciado
    pontuacao = '!,.:;?'
    
    # 3. Remove os símbolos de pontuação do texto
    for simbolo in pontuacao:
        conteudo = conteudo.replace(simbolo, '')
        
    # 4. Divide o texto limpo em uma lista de palavras
    listaPalavras = conteudo.split()
    
    # 5. Retorna a lista tratada
    return listaPalavras

resultado = palavras('capitulo_04/exercicios/exemple.txt') # arquivo dentro do diretório
print(resultado)