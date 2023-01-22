import pytest

def busca (lista, elemento, min = 0 , max = None):

    if max == None:
        max = len(lista)-1
    
    if max < min:
        return False
    else:
        mediana = (max-min) + min // 2
        
    if elemento < lista[mediana]:
        return busca(lista, elemento, min, mediana-1)
    elif elemento > lista[mediana]:
        return busca(lista, elemento, mediana+1, max)
    else:
        return mediana
    

vetor = [1,2,3,4,5,10,15,35,75,100,125,200,500]


@pytest.mark.parametrize("lista, valor, esperado",[
    (vetor, 1, 0),
    (vetor, 35, 7),
    (vetor, 2, 1),
    (vetor, 500, 12),
    (vetor, 200, 11),
    (vetor, 4, 3),
    (vetor, 100, 9),
    (vetor, 1000, False),
    (vetor, -10, False),
    (vetor, 0, False)
    ])

def teste_busca(lista, valor, esperado):
    assert busca(lista, valor) == esperado




            
