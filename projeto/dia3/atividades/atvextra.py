notas = []
def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
       
    try:
        return soma / quantidade
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
        
for x in range(4):
        try:
            x = int(input('Digite um número: '))
            notas.append(x)
        except ValueError:
            print('Digite um número válido')            


media = calcular_media(notas)
print(f"Média: {media}")