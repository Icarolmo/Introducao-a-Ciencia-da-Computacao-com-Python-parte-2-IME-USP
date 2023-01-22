def preenche_linha(x):
    while(x > 0):
        print('#',end = '')
        x -=1

def preenche_bordas(y):
    auxiliar = y
    while(y > 0):
        if(y == auxiliar or y == 1):
            print('#',end = '')
        else:
            print(end = ' ')
        y -=1
    
            
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
verifica = altura 
while(altura > 0):
    if(altura == verifica or altura == 1):
        preenche_linha(largura)
    else:
        preenche_bordas(largura)
    print()
    altura -=1
            
        
            


