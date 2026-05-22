def soma(num1, num2):
    return float(num1) + float(num2)
def subtracao(num1, num2):
    return float(num1) - float(num2)
def multiplicacao(num1, num2):
    return float(num1) * float(num2)
def divisao(num1, num2):
    if float(num2) == 0:
        return "Erro: Divisão por zero não é permitida."
    return float(num1) / float(num2)
def menu():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Digite o número da operação desejada: ")
    if escolha == '1':
        return soma(num1, num2)
    elif escolha == '2':
        return subtracao(num1, num2)
    elif escolha == '3':
        return multiplicacao(num1, num2)
    elif escolha == '4':
        return divisao(num1, num2)
    elif escolha == '5':
        return "Encerrando a calculadora. Até mais!"
    else:
        return "Opção inválida."
while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")   
    resultado = menu()
    if resultado == "Encerrando a calculadora. Até mais!":
        print(resultado)
        break
    print("Resultado:", resultado)