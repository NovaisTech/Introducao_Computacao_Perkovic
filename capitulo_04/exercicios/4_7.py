# Passamos o caminho das pastas a partir da raiz do seu projeto
with open("capitulo_04/exercicios/exemple.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
    
    
def stringCount(nome_arquivo, string_alvo):
    # Consertado: 'as arquivo' no singular para combinar com a linha de baixo
    with open("capitulo_04/exercicios/" + nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        
    return conteudo.count(string_alvo)

# --- CHAMADA DA FUNÇÃO ---
resultado = stringCount("exemple.txt", "line")
print(resultado)