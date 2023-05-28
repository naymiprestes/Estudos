# TUPLAS // são imutáveis, ideais para armazenar dados agrupados

# declarando tuplas

minha_tupla = (10,20,30)
print(minha_tupla)
print(type(minha_tupla))


tupla_de_um_elemento = (10,) # tem que ser finalizada com vírgula
print(tupla_de_um_elemento)
# (10,)


tupla_vazia = ()
print(tupla_vazia)
# ()


#convertendo iteráveis, como string e lista em tupla
tupla_tuple = tuple('Teste')
print(tupla_tuple)



# acessando elementos // acessando indices das tuplas
minha_tupla = (10,20,30)
print(minha_tupla[2])


# manipulando tuplas

# verificando seu tamanho
print(len(minha_tupla))

# verificando se tupla possui determinado elemento
print(30 in minha_tupla)
print(10 in minha_tupla)


# verificando o número de aparições de um elemento
print(minha_tupla.count(10))
print(minha_tupla.count(40))


# verificando o indice de um elemento a partir de seu valor
minha_tupla = ('João', 'José', 'Joana', 'João')
print(minha_tupla.index('João'))


# * imutabilidade das tuplas * 
# // impossível reattrinuir valores em seus indices

minha_tupla = ('Joao', 'Maria', 'Joana',)
#minha_tupla[0] = 'Pedro'


# ===================== EXERCÍCIO ===================

tupla_1 = ('valor_1', 2, 3.1, 'Kenzie Academy', ['Elemento1', 'Elemento2'], 'Kenzie Academy')

# imprima tupla_1:
print(tupla_1)

# imprima o último elemento da tupla
print(tupla_1[-1])

# imprima o tamanho de tupla_1
print(len(tupla_1))

# imprima a contagem de elementos Kenzie Academy
print(tupla_1.count('Kenzie Academy'))

# imprima o indice do elemento 3.1 da tupla_1:
print(tupla_1.index(3.1))

# alterar o último elemento da para 'último elemento'
tupla_1[-1] = 'Último Elemento'
print(tupla_1)