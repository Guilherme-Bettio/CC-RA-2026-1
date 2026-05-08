vet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = 0
impar = 0
for i in range(0, 10):
    if vet[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(vet)
print(f"par: {par}")
print(f"impar: {impar}")