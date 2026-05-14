qualquer = []
for i in range(0, 6):
    while True:
        qualquer.append(int(input("insira um numero: ")))
        if qualquer[i] > 0:
            break
        else:
            print("numero invalido")

print(qualquer)
print(sorted(qualquer))
print(sorted(qualquer, reverse=True))

print(f"tamanho da lista: {len(qualquer)}")
print(f"menor valor da lista: {min(qualquer)}")
print(f"maior valor da lista: {max(qualquer)}")
print(f"soma da lista: {sum(qualquer)}")