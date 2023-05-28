sting1 = "Hello World"
lista1 = [
    {
        "id": 1,
        "name": "Suzuki",
        "year": 2018,
    },
    {
        "id": 2,
        "name": "Ford",
        "year": 2019,
    },
    {
        "id": 3,
        "name": "Honda",
        "year": 2022,
    },
    {
        "id": 4,
        "name": "Toyta",
        "year": 2021,
    },
    {
        "id": 5,
        "name": "Honda",
        "year": 2021,
    },
    {
        "id": 6,
        "name": "Chevrolet",
        "year": 2018,
    },
]

dicionario1 = {
    "name": "Coiso",
    "age": 1,
    "breed": "Vira-Lata",
}

# 1. Transforme a string 1 em uma lista:
lista = list(sting1)
print(lista)


# Retorne o tamanho da lista1:
print(len(lista1))

# 2. Acesse o último elemento da lista1:
print(lista1[-1])

# 3. Imprima o nome do 2 elemento da lista1:
print(lista1[1].get('name'))


# 4. Insira o seguinte elemento na lista1:
elemento = {
    "id": 6,
    "name": "Jaguar",
    "year": 2015,
}

lista1.append(elemento)
print(lista1)

# 5. Mude o nome do último elemnto da lista1:
lista1[-1]['name'] = 'Fusca'
print(lista1)

# 6. Complete a função e sua chamada para retornar uma lista
# com todos os carros com ano maior que 2020:


def carros(lista):

    lista_nova= []

    for carros in lista:
        if carros['year'] > 2020:
            lista_nova.append(carros)
    return lista_nova


print(carros(lista1))


def carros(lista):

    nova_lista = []

    for carro in lista:
        if carro['year'] > 2020:
            nova_lista.append(carro)
    return nova_lista

print(carros(lista1))


# 7. Complete a função e sua chamada para retornar uma lista com
# todos os carros da marca Honda:


def carros_honda(nome):

    nome_novo = []

    for tipo in nome:
        if tipo['name'] == 'Honda':
            nome_novo.append(tipo)
    return nome_novo

print(carros_honda(lista1))

# 8. Complete a função e sua chamada para imprimir o dicionário:


def show_dict(**dicionário):
    print(dicionário)
show_dict(**dicionario1)

# 9. Adicione a chave 'color' com o valor 'white' ao dicionario 1:

dicionario1.update({'color': 'white'})
print(dicionario1)