class Viagem:
    def __init__(self, destino, distancia, combustivel):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_combustivel(combustivel)
    def set_destino(self, destino):
        if destino == "":
            raise ValueError("Não pode ser vazio")
        self.__destino = destino
    def get_destino(self):
        return self.__destino
    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError("A distância precisa ser maior que zero")
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    def set_combustivel(self, combustivel):
        if combustivel < 0:
            raise ValueError("O combustível precisa ser maior que zero")
        self.__combustivel = combustivel
    def get_combustivel(self):
        return self.__combustivel
    def consumo(self):
        return self.__distancia/self.__combustivel
class UI:
    def menu():
        return int(input(f"1 – Calcular, 2 – Fim\nInforme a opção: "))
    def main():
        while UI.menu() != 2:
            UI.calculo()
    def calculo():
        destino = input("Informe o destino da viagem: ")
        distancia = float(input("Informe a distância da viagem em km: "))
        combustivel = float(input("Informe a quantidade de combustível utilizada na viagem em litros: "))
        trip = Viagem()
        print(f"Você quer ir para {trip.get_destino()}, que fica a {trip.get_distancia()}km e gasta {trip.get_combustivel()}l de combustível.")
        print(f"O consumo médio dessa viagem é de {trip.consumo():.2f}km/l")
UI.main()