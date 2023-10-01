numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    soma = 0

    numero_str = str(numero)

    for digito in numero_str:
        soma += int(digito)

    print(f"A soma dos dígitos de {numero} é {soma}.")