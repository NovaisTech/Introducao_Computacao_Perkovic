# ====================================== 1. Calculadora de Churrasco ====================================

# Esse projeto aplica conceitos de aritmética e variáveis de forma prática.
# O que praticar: Operações matemáticas (+, -, *, /), tipos de dados numéricos e strings.
# O projeto: Crie um script que receba (via variáveis pré-definidas ou input()) a quantidade de adultos e crianças.
# Lógica: Defina uma média de consumo (ex: 400g de carne por adulto, 200g por criança).
# Saída: O programa deve calcular o total de carne necessário e o custo total estimado com base em um preço por quilo que você definir.
# Dica de Objeto: Tente armazenar os preços em uma lista para praticar o acesso via índices.

conv_Adultos = int(input("Digite a quantidade de convidados: "))
conv_infantis = int(input("Digite a quantidade de crianças: "))

consumo_Adulto = 400
consumo_Infantil = 200 

kg_Carne = [29.00, 18.00, 25.00]




total_Gramas = (conv_Adultos * consumo_Adulto) + (conv_infantis * consumo_Infantil)
total_Kg = total_Gramas / 1000    # 1000 gramas 

custo_Carne = total_Kg * kg_Carne[0]

print("-" * 30)
print(f"Total de carne necessária: {total_Gramas}Kg")
print(f"Cursto total estimado: R$ {custo_Carne:.2f}")