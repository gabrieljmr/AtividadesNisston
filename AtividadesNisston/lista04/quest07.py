def terceiro_maior(vetor): 
    conjunto_sem_duplicatas = set(vetor)   
    lista_ordenada = sorted(list(conjunto_sem_duplicatas), reverse=True)   
    if len(lista_ordenada) >= 3:
        return lista_ordenada[2] 
    else:
        return "Não há terceiro maior número no vetor."


vetor = [64, 25, 12, 22, 11, 25]

resultado = terceiro_maior(vetor)

print("Terceiro maior número:", resultado)