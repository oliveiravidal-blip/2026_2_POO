import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID deve ser um inteiro positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("Email deve ser informado")
        self.__email = email

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Telefone deve ser informado")
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Fone: {self.__fone}"


class ClienteDAO:
    __objetos = []
       
    @classmethod
    def inserir(cls, obj):
        cls.abrir() 
        cls.__objetos.append(obj)
        cls.salvar()  

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c is not None:
            c.set_nome(obj.get_nome())
            c.set_email(obj.get_email())
            c.set_fone(obj.get_fone())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.get_id())
        if c is not None:
            cls.__objetos.remove(c)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.__objetos.append(c)
        except FileNotFoundError:
            pass 

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            lista_dict = []
            for c in cls.__objetos:
                lista_dict.append({
                    "id": c.get_id(),
                    "nome": c.get_nome(),
                    "email": c.get_email(),
                    "fone": c.get_fone()
                })
            json.dump(lista_dict, arquivo, indent=4)
            
            
class ClienteUI:
    @classmethod
    def main(cls):
        op = 0
        while op != 9:
            op = cls.menu()
            if op == 1: cls.inserir()
            elif op == 2: cls.listar()
            elif op == 3: cls.pesquisar()
            elif op == 4: cls.atualizar()
            elif op == 5: cls.excluir()

    @classmethod
    def menu(cls):
        print("\n--- GESTÃO DE CLIENTES ---")
        print("1 - Inserir Cliente")
        print("2 - Listar Todos os Clientes")
        print("3 - Pesquisar Cliente por ID")
        print("4 - Atualizar Cliente")
        print("5 - Excluir Cliente")
        print("9 - Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @classmethod
    def inserir(cls):
        try:
            id = int(input("Informe o ID do cliente: "))
            nome = input("Informe o nome: ")
            email = input("Informe o e-mail: ")
            fone = input("Informe o telefone: ")
            
            c = Cliente(id, nome, email, fone)
            ClienteDAO.inserir(c)
            print("Cliente cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")

    @classmethod
    def listar(cls):
        clientes = ClienteDAO.listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n--- LISTA DE CLIENTES ---")
            for c in clientes:
                print(c)

    @classmethod
    def pesquisar(cls):
        try:
            id = int(input("Informe o ID do cliente procurado: "))
            c = ClienteDAO.listar_id(id)
            if c is not None:
                print(f"Cliente encontrado: {c}")
            else:
                print("Cliente não encontrado.")
        except ValueError:
            print("ID inválido.")

    @classmethod
    def atualizar(cls):
        try:
            id = int(input("Informe o ID do cliente a ser atualizado: "))
            c = ClienteDAO.listar_id(id)
            if c is not None:
                print(f"Cliente atual: {c}")
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo e-mail: ")
                fone = input("Informe o novo telefone: ")
                
                novo_c = Cliente(id, nome, email, fone)
                ClienteDAO.atualizar(novo_c)
                print("Cliente atualizado com sucesso!")
            else:
                print("Cliente não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")

    @classmethod
    def excluir(cls):
        try:
            id = int(input("Informe o ID do cliente a excluir: "))
            c = ClienteDAO.listar_id(id)
            if c is not None:
                ClienteDAO.excluir(c)
                print("Cliente excluído com sucesso!")
            else:
                print("Cliente não encontrado.")
        except ValueError:
            print("ID inválido.")


if __name__ == "__main__":
    ClienteUI.main()