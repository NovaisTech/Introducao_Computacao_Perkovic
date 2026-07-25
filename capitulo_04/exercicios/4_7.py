# ============================================# Problema Prático 4.7============================

# Escreva a função stringCount() que aceita duas entradas de string 
# — um nome de arquivo e uma string de alvo — e retorna o número de ocorrências da string alvo no arquivo.

# >>> stringCount('example.txt', 'line')

# 4



def stringCount(nome_arquivo, string_alvo):
    # 1. Juntar a pasta com a string 'nome_arquivo' que vai receber "exemple.txt"
    caminho = "capitulo_04/exercicios/" + nome_arquivo
    
    # 2. Abrir o arquivo e guardamos a conexão na variável 'arquivo'
    arquivo = open(caminho, "r", encoding="utf-8")
    
    # 3. Ler o conteúdo do arquivo
    conteudo = arquivo.read()
    
    # 4. REGRA DE OURO: Fechar a variável 'arquivo' logo após ler os dados
    arquivo.close()
    
    # 5. Contar as ocorrências e retornamos o número final
    return conteudo.count(string_alvo)

# --- COMO CHAMAR A FUNÇÃO NO SEU SCRIPT --- 
resultado = stringCount("exemple.txt", "line")
print(resultado)

