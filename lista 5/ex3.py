import enum
from datetime import datetime, timedelta
class Turno(enum.Enum):
    Matutino = 1
    Vespertino = 2
    Noturno = 3   
class Cargo(enum.Enum):
    estagiario = 1
    analista = 2
    gerente = 3
    diretor = 4   
class Funcionario:
    def __init__(self, nome, matricula, salario, turno, cargo, data_a):
        self.set_nome(nome)
        self.set_matricula(matricula)
        self.set_salario(salario)
        self.set_turno(turno)
        self.set_cargo(cargo)
        self.set_data_a(data_a)      
    def set_nome(self,nome):
        if nome =="": raise ValueError ("Preencha o nome do funcionário.")
        self.__nome = nome
    def set_matricula(self,matricula):
        if matricula =="": raise ValueError ("Preencha a matricula do funcionário.")
        self.__matricula = matricula
    def set_salario(self,salario):
        if salario <=0: raise ValueError ("O salário do funcionário não pode ser negativo.")
        self.__salario = salario
    def set_turno(self, turno):
        if not isinstance(turno, Turno):
            raise ValueError("Turno inválido!")
        self.__turno = turno
    def set_cargo(self, cargo):
        if not isinstance (cargo, Cargo):
            raise ValueError("Cargo inválido")
        self.__cargo = cargo
    def set_data_a(self, data_str):
        try:
            self.__data_a = datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de admissão inválida! Use o formato DD/MM/AAAA.")      
    def tempo_trabalho(self):
        hoje = datetime.now()
        diferenca = hoje - self.__data_a
        return f"{diferenca.days} dias"
    def promover(self):
        atual = self.__cargo.value
        if self.__cargo ==Cargo.diretor: raise ValueError("Funcionário já está no cargo máximo da empresa.")
        else:
            self.set_cargo(Cargo(atual+1))
            self.set_salario(self.__salario * 1.25)
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def get_salario(self):
        return self.__salario
    def get_turno(self):
        return self.__turno
    def get_cargo(self):
        return self.__cargo
    def get_data_a(self):
        return self.__data_a   
    def __str__(self):
        data = self.__data_a.strftime("%d/%m/%Y")
        return f"O funcionário {self.__nome}, cadastrado na matrícula {self.__matricula} e admitido na data: {data}, tem o cargo {self.__cargo}, trabalha no turno: {self.__turno} e possui o salário {self.__salario}"    
class UI:
    funcionarios = []
    @staticmethod
    def main ():
        op = UI.menu()
        while op !=9:
            if op == 1: UI.inserir()
            elif op == 2 : UI.listar_turno()
            elif op == 3: UI.listar_cargo()
            elif op == 4: UI.promover()
            op = UI.menu()          
    @staticmethod
    def menu ():
        print("1 - Inserir, 2 - Listar por turno, 3 - Listar por cargo, 4- Promover, 9 - Fim")
        return int(input("Informe a opção: "))   
    @classmethod
    def inserir(cls):
        try:
            nome = input("Informe o nome: ")
            matricula = input("Informe a matrícula: ")
            salario = float(input("Informe o salário: "))

            print("Turnos disponíveis: 1 - Matutino | 2 - Vespertino | 3 - Noturno")
            opcao_turno = int(input("Informe o número do turno: "))
            turno = Turno(opcao_turno)
            print("Cargos disponíveis: 1 - Estagiário | 2 - Analista | 3 - Gerente | 4 - Diretor")
            opcao_cargo = int(input("Informe o número do cargo: "))
            cargo = Cargo(opcao_cargo)
            data_a = input("Informe a data de admissão (DD/MM/AAAA): ")
            funcionario = Funcionario(nome, matricula, salario, turno, cargo, data_a)   
            cls.funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!")
        except ValueError as erro:
            print(f"Erro ao cadastrar: {erro}")
    @classmethod
    def listar_turno (cls):
        if not cls.funcionarios:
                print("Nenhum funcionário cadastrado.")
                return
    
        cls.funcionarios.sort(key=lambda x: x.get_turno().value)
        for p in cls.funcionarios:
            print(p)
    @classmethod
    def listar_cargo (cls):
        if not cls.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return

        cls.funcionarios.sort(key=lambda x: x.get_cargo().value)
        for p in cls.funcionarios:
            print(p)         
    @classmethod
    def promover(cls):
        if not cls.funcionarios:
            print("Nenhum funcionário cadastrado.\n")
            return

        matricula = input("Informe a matrícula do funcionário que deseja promover: ")

        funcionario_encontrado = None
        for f in cls.funcionarios:
            if f.get_matricula() == matricula:
                funcionario_encontrado = f
                break

        if funcionario_encontrado:
            try:
                funcionario_encontrado.promover()
                print(f"Funcionário promovido com sucesso! Novo cargo: {funcionario_encontrado.get_cargo().name} | Novo salário: R$ {funcionario_encontrado.get_salario():.2f}")
            except ValueError as erro:
                print(f"Erro ao promover: {erro}")
        else:
            print("Funcionário não encontrado.")


UI.main()