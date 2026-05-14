notas = [0] * 15
media = 0

for i in range(0,15):
    notas[i] = float(input("insira as notas dos alunos: "))
    media = media + notas[i]

print(f"a media das notas é: {media/15}")