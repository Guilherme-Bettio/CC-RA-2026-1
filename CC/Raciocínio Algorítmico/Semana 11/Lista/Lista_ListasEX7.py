lista = []
for i in range(1, 101):
    lista.append(i)

print(lista)

for i in range(1, 101):
    if lista[i] % 2 == 0:
        print(lista[i])