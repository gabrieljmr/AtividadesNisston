def celsius_para_fahrenheit(celsius):  
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):  
    return (fahrenheit - 32) * 5/9

escolha = input("Escolha a conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\nDigite o número da opção: ")

escolha = int(escolha)

if escolha == 1:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius são {fahrenheit:.2f} graus Fahrenheit.")
elif escolha == 2:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit são {celsius:.2f} graus Celsius.")
else:
    print("Escolha inválida. Por favor, digite 1 ou 2 para escolher a conversão desejada.")