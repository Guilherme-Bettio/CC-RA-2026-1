matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def diagonal(matriz):
    diagonal_principal = []
    for i in range(len(matriz)):
        diagonal_principal.append(matriz[i][i])
    return diagonal_principal
print("A matriz é:")
for linha in matriz:
    print(linha)
print("A diagonal principal é:", diagonal(matriz))