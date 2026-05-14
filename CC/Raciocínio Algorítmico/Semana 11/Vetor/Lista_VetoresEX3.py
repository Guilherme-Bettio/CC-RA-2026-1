'''
Ler um conjunto de n ´umeros reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos t ˆem 10
elementos cada. Imprimir os conjuntos.
'''

vet = [0] * 10
VetQuadrado = [0] * 10

for i in range(0,10):
    vet[i] = int(input("insira um valor: "))

for i in range(0,10):
    VetQuadrado[i] = vet[i]**2
    print(VetQuadrado[i])

print(vet)
print(VetQuadrado)