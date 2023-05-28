d1 = {'nome': 'Kenzinho', 'cidade': 'Curitiba', 'módulo': 'M5'}
print(d1)

print(d1['nome'])
print(d1)


d1.get('telefone', 'a chave telefone não existe')
print(d1)

d1.keys()
print(d1)

d1.values()
print(d1)

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

d2 = dict(zip(lista_1, lista_2))
print(d2)

d2.update(d1)
print(d2)

del d1['casado']
print(d1)

print(d1.pop('idade'))

d1.clear()
print(d1)