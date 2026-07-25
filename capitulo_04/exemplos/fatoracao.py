from sympy import symbols, factor, expand

a, b = symbols("a b")

expressao = 3*a + 3*b
expressao_fatorada = factor(expressao)


print("Expressão original:", expressao)
print("Resultado fatorado:", expressao_fatorada)

print("Conferidno (expandindo):", expand(expressao_fatorada))