class Equacao:
    def __init__(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
    def set_a(self, a):
        if a == 0:
            raise ValueError("O a não pode ser zero")
        self.__a = a
    def get_a(self):
        return self.__a
    def set_b(self, b):
        self.__b = b
    def get_b(self):
        return self.__b
    def set_c(self, c):
        self.__c = c
    def get_c(self):
        return self.__c
    def Delta(self):
        return self.__b**2-4*self.__a*self.__c
    def TemRaizesReais(self):
        if self.Delta() < 0:
            return False
        else:
            return True
    def Raiz1(self):
        return (-self.__b+(self.Delta())**(1/2))/(2*self.__a)
    def Raiz2(self):
        return (-self.__b-(self.Delta())**(1/2))/(2*self.__a)
class UI:
    def menu():
        return int(input("1 - Calcular, 2 - Fim\nInforme o número: "))
    def main():
        while UI.menu() != 2:
            UI.calcular()
    def calcular():
        a = int(input("Informe o valor de a: "))
        b = int(input("Informe o valor de b: "))
        c = int(input("Informe o valor de c: "))
        e = Equacao(a, b, c)
        if e.TemRaizesReais() == True:
            print(f"As raízes da equação {e.get_a()}x² + {e.get_b()}x + {e.get_c()} são {e.Raiz1():.2f} e {e.Raiz2():.2f}")
        else:
            print("Essa equação não tem raízes reais.")
UI.main()
    