import random

numerosjogador1 = []
numerosjogador2 = []
for i in range(0,3):
    numerosjogador1.append(random.randint(1,6))
for i in range(0,3):
    numerosjogador2.append(random.randint(1,6))

print(numerosjogador1)
print(numerosjogador2)    

print(f"Jogador1: {sum(numerosjogador1)}")
print(f"Jogador2: {sum(numerosjogador2)}")
if sum(numerosjogador1) > sum(numerosjogador2):
    print("jogador1 GANHOUUU")
elif sum(numerosjogador1) < sum(numerosjogador2):
    print("jogador2 GANHOUUU")
else:
    print("EMPATE")