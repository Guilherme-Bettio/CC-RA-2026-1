"""
Fac¸a um programa que leia um vetor de 8 posic¸ ˜oes e, em seguida, leia tamb ´em dois va-
lores X e Y quaisquer correspondentes a duas posic¸ ˜oes no vetor. Ao final seu programa
devera´ escrever a soma dos valores encontrados nas respectivas posic¸ ˜oes X e Y .
"""

vet = [1, 2, 3, 4, 5, 6, 7, 8]

print(vet)

x = int(input("insira o indice de algum valor da lista: "))
y = int(input("insira o indice de algum valor da lista: "))

print(vet[x - 1] + vet[y - 1])