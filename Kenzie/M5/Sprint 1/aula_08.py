# DICIONÁRIOS // agrupa dados em formato chave e valor. São de tipo imutáveis

# criando um dicionário

# forma literal
meu_dicionario = {'chave': 'valor'}
print(meu_dicionario)
print(type(meu_dicionario))


# forma builtin
meu_dicionario = dict(primeiro = 1, segundo = 2, terceiro = 3)
print(meu_dicionario)


# tentando criar duas chaves iguais
meu_dicionario = {'chave': 'valor_1', 'chave': 'valor_2'}
# entre as duas, a chave criada por último tem prioridade
print(meu_dicionario)


# podemos também passar ums lista contendo tuplas, representando chave e valor
meu_dicionario = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])
print(meu_dicionario)


# *builtin zip* // transforma dois iteráveis em dicionário

# se um dos iteráveis tiver mais elementos que o outro, ele será ignorado
lista_1 = ['primeiro', 'segundo', 'terceiro', 'quarto']
lista_2 = [1,2,1]
meu_dicionario = dict(zip(lista_1, lista_2))
print(meu_dicionario)


# *loop for em dicionários*

pessoa = {'nome': 'José da Silva', 'idade': 36, 'sexo': 'masaculino' }

# se iteramos somente pelo dicionário o loop será feito apenas pelas chaves:
for item in pessoa:
    print(item)

# o equivalente ao loop acima seria
for item in pessoa.keys():
    print(f'keys {item}')

# se quisermos iterar sobre tanto chave quanto valor,
# perceba que o valor printado é uma estrutura que ainda não conhecemos:
# uma tupla

for item in pessoa.items():
    print(item)


# podemos desempacotar a estrutura anterior em duas variáveis
# veremos esse conceito com mais detalhes no futuro
for key, value in pessoa.items():
    print('chave ->', key)
    print('valor ->', value)


# entendo melhor

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# o retorno é um objeto do tipo dict_keys
print(meu_dicionario.keys())

# o retorno é um objeto do tipo dict_values
print(meu_dicionario.values())

# o retorno é um objeto do tipo dict_items
print(meu_dicionario.items())


# dessa forma temos a liberdade para converter para o tipo que quisermos
# .keys() para lista
print(list(meu_dicionario.keys()))

# .keys() para tupla
print(tuple(meu_dicionario.keys()))

# .items() para dict
print(dict(meu_dicionario.items()))


# acessando elementos

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# acessando o valor da chave 'segundo'
print(meu_dicionario['segundo'])


# * get() *

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

#acessando elemento existente com get()
print(meu_dicionario.get('segundo'))

print(meu_dicionario.get('quarto', 'chave não encontrada.'))


# adicionando e atualizando itens de um dicionário

meu_dicionario = dict(primeiro = 1, segundo = 2, terceiro = 3)
print(meu_dicionario)

# para adicionar a chave com o valor 4, basta fazer o seguinte:
meu_dicionario['quarto'] = 4
print(meu_dicionario)

# se o elemento já existir, ele será atualizado
meu_dicionario['quarto'] = 5
print(meu_dicionario)


# * update() *

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
print(meu_dicionario)

meu_dicionario.update({'quarto': 4})
print(meu_dicionario)

meu_dicionario.update({'quarto': 5})
print(meu_dicionario)

meu_dicionario.update({'quinto': 7})
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2, 'terceiro': 3, 'quarto': 5, 'quinto': 7}


# excluindo elementos

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3 }
del meu_dicionario['primeiro']
print(meu_dicionario)
# {'segundo': 2, 'terceiro': 3}



# * pop() * //  remove o elemento especificado via chave
          # // retorna o valor do elemento excluído


# utilizando pop

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
meu_dicionario.pop('primeiro')
print(meu_dicionario)



# * popitem() * // exclui o último elemento e retorna uma tupla

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
meu_dicionario.popitem()
print(meu_dicionario)
# {'primeiro': 1, 'segundo': 2}



# limpando dicionários


# * clear() * // remove todos os elementos

meu_dicionario = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
meu_dicionario.clear()
print(meu_dicionario)


# ================= EXERCÍCIO =================

d1 = {'nome': 'Kenzinho', 'cidade': 'Curitiba', 'módulo': 'M5'}
print(d1)

# imprima o tipo de d1:
print(type(d1))

# imprima o valor da chave nome:
print(d1['nome'])

# imprima o valor da chave cidade:
print(d1['cidade'])

# imprima o valor da chave módulo:
print(d1['módulo'])

# imprima o valor da chave tefone e caso não exista diga que não existe
print(d1.get('telefone', 'a chave telefone não existe'))

# imprima o valor da chave cep, caso não exista diga.
print(d1.get('cep', 'a chave cep não existe'))

# imprima somente as chaves de d1 (formato dict_keys)
print(d1.keys())

# imprima somente os valores de d1 (formato dict_values)
print(d1.values())

# a partir das seguintes listas, crie um dicionário d2,
# em que lista_1 sejam suas chaves e lista_2 sejam seus
# valores, na mesma ordem.

lista_1 = ['telefone', 'casado', 'idade']
lista_2 = ['999-999-999', False, 28]

d2 = dict(zip(lista_1, lista_2))
print(d2)

# atualize o dicionário d1 com o conteúdo do dicionário d1. Imprima d1
d1.update(d2)
print(d1)

# delete a chave casado de d1
del d1['casado']
print(d1)

# remova e imprima o valor da chave idade de d1
print(d1.pop('idade'))
print(d1)

# remova todos items do dicionário d1
d1.clear()
print(d1)
