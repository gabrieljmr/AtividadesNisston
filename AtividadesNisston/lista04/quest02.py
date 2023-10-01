def ordenar_vetor(vetor, crescente=True):

    if crescente:
        return sorted(vetor)
    else:
        return sorted(vetor, reverse=True)

vetor = [64, 25, 12, 22, 11]

vetor_crescente = ordenar_vetor(vetor, crescente=True)
print("Vetor ordenado em ordem crescente:", vetor_crescente)

vetor_decrescente = ordenar_vetor(vetor, crescente=False)
print("Vetor ordenado em ordem decrescente:", vetor_decrescente)