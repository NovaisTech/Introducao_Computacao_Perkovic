# 2.15 Comece executando

s = 'goodbye'

# Depois, escreva uma expressão Booleana que verifica se:
#(a) O primeiro caractere da string s é 'g'
print("O primeiro caracater da string s é 'g'", s[0] == "g") 


#(b) O sétimo caractere de s é g
print("O sétimo caractere de string s é 'g'", s[6] == "g")


#(c) Os dois primeiros caracteres de s são g e a
print("O dois primeiros caracteres são 'g' e 'a'", s[0] == "g"  and s[1] == "a")

#(d) O penúltimo caractere de s é x
print("O penúltimo caractere de s é 'x':",s[-1] == "x")

#(e) O caractere do meio de s é d
print(len(s))
print("O caractere do meio de s é 'd'?", s[3] == "d")

#(f) O primeiro e último caracteres da string s são iguais
print("O primeiro e último caracteres da string s são iguais?", s[0] == s[-1])

#(g) Os 4 últimos caracteres da string s correspondem à string 'tion'
print("Os 4 últimos caracteres da string s correspondem à string 'tion'?", s[-4:] == 'tion')
# Outra maneira é usar, dito que evita erros caso string seja curta.
print(s.endswith('tion')) 

# Nota: Essas sete instruções devem ser avaliadas como True, False, False, False, True, False e False, respectivamente.