# MÓDULOS, PACOTES E IMPORTS

# módulo // pode ser importado para outro arquivo, para
      # // poder reutilizar a lógica, sem a necessidade
     # // de reescrever o código.


# a diferença de um módulo para um arquivo .py é que não,
# rodamos o módulo, nós importamos o código para utilizar
# em outro código ou até mesmo no mesmo módulo.


# * importação absoluta *

# é quando chamamos o arquivo a partir da raiz do projeto

# ex: from soma import somar
    #(nome do arquivo) | # nome da função

# ex: from subtracao import subtrair



# * Pacotes *

# // são diretórios que agregam os módulos, dentro dele cria
# um arquivo chamado __init__.py


# // o módulo soma esta dentro do pacote operações matemáticas

# ex: operacoes_matematicas.soma import somar



# * importação relativa * // se refere ao nível que você
                       # // está dentro do projeto

# ex: .soma import somar
# ex: .subtracao import subtrair

# obs: ao colocar .(ponto/dot), é refrenciado ao python o
# nível do projeto que estamos.
    # ex: ./ - referencia ao diretório atual [Linux]
        #  . - referencia ao diretório atual [Python Import]



 
