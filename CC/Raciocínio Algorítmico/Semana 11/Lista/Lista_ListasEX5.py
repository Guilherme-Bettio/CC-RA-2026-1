palavras = []
for i in range(0, 5):
    palavras.append(input("insira uma palavra: "))

maxLen = palavras[0]
minLen = palavras[0]

for i in range(0,5):
    if len(palavras[i]) > len(maxLen):
        maxLen = palavras[i]
    elif len(palavras[i]) < len(minLen):
        minLen = palavras[i]

print(f"a maior palavra da lista é: {maxLen}")
print(f"a menor palavra da lista é: {minLen}")