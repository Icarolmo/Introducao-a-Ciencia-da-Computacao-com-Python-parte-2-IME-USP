import random

def lista_grande(n):
    numeros = []
    for i in range(n):
        numeros.append(random.randint(0,1000))
    return numeros
