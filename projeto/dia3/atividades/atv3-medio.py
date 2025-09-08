#Codigo errado:
# def somar(a, b):
#     return a + b

# resultado = somar(10, "5")
# print(resultado)

# Codigo certo:
def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)

# ERRO -> TypeError
# O erro foi causado porque não é possivel somar int com string 