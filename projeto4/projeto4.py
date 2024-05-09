import random
def escolherPalavra():
    from lista_palavras import lista_palavras
    return random.choice(lista_palavras)

def forca(jogador):
    palavra = escolherPalavra()
    letras_usuario = []
    chances = 6
    from forca_imagens import imagem1
    print(imagem1)  
    from forca_imagens import fases
    while True:
        faseCorreta = fases[chances]
        print("")
        print(faseCorreta)
        for letra in palavra:
            if letra in letras_usuario:
                print (letra, end=" ")
            else:
                print("_", end=" ")
        
        print(f"\nEssas letras já foram utilizadas: {letras_usuario}\n")
        tentativa = input(f"Jogador{jogador}, tente adivinhar uma letra para a palavra:")
        letras_usuario.append(tentativa)

        if tentativa not in palavra:
            chances -= 1

        ganhou = True
        for letra in palavra:
            if letra not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break
 
    return chances

def menu():
    print("Bem-vindo ao Jogo da Forca!")
    print("Escolha uma opção:")
    print("1 - Jogar contra um amigo")
    print("2 - Jogar sozinho")

    opcao = input("Escolha a opção desejada: ")

    if opcao == '1':
        chances_jogador1 = forca(1)
        chances_jogador2 = forca(2)

        if chances_jogador1 < chances_jogador2:
            print(f"Parabéns, Jogador 1 venceu com {chances_jogador1} chances restantes!")
        elif chances_jogador2 < chances_jogador1:
            print(f"Parabéns, Jogador 2 venceu com {chances_jogador2} chances restantes!")
        else:
            print("Empate! Ambos jogadores gastaram o mesmo número de chances.")

    elif opcao == '2':
        chances_jogador1 = forca(1)
        print(f"Você jogou sozinho e gastou {chances_jogador1} chances.")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        menu()

menu()