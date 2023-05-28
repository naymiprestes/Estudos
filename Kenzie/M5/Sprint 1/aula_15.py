# CÓPIA RASA E CÓPIA PROFUNDA

# * cópia rasa * // cópia do objeto original em um novo espaço de memória

lista_1 = [1,2,3]
# aqui estamos  copiando apenas o valor de list_1, sem sua referência de memória
lista_2 = lista_1.copy()
print(lista_2)


print(lista_1)
print(lista_2)

print(id(lista_1))
print(id(lista_2))

# não possuem o mesmo espaço de memória
print(lista_1 is lista_2)

print(lista_1 == lista_2)


# * cópia profunda * // criam novas referências 

list_original = [1,2,3, ['a', 'b', 'c'], 4]
list_copy = list_original.copy()


# alterando os elementos ddentro de list_copy
list_copy[0] = 10
list_copy[3][0] = 'Z'
print(list_copy)
print(list_original)
# [10, 2, 3, ['Z', 'b', 'c'], 4]
# [1, 2, 3, ['Z', 'b', 'c'], 4]

import copy

list_original = [1,2,3, ['a', 'b', 'c'], 4, 5, 6]
list_copy = copy.deepcopy(list_original)
list_copy[3][0] = 'Z'
print(list_copy)
print(list_original)
# [1, 2, 3, ['Z', 'b', 'c'], 4, 5, 6]
# [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]


