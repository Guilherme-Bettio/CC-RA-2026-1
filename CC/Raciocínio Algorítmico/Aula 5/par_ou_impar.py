flag = 0
par = 0
impar = 0
while flag < 10:
    flag += 1
    num = int(input("insira um numero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(par)
print(impar)