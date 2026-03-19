x = int(input("insira o valor de x: "))
y = int(input("insira o valor de y: "))
if x < 10 and y < 10 and x > 0 and y > 0:
    print("dentro do quadrado")
elif x == 10 and y >= 0 and y <=10:
    print("em cima da reta do y ")
elif y == 10 and x >= 0 and x <=10:
    print("em cima da reta do x ")
else:
    print("o ponto esta fora do quadrado")