class Triangulo:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def perimetro(self):
        perimetro_triangulo = (self.a + self.b + self.c)
        return perimetro_triangulo

