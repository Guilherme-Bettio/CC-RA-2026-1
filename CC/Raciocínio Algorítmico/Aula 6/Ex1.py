num = 0
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        num += 1
print(f"Numeros que sao multiplos de 3 e nao sao multiplos de 5: {num}")