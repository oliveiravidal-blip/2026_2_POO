class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)
        
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
    
    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("O estoque do produto não pode ser negaivo.")
        self.__estoque = estoque
        
    def get_estoque(self):
        return self.__estoque

    def set_preco(self, preco):
        if preco <= 0:
            raise ValueError("Valor não pode ser de R$00,00")
        self.__preco = preco
        
    def get_preco(self):
        return self.__preco
    
    def set_id_categoria(self, id_categoria):
        if id_categoria <= 0:
            raise ValueError("ID da categoria deve ser válido/positivo")
        self.__id_categoria = id_categoria
        
    def get_id_categoria(self):
        return self.__id_categoria
    
    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "id_categoria": self.__id_categoria
        }
    
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["id_categoria"])
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__id_categoria} - {self.__preco} - {self.__estoque}"