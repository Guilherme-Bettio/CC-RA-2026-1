while True:
    nota = float(input("insira uma nota de um aluno: "))
    if nota >= 0 and nota <= 10:
        break
    print("numero invalido")
print(nota)