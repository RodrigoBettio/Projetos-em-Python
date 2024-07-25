import random, os
from imagens import logo, vs  
from dicionario_famosos import lista  


def obter_conta_aleatoria():
    """Obtém dados de uma conta aleatória"""
    return random.choice(lista)


def formatar_dados(conta):
    """Formata a conta em: nome, descrição e país"""
    nome = conta["nome"]
    descricao = conta["descricao"]
    pais = conta["pais"]
    return f"{nome}, um(a) {descricao}, de {pais}"


def verificar_resposta(palpite, seguidores_a, seguidores_b):
    """Verifica os seguidores em relação ao palpite do usuário
    e retorna True se acertou ou False se errou."""
    if seguidores_a > seguidores_b:
        return palpite == "a"
    else:
        return palpite == "b"

def jogar():
    print(logo)
    pontuacao = 0
    continuar_jogo = True
    conta_a = obter_conta_aleatoria()
    conta_b = obter_conta_aleatoria()

    while continuar_jogo == True:
        conta_a = conta_b
        conta_b = obter_conta_aleatoria()

        while conta_a == conta_b:
            conta_b = obter_conta_aleatoria()

        print(f"Compare A: {formatar_dados(conta_a)}.")
        print(vs)
        print(f"Contra B: {formatar_dados(conta_b)}.")

        palpite = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower().strip()
        seguidores_a = conta_a["seguidores"]
        seguidores_b = conta_b["seguidores"]
        resposta_correta = verificar_resposta(palpite, seguidores_a, seguidores_b)

        os.system("cls") 
        print(logo)
        if resposta_correta:
            pontuacao += 1
            print(f"Você acertou! Pontuação atual: {pontuacao}.")
        else:
            continuar_jogo = False
            print(f"Que pena, você errou. Pontuação final: {pontuacao}")

jogar()
