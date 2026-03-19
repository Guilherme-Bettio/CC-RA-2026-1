while True:
    a = int(input("insira o valor de uma lateral de um triangulo: "))
    b = int(input("insira o valor de outra lateral de um triangulo: "))
    c = int(input("insira o valor de uma terceira lateral de um triangulo: "))
    if a + b > c and a + c > b and b + c > a:
        break
    print("os valores inseridos nao formam um triangulo")

if a == b == c:
    print("seu triângulo é um Equilátero")
elif a != b != c:
    print("seu triângulo é um Escaleno")
else:
    print("seu triângulo é um Isósceles")

if (a > b and a > c) and a**2 == b**2 + c**2:
    print("é retângulo e a hipotenusa é 'a'")
elif (b > a and b > c) and b**2 == a**2 + c**2:
    print("é retângulo e a hipotenusa é 'b'")
elif (c > b and c > a) and c**2 == b**2 + a**2:
    print("é retângulo e a hipotenusa é 'c'")
else:
    print("seu triângulo não é retângulo")