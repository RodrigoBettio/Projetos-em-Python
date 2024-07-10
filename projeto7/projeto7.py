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
    print(f"Suas cartas são: {cartas_usuario}")
    print(f"As cartas do dealer são: {cartas_dealer}")
    soma_dealer = cartas_dealer[0]
    continuar = "parar"
    while True:
        continuar = input("Você deseja \"Continuar\" ou \"Parar\"?\n").strip().lower()
        if continuar == "parar":
            break
        elif continuar == "continuar":
            distribuir_carta_usuario(cartas_usuario)
            print(f"Essas são suas cartas:{cartas_usuario}= ", end="")
            soma_usuario, soma_dealer = calcular_somas(cartas_usuario, cartas_dealer)
            verificar_resultado(soma_usuario, soma_dealer)
            print(f"{soma_usuario}\n")  
            if soma_usuario > 21 or (soma_dealer == 21 and soma_dealer == soma_usuario) or (soma_dealer > 21 and soma_usuario <= 21) or (soma_dealer > soma_usuario and soma_dealer <= 21):
                break
        else:
            print("Tente novamente. Você digitou errado.")
            print(cartas_usuario)  

    if continuar == "parar":
        while soma_dealer < 17:
            distribuir_carta_dealer(cartas_dealer)
            soma_usuario, soma_dealer = calcular_somas(cartas_usuario, cartas_dealer)  # Atualiza a soma do dealer aqui
        print(f"Essas são as cartas da casa: {cartas_dealer} = {soma_dealer}")
        verificar_resultado(soma_usuario, soma_dealer)


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

def calcular_somas(cartas_usuario, cartas_dealer):
    """Calcula as somas das cartas do usuário e do dealer."""
    soma_usuario = sum(cartas_usuario)
    soma_dealer = sum(cartas_dealer)
    return soma_usuario, soma_dealer

def verificar_resultado(soma_usuario, soma_dealer):
    """Compara as somas e determina o resultado do jogo."""
    if soma_usuario > 21:
        print("Você estourou os 21.\nA casa venceu. Próxima?")
    elif soma_dealer > 21 and soma_usuario <= 21:
        print("Você venceu, parabéns")
    elif soma_dealer == soma_usuario and soma_dealer <= 21 and soma_usuario <= 21:
        print("Deu empate")
    elif soma_dealer > soma_usuario and soma_dealer <= 21:
        print(f"A soma de suas cartas {soma_usuario}. É menor do que as da casa {soma_dealer}")
        print("A casa venceu. Próxima?")

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