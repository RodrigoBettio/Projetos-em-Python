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
            time.sleep(0.15)

def principal():
    itens = itens_do_leilao()
    loading_animation()
    os.system("cls")
    rodando(itens)
    
def rodando(itens):
    print("Desenvolver a lógica")

def jogadores():
    lista_lances= {}
    nome = input("Qual é o seu nome?")
    lance = float(input("Qual é o seu lance para o item?"))
    lista_lances ["nome"] = nome
    lista_lances ["lance"] = lance
    print(lista_lances)

principal()
