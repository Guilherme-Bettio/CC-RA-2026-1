import random

notas = [random.randint(0, 10) for i in range(20)]

def media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

print("As notas são:", notas)
print("A média das notas é:", media(notas))