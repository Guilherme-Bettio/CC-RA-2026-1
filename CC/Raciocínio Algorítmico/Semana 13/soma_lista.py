lista = [1,2,3,4,5,6,7,8,9]

def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

print("A lista é:", lista)
print("A soma dos elementos da lista é:", soma_lista(lista))