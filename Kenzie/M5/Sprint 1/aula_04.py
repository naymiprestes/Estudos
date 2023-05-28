# FUNÇÕES E BUILTINS

# funções

def soma(num1, num2):
    return num1 + num2

resultado = soma(4, 5)
print(resultado)
print(soma(2,2))

# argumentos nomeados // recebe o argumento em qualquer ordem, desde que especifique o nome


def calculo_imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado
resultado = round(calculo_imc(80, 1.80), 2)
print(resultado)

# invertendo a ordem dos valores, nossa funcção não funciona como o esperado
resultado = calculo_imc(1.80, 80)
print(resultado)


# nomeando os argumentos, podemos passá-los em qualquer ordem
resultado = calculo_imc(altura=1.80, peso=80)
print(resultado)

# *Funções built-ins*

#conversão de inteiro para booleano
my_bool = bool(0)
print(my_bool)
# False

# conversão de inteiro para string
my_str = str(400)
print(my_str)
# '400'

# conversão de inteiro para decimal

my_float = float(7)
print(my_float)
# 7.0

# conversão de string pra inteiro

my_int = int('14')
print(my_int)
# 14

# verificar tamanho sequencial de uma estrutura sequencial
my_str = 'kenzie Academy Brasil'
print(len(my_str))
# 21

# =============== ATIVIDADE =====================

def delta(a, b, c):
    
    resultado = b ** 2 -4 * a * c


from aula_04 import delta
def bhaskara(a, b, c):
    ...