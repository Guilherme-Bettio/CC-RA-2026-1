palavra = input("Digite uma palavra: ")

def e_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Remove espaços e converte para minúsculas
    return palavra == palavra[::-1]  # Compara a palavra com sua versão invertida

print("A palavra é um palíndromo?", e_palindromo(palavra))