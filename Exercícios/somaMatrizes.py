def dimensoes(matriz):
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    return [(n_linhas ), (n_colunas)]
    
def soma_matrizes(m1, m2):
    dim_m1 = dimensoes(m1)
    dim_m2 = dimensoes(m2)
    if (dim_m1 != dim_m2):
        return False
    else:
        matriz = []
        n_linhas = len(m1)
        n_colunas = len(m1[0])
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                linha.append(m1[i][j] + m2[i][j])
            matriz.append(linha)

        return matriz
        

                
        
