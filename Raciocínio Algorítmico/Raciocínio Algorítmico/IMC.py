peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura em cm: "))

print(f"Seu IMC é: {(((100 * peso) / (altura * altura)) * 100):.f2}")