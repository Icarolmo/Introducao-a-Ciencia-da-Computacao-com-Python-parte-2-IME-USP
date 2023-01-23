def inverte_lista(lista):
    auxiliar = lista[:]
    elemento = -1
    for troca in lista:
        auxiliar[elemento] = troca
        elemento -= 1
    return auxiliar
        
def main():
    vetor = []
    numero = int(input('Insira um número: '))
    while(numero != 0):
        vetor.append(numero)
        numero = int(input('Insira um número: '))
    vetor = inverte_lista(vetor)
    for numeros in vetor:
        print(numeros)
        
        
        
main()
   
    
    
    