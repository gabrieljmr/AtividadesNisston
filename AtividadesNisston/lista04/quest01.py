def ordenar_por_selecao(vetor):
    tamanho = len(vetor)

    for i in range(tamanho):      
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j       
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

vetor = [68, 95, 12, 34, 15]
ordenar_por_selecao(vetor)
print("Vetor ordenado:", vetor)