matriz = [
    [1234, 7.0, 8.4, 0],
    [1345, 7.4, 6.4, 0],
    [1456, 8.9, 8.2, 0],
    [1567, 3.2, 9.4, 0],
    [1678, 2.6, 2.5, 0]
]
matriculaMaiorNota = 0
maiorNota = 0

for i in range(5):
    for j in range(3):
        matriz[i][3] = (matriz[i][1] + matriz[i][2]) / 2
        if matriz[i][3] > maiorNota:
            maiorNota = matriz[i][3]
            matriculaMaiorNota = matriz[i][0]

print(f"o aluno com a maior nota é: {matriculaMaiorNota} com {maiorNota}")        