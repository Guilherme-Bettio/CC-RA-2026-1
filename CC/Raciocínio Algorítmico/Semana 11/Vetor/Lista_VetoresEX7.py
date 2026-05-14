vet = [0] * 10


for i in range(0, 10):
    vet[i] = int(input("insira um valor: "))

print(vet)

maior = vet[0]
indice = 0

for i in range(0, 10):
    if vet[i] >= maior:
        maior = vet[i]
        indice = i


print(f"maior valor do vetor: {maior}")
print(f"indice do maior valor do vetor: {indice + 1}")