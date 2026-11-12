from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
            if op == 5: UI.inserir_categoria()
            if op == 6: UI.listar_categoria()
            if op == 7: UI.atualizar_categoria()
            if op == 8: UI.excluir_categoria()
    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Inserir Categoria, 6 - Listar Categorias, 7 - Atualizar Categoria, 8 - Excluir Categoria, 9 - Fim")
        return int(input("Informe a opção: "))
    @staticmethod
    def inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        Service.cliente_inserir(nome, email, fone)
    @staticmethod
    def listar():
        for c in Service.cliente_listar():
            print(c)
    @staticmethod
    def atualizar():
        UI.listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        Service.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def excluir():            
        UI.listar()
        id = int(input("Informe o id a ser excluído: "))
        Service.cliente_excluir(id)        
        
    @staticmethod
    def categoria_inserir():
        desc = input("Informe a descrição da categoria: ")
        Service.categoria_inserir(desc)
        print("Categoria cadastrada com sucesso!")

    @staticmethod
    def categoria_listar():
        for c in Service.categoria_listar():
            print(c)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o ID da categoria a ser atualizada: "))
        desc = input("Informe a nova descrição: ")
        Service.categoria_atualizar(id, desc)

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o ID da categoria a ser excluída: "))
        Service.categoria_excluir(id)
        
UI.main()