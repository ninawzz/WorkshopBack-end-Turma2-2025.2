import math

numero = float(input('Digite um número real: '))

def arrendondar(num):
    piso = math.floor(num)
    teto = math.ceil(num)
    
    valorProximo = round(num)
    return piso,teto,valorProximo

print(arrendondar(numero))