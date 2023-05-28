# CONJUNTOS

# 1 - armazena dados únicos; 2 - suporta operaçoes matemáticas
# 3 - não é possível modificar os itens existentes, mas pode 
# adicionar ou remover novos elementos. Conjuntos são mutáveis
# 4 - são iteráveis; 5 - não são considerados sequências como
# listas e tuplas. 6 - podem conter apenas elementos imutáveis
# 7 - não suportam indexação e fatiamento


# declarando conjuntos

# definindo conjunto com chaves
meu_conjunto = {1,2,3,4,5,6}
print(meu_conjunto)


# definindo conjunto via builtin set()
meu_conjunto = set([1,2,3,4,5,6])
print(meu_conjunto)


# definindo conjunto via builtin passando range como argumento
meu_conjunto = set(range(10))
print(meu_conjunto)


# * adicionando ou removendo elementos *

# adicionando um elemento
meu_conjunto = set()
meu_conjunto.add(2)
meu_conjunto.add('teste')
meu_conjunto.add((1,2,3))
print(meu_conjunto)
# {'teste', 2, (1, 2, 3)}


# adicionando múltiplos elementos de uma vez
meu_conjunto = set()
meu_conjunto.update([1,2,3])
print(meu_conjunto)
# {1, 2, 3}


# removendo um elemento

meu_conjunto = set([1,2,3,1,2,3])

# * remove() *
meu_conjunto.remove(2)
print(meu_conjunto)
# {1, 3}


# caso o elemento não esteja presente, teremos uma exceção:
# meu_conjunto.remove(4)



# * discard() *

# utilizando discard, não temos uma exceção levantada caso o elemento não exista
meu_conjunto = set([1,2,3,1,2,3,])
meu_conjunto.discard(2)
print(meu_conjunto)
# {1, 3}


# * clear() *

meu_conjunto = set([1,2,3,1,2,3])
meu_conjunto.clear()
print(meu_conjunto)


# ===================== EXERCÍCIO ===================

conjunto_1 = set(1,1,'Kenzie', 'Academy', 'Kenzie', 10)

# imprima conjunto_1
print(conjunto_1)

# imprima o tamanho de conjunto_1
print(len(conjunto_1))

# adicione o elemento 'Novo Elemento' ao conjunto_1:
conjunto_1.add('Novo Elemento')
print(conjunto_1)

#remova o elemento 'Novo Elemento' do conjunto_1

