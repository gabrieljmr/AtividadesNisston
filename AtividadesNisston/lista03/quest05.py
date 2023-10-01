def e_primo(numero):  
    if numero <= 1:
        return False   
    if numero == 2:
        return True 
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro para verificar se é primo: "))

if e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")