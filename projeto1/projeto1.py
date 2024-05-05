import sys
import time

def mostrar_ascii_art(art, delay=0.05):
    for linha in art.splitlines():
        print(linha)
        time.sleep(delay)
        
def tentar_novamente():
    while True:
        tentar = input("\nVocê gostaria de tentar novamente? (sim/não)\n")
        tentar = tentar.lower().strip()
        if tentar == "sim":
            tesouroPerdido()
        elif tentar == "não":
            print("\nObrigado por jogar!")
            sys.exit()
        else:
            print("Por favor, responda apenas com \"sim\" ou \"não\".")

def tesouroPerdido():
    #ascii.co.uk/art
    #Usar 3 aspas simples para exibir várias linhas de string
    imagem1 = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    mostrar_ascii_art(imagem1)
    print("Bem-Vindo a Ilha do Tesouro.")
    print("Sua missão é encontrar o Tesouro Perdido")

    while True:   
        direita_ou_esquerda = input("Você está perdido em uma Ilha Deserta e vê dois caminhos. Quer ir para a \"esquerda\" ou \"direita\"? \n")
        direita_ou_esquerda = direita_ou_esquerda.lower().strip()
        if direita_ou_esquerda == "direita": 
            print("Ao ir pela direita, você encontra um Oráculo que te diz:")
            print("\"Sua vida teria sido mais fácil ao escolher a esquerda, por aqui você tem duas opções:\"")
            print("Opção 1: Passar pelo Urso Protetor da Floresta que está dormindo em sua toca, mas morrendo de fome")
            print("Opção 2: Enfrentar o Dragão de Fogo que protege o Tesouro Perdido")
            while True: 
                urso_ou_dragao = input("Você escolhe o Urso ou o Dragão?\n")
                urso_ou_dragao = urso_ou_dragao.lower().strip()
                if urso_ou_dragao == "dragão" or urso_ou_dragao == "dragao":
                    print("Ao te avistar, o dragão solta um bafo de fogo que te torra imediatamente...")
                    print("Você jura que conseguiria enfrentar um dragão? GAME OVER")
                    tentar_novamente()
                elif urso_ou_dragao == "urso":
                    print("Você entra na toca do urso enquanto ele dorme")
                    print("Enquanto está passando, ele abre um dos olhos, parece que está sentindo algo")
                    while True:
                        correr_ou_imovel = input("Você decide correr ou ficar imóvel?\n")
                        correr_ou_imovel = correr_ou_imovel.lower().strip()
                        if correr_ou_imovel == "correr":
                            print("Sim. Com certeza você conseguiu ser mais rápido que um urso...")
                            print("GAME OVER")
                            tentar_novamente()
                        elif correr_ou_imovel == "ficar imóvel" or correr_ou_imovel == "ficar imovel" or correr_ou_imovel == "imovel" or correr_ou_imovel == "imóvel":
                            print("O urso abre o outro olho e abocanha um inseto que estava passando por perto")
                            print("O urso volta a dormir e você pode seguir o seu caminho")
                            print("Ao seguir, você para na praia da Ilha. Está amanhecendo e você encontra um mapa onde indica o caminho ao tesouro pelo mar")
                            print("Você tem a opção de nadar ou de esperar uma ajuda do além... ")
                            while True:
                                nadar_ou_esperar = input ("Deseja \"nadar\" ou \"esperar\"?\n")
                                nadar_ou_esperar = nadar_ou_esperar.lower().strip()
                                if nadar_ou_esperar == "nadar":
                                    print("Você nada, nada, nada e um tubarão te come ")
                                    print("Você obivamente não conseguiria nadar em mar aberto...")
                                    print("GAME OVER")
                                    tentar_novamente()
                                elif nadar_ou_esperar == "esperar":
                                    print("Você espera e surge um duende mágico, ele estrala os dedos e aparece um barco")
                                    print("Vocês vão navegando e ao entrar em uma caverna, encontra então o tesouro perdido")
                                    print("PARABÉNS, VOCÊ ENCONTROU O TESOURO PERDIDO A ANOS")
                                    tentar_novamente()
                                else:
                                    print("Porque escolheu outra opção? Isso não faz sentido")
                        else:
                            print("Porque escolheu outra opção? Isso não faz sentido")
                    
                else:
                    print("Porque escolheu outra opção? Isso não faz sentido") 

        elif direita_ou_esquerda == "esquerda":
            print("Ao seguir, você para na praia da Ilha. Está amanhecendo e você encontra um mapa onde indica o caminho ao tesouro pelo mar")
            print("Você tem a opção de nadar ou de esperar uma ajuda do além... ")
            while True:
                nadar_ou_esperar = input ("Deseja \"nadar\" ou \"esperar\"?\n")
                nadar_ou_esperar = nadar_ou_esperar.lower().strip()
                if nadar_ou_esperar == "nadar":
                    print("Você nada, nada, nada e um tubarão te come ")
                    print("Você obivamente não conseguiria nadar em mar aberto...")
                    print("GAME OVER")
                    tentar_novamente()
                elif nadar_ou_esperar == "esperar":
                    print("Você espera e surge um duende mágico, ele estrala os dedos e aparece um barco")
                    print("Vocês vão navegando e ao entrar em uma caverna, encontra então o tesouro perdido")
                    print("PARABÉNS, VOCÊ ENCONTROU O TESOURO PERDIDO A ANOS")
                    tentar_novamente()
                else:
                    print("Porque escolheu outra opção? Isso não faz sentido")                            
        else: 
            print("Opção errada. Tente novamente")
    
tesouroPerdido()


