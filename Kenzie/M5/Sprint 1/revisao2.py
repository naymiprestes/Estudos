lista_1 = list(range(6,21))
print(lista_1)

lista_1[-1]
print(lista_1)

lista_1[1] = 'Kenzie'
print(lista_1)

lista_1[2:5]
print(lista_1)

lista_1.append('Academy')
print(lista_1)

lista_1.remove('Kenzie')
lista_1.remove('Academy')
print(lista_1)

lista_2 = sorted(lista_1, reverse=True)
print(lista_2)

len(lista_1)
len(lista_2)
print(lista_1, lista_2)

lista_1.pop()
lista_2.pop()
print(lista_1, lista_2)

lista_1.clear()
lista_2.clear()
print(lista_1, lista_2)