from datetime import datetime, timedelta

class Musica:
    def __init__(self, id, t, art, alb, d):
        self.set_id(id)
        self.set_titulo(t)
        self.set_artista(art)
        self.set_album(alb)
        self.set_duracao(d)

    def set_id(self, id):
        if id <= 0: raise ValueError("ID deve ser positivo")
        self.__id = id

    def set_titulo(self, t):
        if t == "": raise ValueError("Título deve ser informado")
        self.__titulo = t

    def set_artista(self, art):
        if art == "": raise ValueError("Artista deve ser informado")
        self.__artista = art

    def set_album(self, alb):
        if alb == "": raise ValueError("Álbum deve ser informado")
        self.__album = alb

    def set_duracao(self, d):
        if not isinstance(d, timedelta) or d.total_seconds() <= 0:
            raise ValueError("Duração deve ser positiva")
        self.__duracao = d

    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def get_duracao(self): return self.__duracao

    def __str__(self):
        return f"ID: {self.__id} | Músico/Título: {self.__artista} - {self.__titulo} | Álbum: {self.__album} | Duração: {self.__duracao}"


class PlayList:
    def __init__(self, id, n, d):
        self.set_id(id)
        self.set_nome(n)
        self.set_descricao(d)

    def set_id(self, id):
        if id <= 0: raise ValueError("ID deve ser positivo")
        self.__id = id

    def set_nome(self, n):
        if n == "": raise ValueError("Nome da playlist deve ser informado")
        self.__nome = n

    def set_descricao(self, d):
        self.__descricao = d

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao

    def tempo_total(self, itens, musicas):
        total = timedelta()
        for item in itens:
            if item.get_id_playlist() == self.__id:
                for m in musicas:
                    if m.get_id() == item.get_id_musica():
                        total += m.get_duracao()
        return total

    def __str__(self):
        return f"ID: {self.__id} | Playlist: {self.__nome} | Descrição: {self.__descricao}"


class PlayListItem:
    def __init__(self, id, ip, im, dt, seq):
        self.set_id(id)
        self.set_id_playlist(ip)
        self.set_id_musica(im)
        self.set_data_inclusao(dt)
        self.set_sequencia(seq)

    def set_id(self, id):
        if id <= 0: raise ValueError("ID deve ser positivo")
        self.__id = id

    def set_id_playlist(self, ip):
        if ip <= 0: raise ValueError("ID da playlist inválido")
        self.__id_playlist = ip

    def set_id_musica(self, im):
        if im <= 0: raise ValueError("ID da música inválido")
        self.__id_musica = im

    def set_data_inclusao(self, dt):
        if not isinstance(dt, datetime): raise ValueError("Data de inclusão inválida")
        self.__data_inclusao = dt

    def set_sequencia(self, seq):
        if seq <= 0: raise ValueError("Sequência deve ser positiva")
        self.__sequencia = seq

    def get_id(self): return self.__id
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_data_inclusao(self): return self.__data_inclusao
    def get_sequencia(self): return self.__sequencia

    def __str__(self):
        dt_str = self.__data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Ordem: {self.__sequencia} | Incluído em: {dt_str}"


class UI:
    __playlists = []
    __musicas = []
    __itens = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            elif op == 2: UI.listar_playlists()
            elif op == 3: UI.inserir_musica()
            elif op == 4: UI.listar_musicas()
            elif op == 5: UI.inserir_item()
            elif op == 6: UI.listar_itens_playlist()

    @staticmethod
    def menu():
        print("1 - Cadastrar Playlist")
        print("2 - Listar Playlists")
        print("3 - Cadastrar Música")
        print("4 - Listar Músicas")
        print("5 - Adicionar Música na Playlist")
        print("6 - Ver Músicas e Duração Total da Playlist")
        print("9 - Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def inserir_playlist():
        try:
            id = int(input("ID da Playlist: "))
            nome = input("Nome da Playlist: ")
            desc = input("Descrição: ")
            pl = PlayList(id, nome, desc)
            UI.__playlists.append(pl)
            print("Playlist criada com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def listar_playlists():
        if len(UI.__playlists) == 0:
            print("Nenhuma playlist cadastrada.")
        else:
            for pl in UI.__playlists:
                tempo = pl.tempo_total(UI.__itens, UI.__musicas)
                print(f"{pl} | Duração Total: {tempo}")

    @staticmethod
    def inserir_musica():
        try:
            id = int(input("ID da Música: "))
            t = input("Título: ")
            art = input("Artista: ")
            alb = input("Álbum: ")
            m = int(input("Duração - Minutos: "))
            s = int(input("Duração - Segundos: "))
            dur = timedelta(minutes=m, seconds=s)
            
            mus = Musica(id, t, art, alb, dur)
            UI.__musicas.append(mus)
            print("Música cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def listar_musicas():
        if len(UI.__musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            for m in UI.__musicas:
                print(m)

    @staticmethod
    def inserir_item():
        try:
            id = int(input("ID do Item: "))
            id_p = int(input("ID da Playlist: "))
            id_m = int(input("ID da Música: "))
            seq = int(input("Ordem/Sequência na playlist: "))
            dt = datetime.now()

            item = PlayListItem(id, id_p, id_m, dt, seq)
            UI.__itens.append(item)
            print("Música associada à playlist com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def listar_itens_playlist():
        id_p = int(input("Informe o ID da Playlist: "))
        encontrou = False
        for item in UI.__itens:
            if item.get_id_playlist() == id_p:
                print(item)
                encontrou = True
        if not encontrou:
            print("Nenhum item encontrado para esta playlist.")


UI.main()