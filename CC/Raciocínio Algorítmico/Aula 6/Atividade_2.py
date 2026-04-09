vogal = "aeiouAEIOU"

while True:
    palavra = input("Digite uma palavra que comece com uma vogal: ").strip()
    
    if palavra[0] in vogal:
        print("Palavra válida! Processando...")
        break
    else:
        print("Erro: A palavra deve começar com uma vogal (a, e, i, o, u). Tente novamente.")

for letra in palavra:
    print(letra)
