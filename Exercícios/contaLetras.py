class Triangulo:

    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
        
        

    def perimetro():
        return self.a + self.b + self.c


def main():

    t = Triangulo(1,1,1)
    print(t.a)
    print(t.b)
    print(t.c)

    t.perimetro()
    
