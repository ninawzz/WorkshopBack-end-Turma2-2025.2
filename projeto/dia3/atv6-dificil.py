# dados = {
#     "nome": "Isaac ",
#     "idade": 25,
#     "cidade": "São Paulo"
# }

# chave = input("Digite a chave que deseja acessar: ")
# print(f"O valor da chave '{chave}' é: {dados[chave]}")

# Erro:  O usuário tentou acessar uma chave inexistente
# Codigo corrigido:
try:
    dados = {
        "nome": "Isaac ",
        "idade": 25,
        "cidade": "São Paulo"
    }

    chave = input("Digite a chave que deseja acessar: ")
    print(f"O valor da chave '{chave}' é: {dados.get(chave)}")

except KeyError:
    print('Erro: Não é possivel acessar a chave passada')

