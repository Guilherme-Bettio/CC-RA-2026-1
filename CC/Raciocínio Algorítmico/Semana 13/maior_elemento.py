lista = [23, 9, 67, 2, 45, 12]

def maior_elemento(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]  # Assume o primeiro elemento como o maior inicialmente
    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza o maior se encontrar um número maior
    return maior
print("A lista é:", lista)
print("O maior elemento da lista é:", maior_elemento(lista))
