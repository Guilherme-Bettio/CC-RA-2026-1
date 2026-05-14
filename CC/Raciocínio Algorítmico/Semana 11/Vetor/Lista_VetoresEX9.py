vet = [0] * 10
negativos = 0
soma = 0

for i in range(0, 10):
    vet[i] = int(input("insira um numero: "))
    if vet[i] < 0:
        negativos += 1
    else:
        soma = soma + vet[i]

print(f"quantidade de numeros negativos: {negativos}")
print(f"soma dos numeros inteiros: {soma}")