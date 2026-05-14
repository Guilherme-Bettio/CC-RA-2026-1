matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)

for i in range(3):
    print(matriz[i])


for i in range(3):
    for j in range(3):
        print(matriz[i][j])

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

print(matriz)

for i in range(3):
    print(matriz[i])


for i in range(3):
    for j in range(3):
        print(matriz[i][j])

soma = matriz[0][0] + matriz[1][0]
sub = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
div = matriz[1][2] / matriz[0][2]

print(f"soma das celulas [0][0] e [1][0]: {soma}")
print(f"subtracao das celulas [2][2] e [2][1]: {sub}")
print(f"multimplcacao das celulas [0][1] e [2][0]: {mult}")
print(f"divisao das celulas [1][2] e [0][2]: {div}")