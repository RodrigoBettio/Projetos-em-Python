import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
baralho = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def menu():
    print(logo)
    cartas_usuario = []
    cartas_dealer = []
    distribuir_inicial(cartas_usuario, cartas_dealer)
    print(f"Suas cartas são: {cartas_usuario} (Valores)")
    print(f"As cartas do dealer são: {cartas_dealer} (Valores)")
    continuar = "parar"
    while True:
        continuar = input("Você deseja \"Continuar\" ou \"Parar\"?\n").strip().lower()
        if continuar == "parar":
            break
        elif continuar == "continuar":
            distribuir_carta_usuario(cartas_usuario)
            print(f"Essas são suas cartas:{cartas_usuario}= ", end="")
            cartas_usuario, cartas_dealer, soma_usuario, soma_dealer = conferir_resultado(cartas_usuario, cartas_dealer)
            print(f"{soma_usuario}\n")
            if soma_usuario > 21 or (soma_dealer == 21 and soma_dealer == soma_usuario) or (soma_dealer > 21 and soma_usuario <=21) or (soma_dealer > soma_usuario and soma_dealer <=21):
                break
        else:
            print("Tente novamente. Você digitou errado.")
            print(cartas_usuario)
    if continuar == "parar":
        while soma_dealer <17:
            distribuir_carta_dealer(cartas_dealer)
            cartas_usuario, cartas_dealer, soma_usuario, soma_dealer = conferir_resultado(cartas_usuario, cartas_dealer)
            print(f"Essas são as cartas da casa:{cartas_dealer} = ", end="")
            print(soma_dealer)

def distribuir_inicial(cartas_usuario, cartas_dealer):
    """Distribui a mão inicial. 2 cartas ao usuário e 1 carta ao Dealer"""
    for i in range(2):
        carta = random.choice(baralho)
        cartas_usuario.append(carta)
    
    carta = random.choice(baralho)
    cartas_dealer.append(carta)
    
    soma = 0
    for i in cartas_usuario:
        soma += i
    
    if soma == 21:
        print("O usuário ganhou, parabéns!")

    
    return cartas_usuario, cartas_dealer

def conferir_resultado(cartas_usuario, cartas_dealer):
    """Compara os montes do Usuário e do Dealer e imprime o seu resultado"""
    soma_dealer = 0
    soma_usuario = 0

    for i in cartas_usuario:
        soma_usuario += i
    
    for x in cartas_dealer:
        soma_dealer += x

    if soma_dealer == 21 and soma_dealer == soma_usuario:
        print("Deu empate")
    elif soma_usuario >21:
        print("Você estourou os 21.\n A casa venceu. Próxima?")
    elif soma_dealer > 21 and soma_usuario <=21: 
        print("Você venceu, parabéns")
    elif soma_dealer > soma_usuario and soma_dealer <=21:
        print(f"A soma de suas cartas {soma_usuario}. É menor do que as da casa {soma_dealer}")
        print("A casa venceu. Próxima?")
    
    return cartas_usuario, cartas_dealer, soma_usuario, soma_dealer


def distribuir_carta_dealer(cartas_dealer):
    """Insere uma carta no monte da casa"""
    carta = random.choice(baralho)
    cartas_dealer.append(carta)

    return cartas_dealer

def distribuir_carta_usuario(cartas_usuario):
    """Insere uma carta no monte do usuário"""
    carta = random.choice(baralho)
    cartas_usuario.append(carta)

    return cartas_usuario
    
menu()