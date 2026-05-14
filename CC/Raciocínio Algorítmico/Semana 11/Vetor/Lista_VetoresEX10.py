vet = [0] * 5
media = 0

for i in range(0, 5):
    vet[i] = float(input("insira um valor: "))
    media = media + vet[i]

print(vet)

maior = vet[0]
menor = vet[0]

for i in range(0, 5):
    if vet[i] >= maior:
        maior = vet[i]
    elif vet[i] <= menor:
        menor = vet[i]


print(f"maior valor do vetor: {maior}")
print(f"menor valor do vetor: {menor}")
print(f"a média dos valores do vetor é: {media / 5}")