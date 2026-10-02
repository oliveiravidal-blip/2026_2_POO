from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
        
    def set_id(self, id):
        if isinstance(id, int) and id <= 0:
            raise ValueError("O ID deve ser um número positivo")
        if id == "":
            raise ValueError("Informe o ID do usuário")
        self.__id = id

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("A data deve ser informada e ser válida")
        self.__data = data 

    def set_distancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva")
        self.__distancia = distancia

    def set_tempo(self, tempo):
        if not isinstance(tempo, timedelta) or tempo <= timedelta(0):
            raise ValueError("O tempo deve ser positivo")
        self.__tempo = tempo

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo
    
    def pace(self):
        return self.__tempo / self.__distancia
    
    def __str__(self):
        data_str = self.__data.strftime("%d/%m/%Y")
        return f"ID: {self.__id}, Data: {data_str}, Distância: {self.__distancia} KM, Tempo: {self.__tempo}, Pace: {self.pace()}"


class TreinoUI:
    __treinos = []
    
    @classmethod
    def main(cls):
        op = 0
        while op != 9:
            op = cls.menu()
            if op == 1: cls.inserir()
            elif op == 2: cls.listar()
            elif op == 3: cls.listar_id()
            elif op == 4: cls.atualizar()
            elif op == 5: cls.excluir()
            elif op == 6: cls.mais_rapido()

    @classmethod
    def menu(cls):
        print("\n--- MENU TREINOS ---")
        print("1 - Inserir")
        print("2 - Listar Todos")
        print("3 - Listar por ID")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Treino Mais Rápido")
        print("9 - Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @classmethod
    def inserir(cls):
        try:
            id = int(input("Informe o ID do treino: "))
            data_str = input("Informe a data (dd/mm/aaaa): ")
            data = datetime.strptime(data_str, "%d/%m/%Y")
            distancia = float(input("Informe a distância (km): "))
            h = int(input("Informe o tempo - Horas: "))
            m = int(input("Informe o tempo - Minutos: "))
            s = int(input("Informe o tempo - Segundos: "))
            tempo = timedelta(hours=h, minutes=m, seconds=s)

            treino = Treino(id, data, distancia, tempo)
            cls.__treinos.append(treino)
            print("Treino cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")

    @classmethod
    def listar(cls):
        if len(cls.__treinos) == 0:
            print("Nenhum treino cadastrado.")
        else:
            for t in cls.__treinos:
                print(t)

    @classmethod
    def listar_id(cls):
        try:
            id_busca = int(input("Informe o ID do treino procurado: "))
        except ValueError:
            print("ID inválido.")
            return

        for t in cls.__treinos:
            if t.get_id() == id_busca:
                print(t)
                return
        print("Treino não encontrado.")

    @classmethod
    def atualizar(cls):
        try:
            id_busca = int(input("Informe o ID do treino a ser atualizado: "))
        except ValueError:
            print("ID inválido.")
            return

        for t in cls.__treinos:
            if t.get_id() == id_busca:
                try:
                    dt_str = input("Nova data (dd/mm/aaaa): ")
                    dt = datetime.strptime(dt_str, "%d/%m/%Y")
                    ds = float(input("Nova distância (km): "))
                    h = int(input("Novas Horas: "))
                    m = int(input("Novos Minutos: "))
                    s = int(input("Novos Segundos: "))
                    t_delta = timedelta(hours=h, minutes=m, seconds=s)

                    t.set_data(dt)
                    t.set_distancia(ds)
                    t.set_tempo(t_delta)
                    print("Treino atualizado com sucesso!")
                    return
                except Exception as e:
                    print(f"Erro ao atualizar: {e}")
                    return
        print("Treino não encontrado.")

    @classmethod
    def excluir(cls):
        try:
            id_busca = int(input("Informe o ID do treino a excluir: "))
        except ValueError:
            print("ID inválido.")
            return

        for t in cls.__treinos:
            if t.get_id() == id_busca:
                cls.__treinos.remove(t)
                print("Treino removido com sucesso!")
                return
        print("Treino não encontrado.")

    @classmethod
    def mais_rapido(cls):
        if len(cls.__treinos) == 0:
            print("Nenhum treino cadastrado.")
        else:
            mais_rapido = min(cls.__treinos, key=lambda t: t.pace())
            print("--- TREINO MAIS RÁPIDO (MENOR PACE) ---")
            print(mais_rapido)

if __name__ == "__main__":
    TreinoUI.main()