def ordenada(lista):
    ultima_posicao = len(lista)
    for i in range(ultima_posicao - 1):
        for j in range(i+1,ultima_posicao):
            if lista[i] > lista[j]:
                return False
    return True


