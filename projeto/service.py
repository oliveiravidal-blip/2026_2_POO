from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.categoria import Categoria
from models.categoriadao import CategoriaDAO
from models.produto import Produto
from models.produtodao import ProdutoDAO

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
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        p = Produto(0, descricao, preco, estoque, id_categoria)
        ProdutoDAO().inserir(p)
    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()
    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        p = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().atualizar(p)
    @staticmethod
    def produto_excluir(id):
        ProdutoDAO().excluir(id)
    @staticmethod
    def produto_reajustar(percentual):
        ProdutoDAO().reajustar(percentual)