par = []
impar = []
completa = []

for i in range(1, 11):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

completa.extend(par)
completa.extend(impar)

print(par)
print(impar)
print(sorted(completa))