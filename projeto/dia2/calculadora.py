import math
opcao = int(input('Digite o número de acordo com a opção desejada: \n1. Área do circulo\n2.A área de um triângulo\n3. A hipotenusa de um triângulo retângulo\n>> '))

class calcular:
    def calcular_circulo(num):
        area = math.pi * (raio** 2)
        return area
    
    def triangulo(baset, alturat):
        return (baset * alturat) / 2
    
    def calcular_hipotenusa(c1,c2):
        hipotenusa = math.isqrt((c1 ** 2) + (c2 ** 2))
        return hipotenusa
        
        
if opcao == 1:
    raio = float(input('Digite o raio do círculo: '))
    print(f'{calcular.calcular_circulo(raio):.2f}')
elif opcao == 2:
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    print(f'{calcular.triangulo(base,altura):.2f}')
    
elif opcao == 3:
    cateto1 = int(input('Digite o valor do primeiro cateto: '))
    cateto2 = int(input('Digite o valor do segundo cateto: '))
    print(calcular.calcular_hipotenusa(cateto1,cateto2))

    
