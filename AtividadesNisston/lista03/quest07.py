def calcular_imc(peso, altura):

    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser valores positivos."   
    imc = peso / (altura ** 2)  
    return imc

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = calcular_imc(peso, altura)

if isinstance(imc, float):
    print(f"Seu IMC é: {imc:.2f}")
else:
    print(imc)