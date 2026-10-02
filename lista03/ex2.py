class Viagem:
    def __init__(self, distancia, tempo):
        self.distancia = distancia
        self.tempo = tempo
    def tempo_gasto(self):
        return self.tempo / self.distancia
    
print("Digite a distância percorrida (em km):")
distancia = float(input())
print("Digite o tempo gasto (em horas):")
tempo = float(input())
print("O tempo gasto por km é:", Viagem(distancia, tempo).tempo_gasto())