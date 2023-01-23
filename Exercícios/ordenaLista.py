def ordena(lista):
    ultima_posicao = len(lista)
    for i in range(ultima_posicao - 1):
        menor_elemento = i
        for j in range(i+1,ultima_posicao):
            if lista[menor_elemento] > lista[j]:
                menor_elemento = j
        lista[i], lista[menor_elemento] = lista[menor_elemento], lista[i]
    
    return lista


