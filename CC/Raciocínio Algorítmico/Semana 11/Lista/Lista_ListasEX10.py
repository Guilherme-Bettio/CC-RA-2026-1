tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador_atual = "X"
jogadas = 0

print("--- JOGO DA VELHA ---")

while True:
    # Exibir o tabuleiro
    print(f"\n  0   1   2")
    print(f"0 {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print(" ---+---+---")
    print(f"1 {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print(" ---+---+---")
    print(f"2 {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")

    print(f"\nTurno do jogador: {jogador_atual}")
    
    # Loop para garantir uma linha válida
    while True:
        entrada = input("Insira a linha (0, 1, 2): ")
        if entrada in ["0", "1", "2"]:
            linha = int(entrada)
            break
        print("Linha inválida! Escolha 0, 1 ou 2.")

    # Loop para garantir uma coluna válida
    while True:
        entrada = input("Insira a coluna (0, 1, 2): ")
        if entrada in ["0", "1", "2"]:
            coluna = int(entrada)
            break
        print("Coluna inválida! Escolha 0, 1 ou 2.")
            
    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada! Tente outra.")
        continue
        
    # Marcar a jogada
    tabuleiro[linha][coluna] = jogador_atual
    jogadas += 1
    
    # Verificar vitória (linhas, colunas e diagonais)
    venceu = False
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador_atual:
            venceu = True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador_atual:
            venceu = True
    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        venceu = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        venceu = True
        
    if venceu:
        print(f"\nPARABÉNS! O jogador {jogador_atual} venceu!")
        break
        
    if jogadas == 9:
        print("\nDEU VELHA! O jogo empatou.")
        break
        
    # Alternar jogador
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
