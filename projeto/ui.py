from service import Service

class UI:
    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
            if op == 5: UI.inserir_categoria()
            if op == 6: UI.listar_categoria()
            if op == 7: UI.atualizar_categoria()
            if op == 8: UI.excluir_categoria()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.produto_reajustar()
    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Inserir Categoria, 6 - Listar Categorias, 7 - Atualizar Categoria, 8 - Excluir Categoria, 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir, 13 - Reajustar Preços, 0 - Fim")
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
    @staticmethod
    def produto_inserir():
        desc = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID da categoria do produto: "))  
        Service.produto_inserir(desc, preco, estoque, id_categoria)
        print("Produto cadastrado com sucesso!")
    @staticmethod
    def produto_listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(p)
    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o ID do produto a ser atualizado: "))
        
        desc = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        
        UI.categoria_listar()
        id_categoria = int(input("Informe o novo ID da categoria: "))
        
        Service.produto_atualizar(id, desc, preco, estoque, id_categoria)
        print("Produto atualizado com sucesso!")
    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o ID do produto a ser excluído: "))
        Service.produto_excluir(id)
        print("Produto excluído com sucesso!")
    @staticmethod
    def produto_reajustar():
        percentual = float(input("Informe o percentual de reajuste (ex: 10 para +10%, -5 para -5%): "))
        Service.produto_reajustar(percentual)
        print("Preços de todos os produtos reajustados com sucesso!")
UI.main()