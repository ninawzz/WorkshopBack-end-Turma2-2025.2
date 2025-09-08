# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: ")) 

# print(numeros[indice])

# ERRO: IndexError
# O erro foi causado porque o usuario tentou acessar um indice não existente

# Codigo Corrigido:
try:
    numeros = [10, 20, 30]
    indice = int(input("Digite um índice para acessar a lista: ")) 
    print(numeros[indice])
except IndexError:
    print('Erro: não é possivel acessar esse valor')