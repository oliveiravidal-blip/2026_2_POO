print("Digite quatro valores inteiros")

soma_pares = 0
soma_impares = 0

for _ in range(4):
    numero = int(input())
    
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f"Soma dos pares = {soma_pares}")
print(f"Soma dos ímpares = {soma_impares}")