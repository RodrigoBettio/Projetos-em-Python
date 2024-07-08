#Leilão cego
#Pergunta os itens que serão leiloados e armazena em uma lista
#Limpa a tela
#Pergunta o nome do primeiro participante
#Indica o item[0] a ser leiloado
#Indica o valor do lance da pessoa 
#Encerra a rodada e diz se tem mais pessoas
import os
import time
def itens_do_leilao():
    itens_entrada = input("Quais itens serão leiloados?(Separe apenas por vírgula)\n")
    itens = [item  for item in itens_entrada.split(",")]
    return itens

def loading_animation(duration=5):  #Gerado com IA
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(4):
            print(f"Executando o programa, aguarde{'.' * i}", end="\r")
            time.sleep(0.12)

def principal():
    itens = itens_do_leilao()
    loading_animation()
    os.system("cls")

    lista_lances = {}
    vencedores = {}

    for rodada, item in enumerate(itens):
        os.system("cls")
        print(f"\nRodada {rodada}: {item}")

        lances_rodada = coletar_lances(item)
        lista_lances[item] = lances_rodada
        vencedores[item] = determinar_vencedor(lances_rodada)

    exibir_resultados(vencedores, lista_lances, itens)

def coletar_lances(item):
    lances = {}
    while True:
        nome = input("Digite o seu nome:\n")
        lance = float(input(f"Qual o seu lance para o item {item}?\n"))
        lances[nome] = lance
        os.system("cls")

        continuar = input("Há mais jogadores nesta rodada? (sim/não):\n").lower().strip()
        if continuar != "sim":
            break
    return lances

def determinar_vencedor(lances): #Gerada com IA para conferir empates
    maior_lance = max(lances.values())
    vencedores_empatados = [nome for nome, lance in lances.items() if lance == maior_lance]

    if len(vencedores_empatados) > 1:
        return "Empate entre: " + ", ".join(vencedores_empatados)  # Retorna uma string indicando o empate
    else:
        return vencedores_empatados[0]  # Retorna o único vencedor

def exibir_resultados(vencedores, lista_lances, itens):
    os.system("cls")
    print("\nResultado do Leilão:")
    for item, vencedor in vencedores.items():
        print(f"Rodada {itens.index(item) + 1} - {item}: Vencedor - {vencedor} (R${lista_lances[item][vencedor]:.2f})")

principal()
