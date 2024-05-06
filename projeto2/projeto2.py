import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens_jogo = [pedra, papel, tesoura]

def mostrar_escolhas(escolha_jogador1, escolha_jogador2):
    print("Jogador 1 escolheu:")
    print(imagens_jogo[escolha_jogador1])
    print("Jogador 2 escolheu:")
    print(imagens_jogo[escolha_jogador2])

def jogar_contra_jogador():
    pontuacao = {"jogador1": 0, "jogador2": 0}
    rodada = 1

    while True:
        print("Rodada", rodada)
        escolha_jogador1 = int(input("Jogador 1, o que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
        escolha_jogador2 = int(input("Jogador 2, o que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
        print("")

        if escolha_jogador1 < 0 or escolha_jogador1 > 2 or escolha_jogador2 < 0 or escolha_jogador2 > 2:
            print("Você digitou uma opção inválida. Tente novamente.")
            continue

        mostrar_escolhas(escolha_jogador1, escolha_jogador2)

        if escolha_jogador1 == escolha_jogador2:
            print("É um empate")
        elif (escolha_jogador1 == 0 and escolha_jogador2 == 2) or \
             (escolha_jogador1 == 1 and escolha_jogador2 == 0) or \
             (escolha_jogador1 == 2 and escolha_jogador2 == 1):
            print("Jogador 1 ganhou!")
            pontuacao["jogador1"] += 1
        else:
            print("Jogador 2 ganhou!")
            pontuacao["jogador2"] += 1

        print("Pontuação atual - Jogador 1: {}, Jogador 2: {}".format(pontuacao["jogador1"], pontuacao["jogador2"]))

        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break
        rodada += 1

def jogar_contra_computador():
    pontuacao = {"jogador": 0, "computador": 0}
    rodada = 1

    while True:
        print("Rodada", rodada)
        escolha_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
        print("")

        if escolha_usuario < 0 or escolha_usuario > 2:
            print("Você digitou uma opção inválida. Tente novamente.")
            continue

        escolha_computador = random.randint(0, 2)
        mostrar_escolhas(escolha_usuario, escolha_computador)

        if escolha_usuario == escolha_computador:
            print("É um empate")
        elif (escolha_usuario == 0 and escolha_computador == 2) or \
             (escolha_usuario == 1 and escolha_computador == 0) or \
             (escolha_usuario == 2 and escolha_computador == 1):
            print("Você ganhou!")
            pontuacao["jogador"] += 1
        else:
            print("Você perdeu")
            pontuacao["computador"] += 1

        print("Pontuação atual - Jogador: {}, Computador: {}".format(pontuacao["jogador"], pontuacao["computador"]))

        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break
        rodada += 1

def menu():
    print("Bem-vindo ao Pedra, Papel ou Tesoura!")
    print("Escolha uma opção:")
    print("1. Jogar contra o computador")
    print("2. Jogar contra outro jogador")
    print("3. Sair")
    escolha = input("Digite o número da opção desejada: ")
    return escolha

while True:
    opcao = menu()

    if opcao == '1':
        jogar_contra_computador()
    elif opcao == '2':
        jogar_contra_jogador()
    elif opcao == '3':
        print("Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
