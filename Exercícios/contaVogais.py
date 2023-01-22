def conta_letras(frase, contar='vogais'):
    tam = len(frase)


    if contar == 'vogais':
        vogais = ['a', 'e', 'i', 'o', 'u']
        n_vogais = 0
        for i in range(tam):
            if frase[i].lower() in vogais:
                n_vogais += 1
        return n_vogais

    if contar == 'consoantes':
        consoantes = ['b', 'c', ' d', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
        n_consoantes = 0
        for i in range(tam):
            if frase[i].lower() in consoantes:
                n_consoantes += 1
        return n_consoantes
    
    
