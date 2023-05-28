valores = [1,2,3,4,5]

lista_1 = []

# for item in valores:
#     lista_1.append(item * 2)
# print(lista_1)

result = [item * 2 for item in valores] #o primeiro item é o que vai popular, o segundo item é o que iterar os valores
print(result)



# numeros pares

# lista_2 = []

# for item in valores:
#     if item % 2 == 0:
#         lista_2.append(item)
# print(lista_2)

result = [item for item in valores if item % 2 == 0]
print(result)


#MENSAGEM DE NUMEROS PARES

lista_3 = []

for item in valores:
    if item % 2 == 0:
        lista_3.append("PAR")
    else:
        lista_3.append("IMPAR")
print(lista_3)

# o primeiro vai popular a lista,
result = ["PAR" if item % 2 == 0 else "IMPAR" for item in valores]
print(result)


# OUTRO ASSUNTO  DictComprehension
# conjuntos(separado por virgula e não tem valor)
#conjuntos tem alguns métodos nele

valid_key = {"name", "age", "team", "adddress", "favorite_food"}

body = {
    "name": "Yurran",
    "age": 22,
    "team": "Warriors"

}

#mostrandos os items que não tem no body
missing_keys = valid_key.difference(body)
print(missing_keys)
print(bool(missing_keys))
# se o set tem algo dentro(o que ta faltando) ele retorna True

#mostra os campos que estão faltando e uma mensagem com a chave
if missing_keys:
    result = {key:"missing key" for key in missing_keys}
    print(result)
else:
    print("tudo certo")