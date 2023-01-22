def maiusculas(frases):
    letras_maiusculas = ''
    tam = len(frases)
    for i in range(tam):
        if (ord(frases[i]) > 64 and ord(frases[i]) < 91):
            letras_maiusculas += frases[i] 
    return letras_maiusculas
