# 2.18 Escreva instruções Python correspondentes ao seguinte:

# (a) Atribua à variável flores uma lista contendo as strings 'rosa', 'buganvília', 'iúca', 'margarida', 'dália' e 'lírio dos vales'.
flores = ['rosa', 'buganvília','iúca', 'marga', 'dália', 'lírio dos vales']

# (b)Escreva uma expressão Booleana que é avaliada como True se a string 'batata' estiver na lista flores e avalie a expressão.

print('batata' in flores)

# (c)Atribua à lista espinhosas a sublista da lista flores consistindo nos três primeiros objetos na lista.
espinhosa = ['rosa', 'buganvília','iúca']
flores.extend(espinhosa)
print(flores)

# (d)Atribua à lista venenosas a sublista da lista flores consistindo apenas no último objeto da lista flores.
venenosas = ['lírio dos vales']
flores.extend(venenosas)
print(flores)


# (e)Atribua à lista perigosas a concatenação das listas espinhosas e venenosas.
perigosa = [espinhosa + venenosas]
print(perigosa)