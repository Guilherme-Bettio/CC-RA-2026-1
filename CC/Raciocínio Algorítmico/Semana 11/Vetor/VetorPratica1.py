numeros = [5, 7, 12, 2, 9, 21]
soma = 0
sub = 0
mult = 0
div = 0

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])

numeros[1] = 17
numeros[2] = 1
numeros[3] = 22
numeros[4] = 29

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])

soma = numeros[4] + numeros[5]
sub = numeros[3] - numeros[1]
mult = numeros[0] * numeros[5]
div = numeros[3] / numeros[2]

print("\n")
print(soma)
print(sub)
print(mult)
print(div)
print("\n")

i = 0

while i < 6:
    print(numeros[i])
    i += 1