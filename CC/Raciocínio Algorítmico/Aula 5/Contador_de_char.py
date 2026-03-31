palavra = str(input("insira uma palavra: "))
while len(palavra) < 3 or len (palavra) > 10:
    print("palavra invalida")
print(palavra)
print(len(palavra))