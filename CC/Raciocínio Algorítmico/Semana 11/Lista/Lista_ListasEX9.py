import random

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
random.shuffle(lista)
escolha = random.choice(lista)
indice = 0

for i in range(0, 26):
    if lista[i] == escolha:
        indice = i

resposta = int(input(f"insira o numero da posicao que você acredita que a letra {escolha} se encontra: "))
if resposta == escolha:
    print("MEUS PARABENS, VOCÊ ACERTOU!!!! (sabe deus como...)")
else:
    print("pois é, infelizmente você teve o mesmo resultado que os outros")