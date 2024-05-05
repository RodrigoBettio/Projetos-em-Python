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

def mostrar_escolhas(escolha_usuario, escolha_computador):
    print("Você escolheu:")
    print(imagens_jogo[escolha_usuario])
    print("O computador escolheu:")
    print(imagens_jogo[escolha_computador])

def jogar(pontuacao):
    escolha_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
    print("")

    if escolha_usuario < 0 or escolha_usuario > 2:
        print("Você digitou uma opção inválida. Tente novamente.")
        return pontuacao

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
    return pontuacao

pontuacao = {"jogador": 0, "computador": 0}
rodada = 1

while True:
    print("Rodada", rodada)
    pontuacao = jogar(pontuacao)
    jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        break
    rodada += 1