vet = [0] * 10


for i in range(0, 10):
    vet[i] = int(input("insira um valor: "))

print(vet)

maior = vet[0]
menor = vet[0]

for i in range(0, 10):
    if vet[i] >= maior:
        maior = vet[i]
    elif vet[i] <= menor:
        menor = vet[i]


print(f"maior valor do vetor: {maior}")
print(f"menor valor do vetor: {menor}")