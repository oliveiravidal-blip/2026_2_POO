import json
from models.cliente import Cliente

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.get_id()).get_id()
        obj.set_id(id + 1)    
        self.__objetos.append(obj)
        self.__salvar()
    def listar(self):
        self.__abrir()
        return self.__objetos
    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None
    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()
    
    def __abrir(self):
        self.__objetos = []
        try:
            arquivo = open(self.__arquivo, mode="r")
            objetos_json = json.load(arquivo)
            for obj in objetos_json:
                self.__objetos.append(Cliente.from_json(obj))
            arquivo.close()
        except FileNotFoundError: ("erro")
    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()