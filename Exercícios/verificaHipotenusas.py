
def é_hipotenusa(x):
    hip = x**2
    while(x > 1):
        cat_ad = 1
        cat_op = x - 1
        while(cat_ad < cat_op):
            if( hip == ((cat_ad**2) + (cat_op**2))):
                return True
            cat_ad += 1
        x -= 1
    return False
            

def soma_hipotenusas(n):
    soma = 0
    while(n > 4):
        if(é_hipotenusa(n)):
            soma = soma + n
        n -=1
    return soma
    
