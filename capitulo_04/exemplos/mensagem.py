mensagem = '''Esta mensagem é secreta e não deverá

ser divulgada a qualquer um que não tenha autorização secreta'''


print(mensagem.find('secreta'))
print(mensagem.count('secreta'))

print(mensagem.replace('sercreta', 'confidencial'))
print(mensagem)

pública = mensagem.replace('secreta', 'pública')
print(pública)

mensagem = 'secreta'
print(mensagem.capitalize())
print(mensagem.upper())


mensagem2 ='''Este vai ser nosso novo texto modelo para estudo'''

print(mensagem2.split(';'))


