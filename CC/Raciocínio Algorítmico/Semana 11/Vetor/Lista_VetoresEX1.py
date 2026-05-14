#Fac¸a um programa que possua um vetor denominado A que armazene 6 n ´umeros intei-
#ros. O programa deve executar os seguintes passos:
#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
#(b) Armazene em uma vari ´avel inteira (simples) a soma entre os valores das posic¸ ˜oes
#A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
#(c) Modifique o vetor na posic¸ ˜ao 4, atribuindo a esta posic¸ ˜ao o valor 100.
#(d) Mostre na tela cada valor do vetor A, um em cada linha.

A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]

print(f"soma: {soma}")

A[3] = 100

for i in range(0, 6):
    print(A[i])