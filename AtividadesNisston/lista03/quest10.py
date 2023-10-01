def gerar_sequencia_fibonacci(numero_de_termos):
    termo1, termo2 = 0, 1

    if numero_de_termos <= 0:
        return "O número de termos deve ser maior que zero."  
    elif numero_de_termos == 1:
        return [termo1] 
    else:
        sequencia = [termo1, termo2]
        for _ in range(2, numero_de_termos):
            proximo_termo = termo1 + termo2
            sequencia.append(proximo_termo)
            termo1, termo2 = termo2, proximo_termo
        return sequencia

numero_de_termos = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

resultado = gerar_sequencia_fibonacci(numero_de_termos)

if isinstance(resultado, list):
    print(f"A sequência de Fibonacci com {numero_de_termos} termos é: {resultado}")
else:
 print(resultado)