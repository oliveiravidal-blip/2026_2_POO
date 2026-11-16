class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)
        
    def set_id(self, id):
        self.__id = id
        
    def get_id(self):
        return self.__id
    
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Descrição não pode ser vazia")
        self.__descricao = descricao

    def get_descricao(self):
        return self.__descricao

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao
        }

    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"])

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"