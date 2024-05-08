import random
def geradorDeSenhas():
    #Quantas letras você quer em sua senha?
    #Quantos símbolos você quer em sua senha?
    #Quantos números você quer em sua senha?
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("|| Seja Bem-Vindo ao lugar aonde você pode gerar senhas fortes, sem ter que bater no teclado para isso... ||")
    numLetras = int(input("Para começar...\nQual o número de letras que você quer em sua senha?"))
    numNumeros = int(input("E o número de números?"))
    numSimbolos = int(input("Para finalizarmos... qual o número de símbolos que você quer na senha?"))
    
    letrasUsuario = random.sample(letras, numLetras)
    numerosUsuario = random.sample(numeros, numNumeros)
    simbolosUsuario = random.sample(simbolos, numSimbolos)

    senha = letrasUsuario + numerosUsuario + simbolosUsuario
    random.shuffle(senha)
    senha_str = ''.join(senha) 
    print(f"Sua senha gerada é: {senha_str}")
    print("Não esqueça de guardar a senha com segurança. Obrigado por utilizar :)")
geradorDeSenhas()