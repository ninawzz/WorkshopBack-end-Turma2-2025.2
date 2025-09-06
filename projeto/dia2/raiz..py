import math
numero = int(input('Digite um número: '))

def calcular_raiz(num):
    raiz = math.isqrt(num)
    return raiz

print(calcular_raiz(numero))