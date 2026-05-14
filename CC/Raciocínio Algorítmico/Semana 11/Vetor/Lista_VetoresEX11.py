vet = [0] * 5
indiceMin = 0
indiceMax = 0

for i in range(0, 5):
    vet[i] = int(input("insira um valor: "))

print(vet)

maior = vet[0]
menor = vet[0]

for i in range(0, 5):
    if vet[i] >= maior:
        maior = vet[i]
        indiceMax = i
    elif vet[i] <= menor:
        menor = vet[i]
        indiceMin = i


print(f"maior valor do vetor: {maior}")
print(f"indice do maior valor do vetor: {indiceMax}")
print(f"menor valor do vetor: {menor}")
print(f"indice do menor valor do vetor: {indiceMin}")