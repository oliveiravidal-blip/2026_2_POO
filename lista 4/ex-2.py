class Cliente:
    def __init__(self, nome, cpf, limite):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_limite(limite)
        self.__socio = None
    def set_nome(self,nome):
        if nome =="":
            raise ValueError("Digite o nome")
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf =="":
            raise ValueError("Digite o CPF")
        self.__cpf = cpf
    def set_limite(self, limite):
        if limite <= 0:
            raise ValueError("Limite deve ser positivo")
        self.__limite = limite
    def set_socio(self, socio):
        if self.__socio == None:
            self.__socio = socio
        else:
            self.__socio.__socio = None
            self.__socio = socio
        if socio.__socio != None:
            socio.__socio.__socio = None
        socio.__socio = self
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_limite(self):
        if self.__socio == None:
            return self.__limite
        return self.__limite + self.__socio.__limite
    def get_socio(self):
        return self.__socio
    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Limite: {self.__limite}"

class Empresa:
    def __init__(self, nome):
        self.set_nome(nome)
        self.__clientes =[]
    def set_nome(self, nome):
       if nome =="": raise ValueError("Digite o nome")
       self.__nome = nome
    def inserir(self, cliente):
        self.__clientes.append(cliente)
    def listar(self):
        return self.__clientes
    def __str__(self):
        return f"Nome: {self.__nome}, lista de clientes: {self.__clientes}"
    def get_nome(self):
        return self.__nome
    
class UI:
    empresas=[]
    @classmethod
    def main(cls):
        while True:
            op = cls.menu_empresas()
            if 1 == op:
                nome = input("Digite o nome: ")
                cls.empresas.append(Empresa(nome))
            elif 2 == op:
                break
            elif op - 3 < len(cls.empresas):
                while True:
                    emp = cls.empresas[op - 3]
                    opc = cls.menu_cliente(emp)
                    if opc == 1:
                        cls.inserir_cliente(emp)
                    elif 2 == opc:
                        break
                    elif opc -3 < len(emp.listar()):
                        cliente =emp.listar()[opc - 3]
                        opca = cls.associar(cliente, emp)
                        
                        
       
            
    @classmethod
    def menu_empresas(cls):
        print("1 - Inserir empresa")
        print("2 - Sair")
        for indice, empresa in enumerate(cls.empresas):
            print(f"{indice + 3} - {empresa.get_nome()}")
        return int(input("Digite a opção que você quer: "))

    @classmethod
    def menu_cliente(cls, empresa):
        print("1 - Inserir cliente")
        print("2 - Sair")
        for indice, cliente in enumerate(empresa.listar()):
                print(f"{indice + 3} - {cliente.get_nome()} {cliente.get_socio()}")
        return int(input("Digite a opção que você quer: "))
        
    @classmethod
    def inserir_cliente(cls, empresa):
        n = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        limite = float(input("Digite o limite: "))
        cliente = Cliente(n, cpf, limite)
        empresa.inserir(cliente)
        
    @classmethod
    def associar(cls, c1, empresa):
        for indice, c2 in enumerate(empresa.listar()):
            if c1.get_cpf() != c2.get_cpf():
                print(f"{indice + 1} - {c2.get_nome()}")
        a = int(input("Digite a opção que você quer: "))
        c1.set_socio(empresa.listar()[a-1])
    
        
UI.main()