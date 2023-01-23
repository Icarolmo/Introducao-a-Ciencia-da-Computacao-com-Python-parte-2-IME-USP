def busca(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        particao = (inicio + fim) // 2
        if elemento == lista[particao]:
            print(particao)
            return particao
        else:
            if elemento < lista[particao]:
                print(particao)
                fim = particao - 1
                
            else:
                print(particao)
                inicio = particao + 1
    return False
