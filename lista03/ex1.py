class Raio:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

print("Digite o valor do raio:")
raio = float(input())
print(f"A área do círculo é: {Raio(raio).area()}")