# PACKING (empacotamento) / UNPACKING (desempacotamento)

# *args // quando o número de argumentos for desconhecido

# acessando valores por indexação

tabuada_5 =  [n for n in range(1,51) if n % 5 == 0 ]
print(tabuada_5[0])
print(tabuada_5)

print(tabuada_5[1:4])
# [10, 15, 20]


# acessando valores por desempacotação
#v1, v2, v3, v4, v6, v7, v8, v9, v10 = tabuada_5
#print(v1)

# pegando o primeiro, segundo e compactando o restante
#primeiro, segundo, terceiro, *restante = tabuada_5
#print(primeiro)


def exibir(*args):
    return f'o tipo de {type(args)} e os valores são: {args}'

resultado = exibir(10,True, 9.5, None, 'Carro')
print(resultado)



frutas_tropicais = ['Abacaxi', 'Açaí', 'Acerola', 'Caju']
frutas_invernais = ['Abacate', 'Morango', 'Kiwi', 'Maçã']

# adicionando elementos a uma nova_lista usando asterisco
frutas_atualizadas = [*frutas_tropicais, 'Banana']
print(frutas_atualizadas)


# juntando as duas listas

frutas_atualizadas = [*frutas_tropicais, *frutas_invernais]
print(frutas_atualizadas)


# acessando item a item com um loop for
def frutas(*frutas):
    print('acessando frutas')

    for fruta in frutas:
        print(f'a fruta da vez é: {fruta}')

frutas('Abacaxi', 'Banana', "Maçã")


def animais(*animais):
    for animal in animais:
        print(animal)
animais('Gato', 'Cachorro', 'Peixe')

def flores(*flores):
    for flor in flores:
        print(flor)
flores('Girasol', 'Rosa')

def nomes(*nomes):
    for nome in nomes:
        print(nome)
nomes('Santiago', 'Vitório', 'Floquinho')



# * kwargs * // quando tem keys indeterminadas 

def pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f'chave -> {chave} - valor: {valor}')
pessoa(nome='José', idade=38, profissao='programador')


# atualizando um dicionário

