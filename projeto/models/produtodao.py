import json
from models.produto import Produto

class ProdutoDAO:
    
    def __init__(self):
        self.__arquivo = "produtos.json"
        self.__objetos = []
        
    def inserir (self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) !=0:
            id = max(self.__objetos, key = lambda x: x.get_id()).get_id()
        obj.set_id(id+1)
        self.__objetos.append(obj)
        self.__salvar()
    
    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None
    
    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux is not None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux is not None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        self.__objetos = []
        try:
            with open(self.__arquivo, mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    self.__objetos.append(Produto.from_json(obj))
        except FileNotFoundError:
            pass

    def __salvar(self):
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(self.__objetos, arquivo, default=Produto.to_json, indent=2)
            