numMin = int(input("Insira um numero Minimo: "))
numMax = int(input("Insira um numero Maximo: "))
for i in range(numMin, numMax + 1):
    for j in range(1, 11):
        print(i * j, end=" | ")
    print("")