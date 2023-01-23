def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas-1):
            print(matriz[i][j], end = ' ')
        print(matriz[i][colunas-1])
        
        
    
        
    

                
        
