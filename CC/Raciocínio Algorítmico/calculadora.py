num1 = float(input("Insira dois números: "))
num2 = float(input(""))
print("1. Soma\n4. Subtração\n3. Multiplicação\n4. Divisão")
op = int(input("Escolha uma das operações abaixo: "))
if(op == 1):
    print("Resultado: " + str(num1 + num2))
else:
    if(op == 2):
        print("Resultado: " + str(num1 - num2))
    else: 
        if(op == 3):
            print("Resultado: " + str(num1 * num2))
        else:
            if(op == 4):
                print("Resultado: " + str(num1 / num2))
            else:
                print("ERROR")