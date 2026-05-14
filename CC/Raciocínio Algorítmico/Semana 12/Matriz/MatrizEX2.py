import random

matriz = [
    [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)],
    [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)],
    [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)],
    [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
]
maiorCelula = 0
xMaior = 0
yMaior = 0

print(matriz)

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maiorCelula:
            maiorCelula = matriz[i][j]
            xMaior = i
            yMaior = j

print(f"o maior valor da matriz é: {maiorCelula} na celula [{xMaior}][{yMaior}]")