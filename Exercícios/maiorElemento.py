def maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior
