class Pais:
    def __init__(self,nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)
    def set_nome(self, nome):
        if nome =="": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def  set_populacao(self, populacao):
        if populacao <=0: raise ValueError("Número de pessoas deve ser positivo")
        self.__populacao = populacao
    def set_area (self, area):
        if area <=0: raise ValueError ("Area deve ser positiva")
        self.__area = area
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def desidade(self):
        return self.__area/ self.__populacao
    def __str__(self):
        return f"Densidade de {self.__nome}, é de: {self.__densidade}"
    
class PaisUI:
    @staticmethod
    def main():
        op = 0
        while op !=9:
            op = PaisUI.menu()
            if op ==1: PaisUI.calculo()
    @staticmethod
    def menu():
        print("1-Desnidade, 9- Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def calculo():
        nome = input("Digite o nome: ")
        populacao = float(input("Informe o número de moradores: "))
        area = float(input("Informe a área em KM quadradros: "))
        x = Pais(nome, populacao, area)
        print(x)
        print(f"A densidade demografica nessa cidade é de {x.densidade()}")

PaisUI.main()