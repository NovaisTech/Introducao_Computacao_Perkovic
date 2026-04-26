# 2.2 Strings: 
# Explora a manipulação de texto, incluindo concatenação, replicação e indexação.
# Os exercícios desafiam o aluno a extrair partes específicas de uma frase.
# -------------------------------------------//-------------------------------------------------#


#================================================================================================
#------------------------------Problema Prático 2.4-------------------------------------#

#Comece executando as instruções de atribuição:

s1 = 'ant'

s2 = 'bat'

s3 = 'cod'

# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:

# (a)'ant bat cod'

print(s1 + ' ' + s2  + ' ' + s3)

# (b)  'ant ant ant ant ant ant ant ant ant ant'

print((s1 +' ')*  10)

# (c)   'ant bat bat cod cod cod'

print(s1 + ' ' + s2 + ' ' + s2 + ' ' + s3 + ' ' + s3 + ' ' + s3)

print(s1 + ' ' + (s2 + ' ') * 2  + (s3 + ' ' ) * 3)

# (d)'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'

print((s1 + ' ' + s2 + ' ') * 7)

# (e)'batbatcod batbatcod batbatcod batbatcod batbatcod'

print((s2 + s2 + s3 + ' ') * 3  )


#================================================================================================
#                         Operador de Indexação []

# ------------------  Problema Prático 2.5 ---------------------------------------#
# Comece executando a atribuição:
s = '0123456789'
# Agora, escreva expressões usando a string s e o operador de indexação que é avaliado como:

# (a)'0'
print(s[0])
print(s[-10])

# (b)'1'
print(s[1])
print(s[-9])

# (c)'6'
print(s[6])
print(s[-4])

# (d)'8'
print(s[8])
print(s[-2])

# (e)'9
print(s[9])
print(s[-1])