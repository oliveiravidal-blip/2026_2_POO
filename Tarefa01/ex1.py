class Viagem:
    def __init__(self, dest, dist, lt):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)
    def set_destino(self, dest):
        if dest == "": raise ValueError("Destino deve ser informado")
        self.__destino = dest        
    def set_distancia(self, dist):
        if dist <= 0: raise ValueError("Distância deve ser positiva")
        self.__distancia = dist
    def set_litros(self, lt):
        if lt <= 0: raise ValueError("Litros deve ser positivo")
        self.__litros = lt
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros 
    def __str__(self):
        return f"Destino = {self.__destino}, distância = {self.__distancia} km, litros = {self.__litros} l"

class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
    @staticmethod
    def menu():
        print("1-Viagem, 9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def calculo():
        dest = input("Informe o destino da viagem: ")
        dist = float(input("Informe a distância em km: "))
        lt = float(input("Informe a quantidade de combustível usada em litros: "))
        x = Viagem(dest, dist, lt)
        print(x)
        print(f"Seu consumo médio foi de {x.consumo()} km/l")        

ViagemUI.main()