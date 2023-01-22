def n_primos(x):
    primos = 0
    while(x >= 2):
        auxiliar = x // 2 
        while(auxiliar > 1):
            if(x % auxiliar == 0):
                auxiliar = 0
            else:
                auxiliar -=1
        if(auxiliar == 1):
            primos += 1
        x -=1
    return primos

