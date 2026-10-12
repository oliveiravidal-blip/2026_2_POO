import enum
from datetime import datetime, timedelta

class SituacaoEstagio(enum.Enum):
    Cadastrado = 1
    Iniciado = 2
    Cancelado = 3
    Finalizado = 4

class Estagio:  # Entidade
    def __init__(self, est, emp):
        self.set_estagiario(est)     # Atributos
        self.set_empresa(emp)
        self.__data_inicio = None
        self.__data_cancelamento = None
        self.__data_fim = None
        self.__situacao = SituacaoEstagio.Cadastrado

    def set_estagiario(self, est):   # Métodos
        if est == "": raise ValueError("Estagiário deve ser informado")
        self.__estagiario = est
    def set_empresa(self, emp):
        if emp == "": raise ValueError("Empresa deve ser informada")
        self.__empresa = emp
    def get_estagiario(self): return self.__estagiario
    def get_empresa(self): return self.__empresa
    def situacao(self): return self.__situacao

    def iniciar(self, data):
        if self.__situacao != SituacaoEstagio.Cadastrado: raise ValueError("Só é possível iniciar um estágio cadastrado")
        self.__data_inicio = data
        self.__situacao = SituacaoEstagio.Iniciado

    def cancelar(self, data):
        if self.__situacao != SituacaoEstagio.Iniciado: raise ValueError("Só é possível cancelar um estágio iniciado")
        self.__data_cancelamento = data
        self.__situacao = SituacaoEstagio.Cancelado

    def finalizar(self, data):
        if self.__situacao != SituacaoEstagio.Iniciado: raise ValueError("Só é possível finalizar um estágio iniciado")
        self.__data_fim = data
        self.__situacao = SituacaoEstagio.Finalizado   

    def tempo_estagio(self):
        if self.__situacao == SituacaoEstagio.Cadastrado: return timedelta()
        if self.__situacao == SituacaoEstagio.Iniciado: return datetime.now().date() - self.__data_inicio.date()
        if self.__situacao == SituacaoEstagio.Cancelado: return self.__data_cancelamento - self.__data_inicio
        return self.__data_fim - self.__data_inicio
    
    def __str__(self):
        s = f"{self.__estagiario} - {self.__empresa} - "
        if self.__situacao == SituacaoEstagio.Cadastrado: 
            return s + "aguandando início"
        if self.__situacao == SituacaoEstagio.Iniciado: 
            return s + f"iniciado em {self.__data_inicio.strftime('%d/%m/%Y')}"
        if self.__situacao == SituacaoEstagio.Cancelado: 
            return s + f"cancelado em {self.__data_cancelamento.strftime('%d/%m/%Y')}"
        return s + f"realizado no período de {self.__data_inicio.strftime('%d/%m/%Y')} a {self.__data_fim.strftime('%d/%m/%Y')}"

class UI:
    estagios = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar_empresa()
            if op == 3: UI.listar_estagiario()
            if op == 4: UI.filtrar_situacao()
            if op == 5: UI.iniciar_estagio()
            if op == 6: UI.cancelar_estagio()
            if op == 7: UI.finalizar_estagio()
    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar por empresa, 3 - Listar por estagiário, 4 - Filtrar situação, 5 - Iniciar estágio, 6 - Cancelar estágio, 7 - Finalizar estágio, 9 - Fim")
        return int(input("Informe a opção: "))
    @classmethod
    def inserir(cls):
        estagiario = input("Informe o nome do estagiário: ")
        empresa = input("Informe o nome da empresa: ")
        x = Estagio(estagiario, empresa)
        cls.estagios.append(x)
    @classmethod
    def listar_empresa(cls):
        cls.estagios.sort(key = lambda x : x.get_empresa() + x.get_estagiario() )
        for x in cls.estagios:
            print(x)
    @classmethod
    def listar_estagiario(cls):
        cls.estagios.sort(key = lambda x : x.get_estagiario() )
        for x in cls.estagios:
            print(x)
    @classmethod
    def filtrar_situacao(cls):
        op = int(input("Informe a situação: 1 - Cadastrado, 2 - Iniciado, 3 - Cancelado, 4 - Finalizado: "))
        r = []
        for x in cls.estagios:
            if x.situacao() == SituacaoEstagio(op): r.append(x)
        for x in r:
            print(x)
    @classmethod
    def iniciar_estagio(cls):
        for i, x in enumerate(cls.estagios):
            if x.situacao() == SituacaoEstagio.Cadastrado: print(i, ":", x)
        op = int(input("Informe o número do estágio para iniciar: "))
        cls.estagios[op].iniciar(datetime.now())    
    @classmethod
    def cancelar_estagio(cls):
        for i, x in enumerate(cls.estagios):
            if x.situacao() == SituacaoEstagio.Iniciado: print(i, ":", x)
        op = int(input("Informe o número do estágio para cancelar: "))
        cls.estagios[op].cancelar(datetime.now())  
    @classmethod
    def finalizar_estagio(cls):
        for i, x in enumerate(cls.estagios):
            if x.situacao() == SituacaoEstagio.Iniciado: print(i, ":", x)
        op = int(input("Informe o número do estágio para finalizar: "))
        cls.estagios[op].finalizar(datetime.now())  
UI.main()