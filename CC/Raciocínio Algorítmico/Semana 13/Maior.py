num1 = input("insira o primeiro número: ")
num2 = input("insira o segundo número: ")
num3 = input("insira o terceiro número: ")

def maior_numero(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print(f"o maior número é: {maior_numero(num1, num2, num3)}")