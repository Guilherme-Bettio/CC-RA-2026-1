"""
6. Desenvolvimento de uma calculadora em Python com menu de opções

Implemente um programa em Python que funcione como uma calculadora simples com menu.

O programa deve exibir repetidamente as seguintes opções:

1: soma
2: subtração
3: multiplicação
4: divisão
0: sair
Ao escolher uma operação, o usuário deve informar dois números, e o programa deve exibir o resultado correspondente.

O menu deve continuar sendo exibido até que o usuário escolha a opção 0.

Requisitos:
utilizar while para manter o programa em execução
utilizar if/elif/else para tratar as opções do menu
tratar divisão por zero
informar quando a opção digitada for inválida
6.1 [DESAFIO com expressão completa]

Crie uma nova versão da calculadora sem menu de opções, em que o usuário digita diretamente uma expressão aritmética para ser resolvida pelo programa.

Escolha um dos níveis abaixo para implementar, de acordo com o grau de dificuldade desejado.

Nível 1: Fácil

O programa deve aceitar uma expressão aritmética simples, contendo:

dois números
um único operador
Exemplos de entradas aceitas:

2 + 5
10 - 4
3 * 8
20 / 5
O programa deve identificar os dois operandos e o operador, realizar o cálculo correspondente e exibir o resultado.

Nível 2: Intermediário

O programa deve aceitar uma expressão com quantidade ilimitada de números e operadores, por exemplo:

2 + 5 - 1
10 + 4 + 3
20 / 5 * 2
Nesta versão, a expressão deve ser resolvida da esquerda para a direita, sem respeitar a prioridade entre operadores.

Exemplo:

8 + 3 * 2
Resultado produzido pelo programa nessa versão:

8 + 3 = 11
11 * 2 = 22
Observação: nessa versão, a expressão será resolvida apenas na ordem em que aparece, o que pode gerar resultados diferentes da prioridade matemática usual.

Nível 3: Difícil

O programa deve aceitar uma expressão com quantidade ilimitada de números e operadores, por exemplo:

2 + 5 - 1
10 + 4 * 3
20 / 5 * 2
8 + 3 * 2
Nesta versão, o programa deve resolver a expressão respeitando a prioridade das operações, ou seja:

multiplicação e divisão antes
soma e subtração depois
Exemplo:

8 + 3 * 2
Resultado correto:

3 * 2 = 6
8 + 6 = 14
Nível 4: Muito Difícil

O programa deve aceitar uma expressão completa, incluindo:

vários números
vários operadores
uso de parênteses
Exemplos:

2 * (3 + 5 - 1)
(10 - 2) * 3
8 + 2 * (4 - 1)
Nesta versão, o programa deve resolver corretamente a expressão considerando:

os parênteses
a prioridade entre operadores
Regras gerais do desafio

a calculadora não deve utilizar menu de opções
o usuário deve digitar diretamente a expressão
o programa deve continuar funcionando até que seja digitado um comando de saída, como sair
o programa deve informar quando a expressão estiver em formato inválido
o programa deve tratar divisão por zero, quando necessário
"""

def resolver_simples(lista):
    # Trata expressões que começam com sinal (ex: -5 + 3)
    if lista and lista[0] == "-":
        lista.insert(0, 0.0)
    if lista and lista[0] == "+":
        lista.pop(0)

    i = 0

    while i < len(lista):

        if lista[i] == "*" or lista[i] == "/":
            numEsq = lista[i - 1]
            numDir = lista[i + 1]

            if lista[i] == "*":
                resultadoParcial = numEsq * numDir
            else:
                if numDir == 0:
                    raise ZeroDivisionError("Divisão por zero!")
                resultadoParcial = numEsq / numDir
            lista[i - 1] = resultadoParcial
            lista.pop(i)
            lista.pop(i)

        else:
            i += 1
    i = 0

    while i < len(lista):

        if lista[i] == "+" or lista[i] == "-":
            numEsq = lista[i - 1]
            numDir = lista[i + 1]

            if lista[i] == "+":
                resultadoParcial = numEsq + numDir
            else:
                resultadoParcial = numEsq - numDir
            lista[i - 1] = resultadoParcial
            lista.pop(i)
            lista.pop(i)

        else:
            i += 1
    return lista[0]

while True:
    try:
        ex = input("Insira uma expressao matematica (ex: 8 + 3 * 2) ou 'sair': ").strip()

        if ex.lower() == "sair":
            print("Encerrando calculadora...")
            break

        if not ex:
            continue


        lista = []
        numTemp = ""

        for char in ex:

            if char == " ":
                continue

            if char in "+-*/()":
                # Permite sinal de + ou - como parte de um número (ex: -5 * 3 ou (-2+4))
                if (char == "-" or char == "+") and (not lista or (isinstance(lista[-1], str) and lista[-1] in "+-*/(")):
                    if not numTemp:
                        numTemp = char
                        continue

                if numTemp:
                    if numTemp == "-" or numTemp == "+":
                        # Caso especial: sinal antes de parênteses (ex: -( ... ))
                        if char == "(":
                            if numTemp == "-":
                                lista.append(0.0)
                                lista.append("-")
                        # Se não for parêntese, o sinal deveria estar numTemp seguido de dígitos
                        # Se chegou aqui como sinal puro, é um erro de sintaxe que o float() pegaria
                        else:
                            try:
                                lista.append(float(numTemp))
                            except ValueError:
                                # Deixa o erro acontecer para ser pego pelo bloco try/except principal
                                pass
                    else:
                        lista.append(float(numTemp))
                    numTemp = ""
                lista.append(char)

            else:
                numTemp += char

        if numTemp != "":
            lista.append(float(numTemp))
        
        while "(" in lista:
            indice_abre = -1
            for i in range(len(lista)):
                if lista[i] == "(":
                    indice_abre = i

            indice_fecha = -1
            for i in range(indice_abre, len(lista)):
                if lista[i] == ")":
                    indice_fecha = i
                    break
            
            if indice_fecha == -1:
                raise ValueError("Erro: Parêntese não fechado!")
            
            sub_lista = lista[indice_abre + 1 : indice_fecha]
            resultado_sub = resolver_simples(sub_lista)

            lista[indice_abre] = resultado_sub
            for _ in range(indice_fecha - indice_abre):
                lista.pop(indice_abre + 1)
            
        resultado_final = resolver_simples(lista)
        print(f"o resultado final: {resultado_final}")
    
    except ZeroDivisionError as e:
        print (e)
    except Exception as e:
        print(f"Error na expressão: {e}")