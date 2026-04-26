# =============================   Problema Prático 3.4   ===========================
# ==================================================================================

# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos.
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
# Aqui está um exemplo de um login bem-sucedido:


lista  = ['joe', 'sue', 'hani', 'shopie']
login = input("Digite sua identificação de login: ")

if login in lista:
    print(f"Login: {login}")
    print("Você entrou!")
else:
    print(f"Login: {login}")
    print("Usuário desconhcido")
    
    

            
