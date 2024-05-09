# Jogo da Forca: Implemente uma versão simples do jogo da forca. 
#O programa começa com uma palavra oculta (o usuário não vê) e 
#o usuário tenta adivinhar a palavra, letra por letra. 
#O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
import random
def escolherPalavra():
    from lista_palavras import lista_palavras
    return random.choice(lista_palavras)

def forca():
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
        tentativa = input("Tente adivinhar uma letra para a palavra:")
        letras_usuario.append(tentativa)

        if tentativa not in palavra:
            chances -= 1

        ganhou = True
        for letra in palavra:
            if letra not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break
 
    if ganhou:
        print(f"Parabens, você ganhou restando {chances} chances, a palavra era: {palavra}")
        
    else:
        print(f"\nAcabaram suas chances, você perdeu! A palavra era:{palavra}")
        print(fases[0])
        
            
forca()