num = 0
numTotal = 0
while True:
    num = int(input("insira um numero positivo: "))
    if (num < 0):
        print("numero invalido, tente novamente...")
    else:
        print("numero valido, prosseguindo...")
        break
for i in range(1, num + 1):
    numTotal = numTotal + i
    print(f"{i}", end="")
    if i == num:
        print(f" = {numTotal}")
    else:
        print(" + ", end="")