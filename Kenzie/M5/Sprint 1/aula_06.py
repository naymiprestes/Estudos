# ESTRUTURAS DE REPETIÇÃO

# loop for em string

string = 'Kenzie'

for letra in string:
    print(letra)

string = 'Santiago'

for nome in string:
    print(nome)


# loop for com contador
for i in range(4):
    print(i)


# usando _ no lugar do contatdor
for _ in range(3):
    print('Olá Kenzie')


# *Loops utilizando while*

contador = 0

while contador <= 5:
    print(f'Contando: {contador}')
    contador += 1

print('fim da contagem')


# *Enumerate*

minha_string = 'Churros'

#podemos desempacotar a tupla em indice e item
for indice, item in enumerate(minha_string):
    print(indice, item)


# Auxiliadores break, continue e pass

# break

for numero in range(5):
    print(numero)

for numero in range(10):
    if numero == 3:
        break
    print(numero)


# continue

for numero in range(10):
 
# checa se o número está contido na lista de números
    if numero in[4,5,6,7,8]:
        continue
    print(numero)

for numero in range(5):
    if numero in[2,3,4]:
        continue
    print(numero)


numero = 0

while numero <= 6:
    numero += 1

    if numero == 2 or numero == 3:
        continue
    print(numero)


# pass

for item in range(10):
    pass

def funcao():
    pass

# ... como atalho

for item in range(10):
    ...

def funcao():
    ...
