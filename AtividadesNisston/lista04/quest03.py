def encontrar_maximo(vetor):
    if not vetor:
        return None  

    maximo = vetor[0]  

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

    return maximo

def encontrar_minimo(vetor):
    if not vetor:
        return None  

    minimo = vetor[0]  

    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return minimo

vetor = [64, 25, 12, 22, 11]

maximo = encontrar_maximo(vetor)
minimo = encontrar_minimo(vetor)

print("Elemento máximo:", maximo)
print("Elemento mínimo:", minimo)