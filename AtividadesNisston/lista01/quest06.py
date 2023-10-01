num = int(input("Digite um número inteiro positivo: "))

contador = 1
resultado = 1

while contador < num:
    resultado *= contador
    contador += 1

print(f"O fatorial de {num} é {resultado}")