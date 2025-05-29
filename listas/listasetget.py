class Retangulo:
    def __init__(self, b, h):
        self.set_b(b)
        self.set_h(h)
    def set_b(self, b):
        if b < 0: raise ValueError("A base não pode ser negativa.")
        self.__b = b
    def get_b(self):
        return self.__b
    def set_h(self, h):
        if h < 0: raise ValueError("A altura não pode ser negativa.")
        self.__h = h
    def get_h(self):
        return self.__h
    def CalcArea(self):
        return self.__b*self.__h
    def CalcDiagonal(self):
        return (self.__b**2+self.__h**2)**(1/2)
    def __str__(self):
        return f'A base do retângulo é {self.__b} e a altura é {self.__h}.'
r = Retangulo(int(input("Informe o valor da base: ")), int(input("Informe o valor da altura: ")))
print(f'A área é {r.CalcArea()} e a diagonal é {r.CalcDiagonal():.2f}')
