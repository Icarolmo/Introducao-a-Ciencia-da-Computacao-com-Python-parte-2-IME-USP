class Triangulo:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def perimetro(self):
        perimetro_triangulo = (self.a + self.b + self.c)
        return perimetro_triangulo

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        if (self.a ** 2) + (self.b ** 2) == (self.c ** 2):
            return True
        else:
            return False

    def semelhantes(self,triangulo):
        tri_a = []
        tri_a.append(self.a)
        tri_a.append(self.b)
        tri_a.append(self.c)
        tri_a.sort()
        tri_b = []
        tri_b.append(triangulo.a)
        tri_b.append(triangulo.b)
        tri_b.append(triangulo.c)
        tri_b.sort()
        for i in range(3):
            if tri_b[i] % tri_a[i] != 0:
                return False
        return True







