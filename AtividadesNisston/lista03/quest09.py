def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero."
    return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite o número da operação desejada: ")

escolha = int(escolha)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if escolha == 1:
    resultado = somar(numero1, numero2)
    operacao = "adição"
elif escolha == 2:
    resultado = subtrair(numero1, numero2)
    operacao = "subtração"
elif escolha == 3:
    resultado = multiplicar(numero1, numero2)
    operacao = "multiplicação"
elif escolha == 4:
    resultado = dividir(numero1, numero2)
    operacao = "divisão"
else:
    print("Escolha inválida. Por favor, digite um número de 1 a 4 para escolher a operação.")

if isinstance(resultado, (int, float)):
    print(f"O resultado da {operacao} é: {resultado:.2f}")
else:
    print(resultado)