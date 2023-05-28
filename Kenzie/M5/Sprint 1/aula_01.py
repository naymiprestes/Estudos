#VARIÁVEIS

#declarando variáveis
minha_string = "hello"

# verificando o tipo de uma variável

print(type(minha_string)) # output: <class: 'str'>

meu_inteiro = 123
print(type(meu_inteiro)) #output: <class: 'int'>

meu_decimal = 3.1415
print(type(meu_decimal)) # output: <class: 'float'>

meu_booleano = True
print(type(meu_booleano)) # output: <class: 'boolean'>

meu_vazio = None
print(type(meu_vazio)) # output: <class: 'NoneType'>

MINHA_CONSTANTE = 'Olá, M5'
print(type(MINHA_CONSTANTE))



# PRINCIPAIS CARACTERÍSTICAS DO PYTHON

#TIPAGEM DINÂNMICA

minha_string = '2'
print(type(minha_string)) #output: <class: 'str'>
minha_string = '1500' #atribuindo um novo valor, pois é do tipo string.

# TIPAGEM FORTE

meu_numero = 1
print(type(meu_numero))

#soma = meu_numero + minha_string
 # output: unsuported operand type(s) for +: 'int' and 'str'


# *DEFININDO FUNÇÕES*

def minha_funcao():
    meu_valor = 1234
    return meu_valor
print(minha_funcao()) # output: 1234

print(type(minha_funcao)) #output: <class: 'function'>










