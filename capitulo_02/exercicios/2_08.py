# ======================  Problema Prático 2.8  ====================================

# Em que ordem os operadores nas expressões a seguir são avaliados?
# A ordem é indicada por meio de parênteses:

# (a) 2 + 3 == 4 or a >= 5

a =2
print((2 + 3) == 4) or (a >= 5) # defini um valor para 'a' pra não gerar erro

# (b) lst[1] * -3 < -10 == 0

lst = [1 , 2, 3]
print(((lst[1]) * (-3)) < (-10 ))== 0

# (c) (lst[1] * -3 < -10) in [0, True]

print(((lst[1]) * (-3)) < (-10)) in [0, True]
# (d) 2 * 3**2
print(2 * (3**2))

# (e) 4 / 2 in [1, 2, 3]
print((4 / 2) in ([1, 2, 3]))
