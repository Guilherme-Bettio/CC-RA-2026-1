#Floresta
while True:
    print ("Você está em uma floresta e precisa escolher um caminho para seguir. Você pode escolher: \n1. esquerda \n2. direita.")
    
    while True:
        dir = (input("Insira a direcao que deseja seguir: "))
        if dir in ("Direita", "Esquerda", "1", "2"):
            break
        print("Opção inválida. Tente novamente.")

    #Rio
    if dir == "Esquerda" or dir == "1":
        while True:
            print("Você encontra um rio: \n1. Atravessar \n2. Voltar")

            while True:
                mon = input("Insira sua decisão: ")
                if mon in ("Atravessar", "Voltar", "1", "2"):
                    break
                print("Opção inválida. Tente novamente.")

            if mon in ("2", "Voltar"): 
                break

            if mon in ("1", "Atravessar"):
                print("Meus parabens! Você esta seguro na vila!")
                break

        if mon in ("1", "atravessar"): break

    #Montanha
    if dir == "Direita" or dir == "2":
        while True:
            print("Você encontra uma montanha: \n1. Subir \n2. Voltar")

            while True:
                mon = input("Insira sua decisão: ")
                if mon in ("Subir", "Voltar", "1", "2"):
                    break
                print("Opção inválida. Tente novamente.")

            if mon in ("2", "Voltar"): 
                break

            if mon in ("1", "Subir"):
                print("Meus parabens! Você encontrou o tesouro perdido!")
                break

        if mon in ("1", "Subir"): break