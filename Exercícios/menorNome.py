
def menor_nome(nomes):
    menor_nome = nomes[0]
    for nome in nomes:
              if len(nome.strip()) < len(menor_nome.strip()):
                  menor_nome = nome
    return menor_nome.strip().capitalize() 
            
