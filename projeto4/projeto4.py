import random
def escolherPalavra():
    palavras = [ "Python", "Computador", "Mouse"]
    palavraEscolhida = random.choice(palavras)
    return palavraEscolhida

def forca():
    from forca_imagens import imagem1
    print(imagem1)
    palavraEscolhida = escolherPalavra()
    chances = 6

    while True:
        ganhou = True

        letraUsuário = input("Digite uma letra que você acha que está na palavra: ").strip()
        if letraUsuário not in palavraEscolhida:
            chances -= 1
            
        for caracter in palavraEscolhida:
            if caracter == letraUsuário:
                print(caracter, end=" ")
            else:
                print("_", end=" ")
        
        if ganhou == False or chances == 0:
            break
        print(palavraEscolhida)
        print(chances)
forca()