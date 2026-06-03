diasemana = 'Quarta'
mês = 'Outubro'
dia = 9
ano = 2013
hora = 11
minuto = 45
segundo = 33


print(diasemana+', '+str(dia)+' de ' +mês+ ',' +str(ano)
+' às '+str(hora)+ ' : '+str(minuto)+':'+str(segundo))

print('{0}:{1}:{2}'.format(hora, minuto, segundo))

# n1  = 12
# n2 = 354

# print('{0:3}{1:5}'.format(n1, n2)) 

# # Alinhamento de dados e colunas
# # 0 é o identificador da minha variável,
# # enquanto 3 após dois pontos : idndica o espaço disponível a frente da variável 


# primeiro = "Bill"
# segundo  = "Gates"


# print("{:10} {:10}".format(primeiro, segundo))
# for i in range(10):
#     print("{:10} {:10}".format(primeiro, segundo))
    
# print("{:8.4}".format(1000 / 3))   
# print((1000 / 3))     

#n = 10

# print("{:b}".format(n)) # mostra o numero em binário
# print("{:c}".format(n)) # mostra o caractere Unicode ao valor interio
# print("{:o}".format(n)) #mostra o numero na base 8

# print("{:d}".format(n)) # mostra o numero da notação decimal 
# print("{:x}".format(n)) # mostra o numero na bsae 16
# print("{:X}".format(n)) # mostra o numero na base 16 com letras maiúsculas

# print("{:6.2f}".format(5 / 3))

#======================================================

# Agora, vamos retornar ao nosso problema original de apresentação dos valores
# de funções i2, i3 e 2i para i = 1, 2, 3, ... até no máximo 12. 
# Especificamos uma largura mínima de 3 para os valores de i e 6 para os valores de i2,
# i3 e 2i para obter a saída no formato desejado.



# for i in range(1,20):
#     print("{:3}{:6}{:6}{:6}".format( i, i**2, i**3, 2*i))
    
    
# def taxaCrescimento(n):
#     print("i  i**2  i**3 2**i") 
#     format_str ="{0:2d}{1:6d}{2:6d}{3:6d}"
#     for i in range(2, n+1):
#         print(format_str.format(i, i**2, i**3, 2**i))   
# taxaCrescimento(12)      