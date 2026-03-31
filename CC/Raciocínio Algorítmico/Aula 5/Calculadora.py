while True:
    while True:
        op = int(input("insira o numero correspondente ao operador desejado: \n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Sair\n"))
        if op >= 1 and op <= 5:
            break
        print("operador inválido")
    if op == 5:
        break
    num1 = int(input("insira um numero: "))
    num2 = int(input("insira um numero: "))
    if op == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    if op == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    if op == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    if op == 4:
        if num2 == 0:
            print("Qualquer numero dividido por ZERO é considerado uma aberração")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")


