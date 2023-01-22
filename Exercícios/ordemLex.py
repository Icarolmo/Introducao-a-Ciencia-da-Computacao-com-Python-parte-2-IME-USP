def primeiro_lex(lista):

    devolva = lista[0]
    tam = len(lista)
    for i in range(tam):
        if lista[i] < devolva:
            devolva = lista[i]
    return devolva
        
