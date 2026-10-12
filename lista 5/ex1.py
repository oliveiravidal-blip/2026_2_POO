from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
        
    def set_nome (self, nome):
        if nome =="": raise ValueError ("O nome do paciente não pode ser vazio")
        self.__nome = nome
    def set_cpf (self, cpf):
        if cpf =="": raise ValueError ("O CPF do paciente não pode ser vazio")
        self.__cpf = cpf
    def set_telefone (self, telefone):
        if telefone =="": raise ValueError ("Informe o telefone do paciente corretamente")
        self.__telefone = telefone   
    def set_nascimento (self, nascimento_str):
        try:
            self.__nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")        
        except ValueError:
            raise ValueError("Data de nascimnto inválida! Use o formato  DD/MM/AAAA")
            
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento
    
    def __str__(self):
        data = self.__nascimento.strftime("%d/%m/%Y")
        return f"O paciente {self.__nome}, cadastrado no CPF {self.__cpf} e nascido na data: {data}, tem o responsável que pode ser contatado através do número: {self.__telefone}"
    
class UI:
    pacientes = []    
    @staticmethod
    def main():
        op = UI.menu()
        while op !=9:
            if op == 1: UI.inserir()
            elif op == 2: UI.listar_pacientes()
            elif op == 3: UI.listar_nascimento()
            op = UI.menu()
    @staticmethod
    def menu():
        print ("1-Inserir paciente, 2- Listar pacientes por nome, 3 - listar pacientes por data de nascimento, 9 - Fim")
        return int(input("Selecione uma opção: "))
    @classmethod
    def inserir(cls):
        try:
            nome = input("Informe o nome: ")
            cpf = input("Informe o CPF: ")
            telefone = input("Informe o telefone: ")
            nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")

            paciente = Paciente(nome, cpf, telefone, nascimento)
            cls.pacientes.append(paciente)
            print("Paciente cadastrado com sucesso!")
        except ValueError as erro:
            print(f"Erro ao cadastrar: {erro}")
    @classmethod
    def listar_pacientes(cls):
        if not cls.pacientes:
            print("Nenhum paciente cadastrado.")
            return

        cls.pacientes.sort(key=lambda x: x.get_nome().lower())
        for p in cls.pacientes:
            print(p)

    @classmethod
    def listar_nascimento(cls):
        if not cls.pacientes:
            print("Nenhum paciente cadastrado.")
            return

        cls.pacientes.sort(key=lambda x: x.get_nascimento())
        for p in cls.pacientes:
            print(p)  
    
    


UI.main()