#STRINGS

#utilizando ' entre ""

minha_string = "Estou em Martha's Vineyard, na Virginia."
print(minha_string)

# utilizando / para esapar aspas ' dentro da string ''

minha_string = "estou em Martha\'s Vineyard, na Virginia."
print(minha_string)


# *INTERPOLAÇÃO*

minha_string = 'Hello Kenzie'
print(f'Tipo de string: {type(minha_string)}')
# Tipo de string: <class: 'str'>
print(f'Oi, {minha_string}')


# *CONCATENAÇÃO*

string_1 = 'cow'
string_2 = 'boy'
new_string = string_1 + string_2
print(new_string)
# cowboy


# *Acessando Caracteres*

string = 'Kenzie'
print(string[0]) # K
print(string[-1]) # e


# *FATIAMENTO (Slicing)*

#acessando a palavra Monty
string = 'Monty Python'
print(string[0:5])


# podemos omitir o 0, pois queremos o início da string
print(string[:5])

# acessando a palvra Python
print(string[6:12])

# como queremos ir até o fim da string, podemos omitir o 12
print(string[6:])

#acessando toda a string
print(string[0:12])

#omitindo o início e o fim
print(string[:])

#acessando toda a string, com passo 2
print(string[0:12:2])

#omitindo início e fim
print(string[::2])


#MANIPULANDO STRING

#*Capitalize* não modifica string original

string = 'mOnTy pYtHon'
print(string.capitalize())
# Monty python


# *Count* não modifica string original

string = 'Monty Python'
print(string.count('Python'))
# 1
print(string.count('o'))
# 2


# *Split* não modifica string original

string = 'Monty Python'
print(string.split())
# ['Monty', 'Python']

string = 'Monty+Python'
print(string.split('+'))
# ['Monty', 'Python']

# *Join*
string = 'Monty Python'
print('+'.join(string))
# M+o+n+t+y+ +P+y+t+h+o+n



# def sum_str(a, b):
    
#     sum = int(a) + int(b)
#     result = str(sum)
#     print(type(result))
#     return result
# print(sum_str('2'))