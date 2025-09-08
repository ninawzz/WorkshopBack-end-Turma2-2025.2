def validar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
        return idade
    except ValueError:
        print("A idade deve estar entre 0 e 120 anos!")
        return 0
while True:
    idade = validar_idade()
    if idade <= 0 or idade > 120:
        continue
    else:
        print(f"Idade válida: {idade}")
        break