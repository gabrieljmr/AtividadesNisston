class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return area


ret = Retangulo(5, 6)

print(ret.calcular_area())