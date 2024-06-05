from imagens import imagem1
print(imagem1)
def cifra():
    while True:
        entrada = input("Você deseja [codificar] ou [decodificar] a mensagem?\n").strip().lower()
        if entrada == "codificar":
            codificar()
        elif entrada == "decodificar":
            decodificar()
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        continuar = input("Você deseja realizar outra operação? [sim/não]\n").strip().lower()
        if continuar != 'sim':
            print("Encerrando o programa. Até mais!")
            break
    
    #Usuário digita se quer codificar ou decodificar 
    #Usuario digita a frase
    #Usuario digita o número pra ir pra frente (codificar) ou pra trás (decodificar)
    #Retorna a palavra 
def codificar():
    alfabeto, lista_palavra, posicoes = listagem_palavra()
    mensagem = []
    numero = int(input("Qual o número que você quer para codificar sua mensagem?\n"))
    
    for indice in posicoes:
        if indice == -1:
            mensagem.append(-1)
        else:
            indice = (indice + numero) %len(alfabeto)
            mensagem.append(indice)
    codificado = "".join([alfabeto[i] for i in mensagem]) 
    print(f"A frase codificada é:{codificado}")
    print(mensagem)
        #Pegar as posições 
        #Aumentar o número de vezes que o usuário pedir
        #Imprimir o alfabeto com as novas posições
        
def decodificar():
    alfabeto, lista_palavra, posicoes = listagem_palavra()
    mensagem = []
    numero = int(input("Qual o número que você quer para decodificar sua mensagem?\n"))
    for indice in posicoes:
        if indice == -1:
            mensagem.append(-1)
        else:
            indice = (indice - numero)%len(alfabeto)
            mensagem.append(indice)
    codificado = "".join([alfabeto[i] if  i != -1 else ' ' for i in mensagem])
    print(f"A frase decodificada é: {codificado}")

def listagem_palavra():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
    palavra = input("Qual frase gostaria você gostaria de enviar?\n").lower()
    lista_palavra = []
    posicoes = []

    for letra in palavra:
        lista_palavra.append(letra) 

    for letra in palavra:
        if letra == " ":
            posicaoEspaco = -1
            posicoes.append(posicaoEspaco)
        elif letra in alfabeto:
            posicao = alfabeto.index(letra)
            posicoes.append(posicao)
        else:
            print("Escreva sem acentos")
            return listagem_palavra()
    return alfabeto, lista_palavra, posicoes
cifra()