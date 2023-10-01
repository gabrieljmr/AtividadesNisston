def calcular_mediana(vetor):
    vetor_ordenado = sorted(vetor)    
    tamanho = len(vetor_ordenado)
    indice_do_meio = tamanho // 2   
    if tamanho % 2 == 1:    
        mediana = vetor_ordenado[indice_do_meio]
    else:      
        elemento1 = vetor_ordenado[indice_do_meio - 1]
        elemento2 = vetor_ordenado[indice_do_meio]
        mediana = (elemento1 + elemento2) / 2   
    return mediana

vetor = [64, 25, 12, 22, 11]

resultado = calcular_mediana(vetor)

print("Mediana:", resultado)