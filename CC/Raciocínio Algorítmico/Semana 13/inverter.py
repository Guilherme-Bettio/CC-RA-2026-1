palavra = input("Digite uma palavra: ")

def inverter(palavra):
    invertida = ""
    for i in range(len(palavra)-1, -1, -1):
        invertida += palavra[i]
    return invertida
print("A palavra invertida é:", inverter(palavra))