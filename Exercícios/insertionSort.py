def insertion_sort(lista):
    for i in range(len(lista)):
        j = i
        while(j > 0 and lista[j-1] > lista[j]):
            lista [j],lista[j-1] = lista[j-1],lista[j]
            j -= 1
    return lista        
        
