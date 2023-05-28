# LISTAS // são mutáveis e sequenciais

# criando uma lista

# podemos criar uma lista com sintaxe literal [ ]
minha_lista = [3, 'abacate', 9.7, [4,5,6], (3,'j')]
print(minha_lista[3])
print(minha_lista[4])

# utilizando a função list() para trabalhar com lista
minha_lista = list('abc')
print(minha_lista)
# ['a', 'b', 'c'] // iterável => retorna seus membros um de cada vez (list, str, tuple) - tipos de sequência

# minha_lista = list(123)
# Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable


# criando uma lista com range(intervalor_inicial, intervalor_final, passo)

# para criarmos um valor de 0 a 5
minha_lista = list(range(6))
print(minha_lista)
# [0, 1, 2, 3, 4, 5]

# para criarmos um valor no intervalor de 15 a 20
minha_lista = list(range(15, 21))
print(minha_lista)
#[15, 16, 17, 18, 19, 20]


# para criarmos um valor no intervalor de 15 a 20 com um passo de 2:
minha_lista = list(range(15, 21, 2))
print(minha_lista)
#[15, 17, 19]


# *Loop for em listas*

carrinho_de_compras = ['Banana', 'Pera', 'Tomate']

for item in carrinho_de_compras:
    print(item)

# Banana
# Pera
# Tomate


# *alterando elemento de uma lista*

minha_lista = ['1', '2', '3']
print(minha_lista)
# ['1', '2', '3']

# vamos alterar o segundo elemento para a palavra 'teste'
minha_lista[1] = 'teste'
print(minha_lista)
# ['1', 'teste', '3']


# *fatiamento de listas*

minha_lista = ['1', 'teste', '3']

# acessando o primeiro elemento
minha_lista[0]
# 1

# para acessarmos o último elemento temos duas maneiras:

minha_lista[2]
print(minha_lista) # 3

minha_lista[-1] # 3


# acessando um intervalor do começo da lista, até o indice 2
# lembrando que o limite(no caso o indice 2), não é considerado no fatiamento.
# para pegar o último teria que ser a posição 3 [0:3]

print(minha_lista[0:2])
#['1', 'teste']


# acessando um intervalor entre o início e o indice 3 com o passo de 2:
print(minha_lista[:3:2])
#['1', '3']

# acessando toda a lista com passo de 2
print(minha_lista[::2])
# ['1', '3']

print(minha_lista[:])
# ['1', 'teste', '3']



# *manipulação de listas*

minha_lista = [1,2,3,1]

#tamanho da lista
print(len(minha_lista))
# 4

# adicionando um item ao final da lista
minha_lista.append(4)
print(minha_lista)
# [1, 2, 3, 1, 4]

# contando as ocorrencias de um determinado valor
print(minha_lista.count(1))
# 2

# adiciona os valores de um iterável a lista original
minha_lista.extend([100, 200, 300])
print(minha_lista)

# retorna o indice da primeira ocorrência de um determinado valor
print(minha_lista.index(1))

# remove e retorna um item baseado no seu indice
print(minha_lista.pop(0))
print(minha_lista)


# remove a primeira ocorrência de determinado item da lista, alterando a original.
minha_lista.remove(200)
print(minha_lista)
#[2, 3, 1, 4, 100, 300]


# limpa todos os itens da lista
minha_lista.clear()
print(minha_lista)
# []




# * ordenando listas *

# sorted() // recebe como argumento um iterável

minha_lista = ['hi', 'hello', 'olá']

# é retornada uma nova lista
print(sorted(minha_lista))
# ['hello', 'hi', 'olá']

print(sorted(minha_lista, reverse=True))
# ['olá', 'hi', 'hello']

# lista original não foi modificada
print(minha_lista)


# * sort() *

minha_lista = ['hi', 'hello', 'olá']

minha_lista.sort()
print(minha_lista)


minha_lista.sort(reverse=True)
print(minha_lista)


# ===================== EXERCÍCIO ========================


# crie uma lista dos inteiros de 6 a 20(ambos inclusos) utilizando range
lista_1 = list(range(6,21))
print(lista_1)

# imprima o último elemento da lista_1
print(lista_1[-1])

# altere o segundo elemento de lista_1 para 'kenzie'.
lista_1[1] = 'Kenzie'
print(lista_1)

# utilize o fatiamento para imprimir somente elementos de indice 2,3,4 de lista_1
print(lista_1[2:5])

# Adicione o seguinte valor ao final de lista_1: 'Academy'.
lista_1.append('Academy')
print(lista_1)

# Remova os items referentes aos valores 'Kenzie' e 'Academy'.
lista_1.remove('Kenzie')
lista_1.remove('Academy')
print(lista_1)

#Crie e imprima uma nova lista ordenada inversamente (lista_2) com base em lista_1, sem ordenar de fato a lista_1.

lista_2 = sorted(lista_1, reverse=True)
print(lista_2)


# Imprima o tamanho de lista_1 e lista_2
print(len(lista_1), len(lista_2))

# Retire o ultimo item de lista_1 e lista_2.
print(lista_1.pop(), lista_2.pop())

# Retire todos os elementos tanto de lista_1 quanto de lista_2.
lista_1.clear()
lista_2.clear()
print(lista_1,lista_2)






