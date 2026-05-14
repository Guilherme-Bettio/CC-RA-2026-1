import random

acertos = 0
numeros = [0] * 6
sorteados = [0] * 6

for i in range(0,6):
    while True:
        numeros[i] = (int(input("Insira os numeros desejados para concorrer à Mega Sena: ")))
        if numeros[i] > 0 and numeros[i] < 61:
            break
        else:
            print("numero invalido")

for i in range(0,6):
    sorteados[i] = (random.randint(1, 61))

for i in range(0,6):
    sorteados[i]
    for j in range(0,6):
        if numeros[j] == sorteados[i]:
            acertos += 1

print(f"Sorteados: {sorteados}")
print(f"Escolhidos: {numeros}")
print(f"Acertos: {acertos}")