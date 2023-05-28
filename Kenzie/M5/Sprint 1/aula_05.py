# ESTRUTURAS CONDICIONAIS

# operadores relacionais

x = 1
y = 2
print(x > y)
print( x != y)

# operadores lógicos

print(2 > 1 and 5 < 3)
print(2 > 1 or 5 < 3)
print(not(0 == 0))


# if

def nota_aluno():

    entrada = input('Digite a sua nota: ')
    nota = float(entrada)

    if nota >= 8.0:
        print(f'Sua média é {nota}, logo, você está aprovado.')
    if nota < 8.0:
        print(f'sua média é {nota}, logo, você não está aprovado.')
nota_aluno()

# else

entrada = input('Digite sua nota: ')
nota = float(entrada)

if nota >= 8.0:
    print(f'Sua média é {nota}, logo, você está aprovado.')
else:
    print(f'Sua média é {nota}, logo, você não está aprovado.')


# elif

entrada = input('Digite sua nota')
nota = float(entrada)

if nota >= 8.0:
    print(f'Sua média é {nota}, logo, você está aprovado.')
elif nota >= 4.0 and nota <= 6.0:
    print(f'Sua nota é {nota}, portanto você está de recuperação.')
elif nota > 6.0 and nota < 8.0:
    print(f'Sua média é {nota}, você está aprovado, porém com ressalvas, fique atento.')
else:
    print(f'Sua média é {nota}, logo, você não está aprovado.')
