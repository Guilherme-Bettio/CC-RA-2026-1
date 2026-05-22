palavra = input("Digite uma palavra: ")

def conta_caracter(palavra):
    contador = 0
    for char in palavra:
        if char == 'a':  # Exemplo: contar apenas o caractere 'a'
            contador += 1
    return contador

print("A palavra é:", palavra)
print("Contagem de 'a':", conta_caracter(palavra))