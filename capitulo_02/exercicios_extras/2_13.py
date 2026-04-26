# 2.13 Comece avaliando, no shell interativo, a atribuição:

s1 = '-'

s2 = '+'

# Agora, escreva expressões de string envolvendo s1 e s2 e os operadores de string + e * que são avaliados como:

# (a)'-+'
print(s1 + s2)

# (b)'–+'
print(s1 + s2)

# (c)'+––'
print(s2 + s1 + s1)

# (d)'+––+––'
print(s2 + s1 + s1 + s2 + s1 + s1)

# (e)'+––+––+––+––+––+––+––+––+––+––+'
print(((s2 + s1 + s1 )*10) + (s2))

# (f)'+–+++––+–+++––+–+++––+–+++––+–+++––'
print(((s2 + s1) + ((s2)*3 +s1 + s1))*5)

# Tente tornar suas expressões de string as menores possíveis.