from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.categoria import Categoria
from models.categoriadao import CategoriaDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)        
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        CategoriaDAO().inserir(c)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO().atualizar(c)

    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO().excluir(id)