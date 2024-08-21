class QuizControle:

    def __init__(self, lista_perguntas):
        self.numero_pergunta = 0
        self.pontuacao = 0
        self.lista_perguntas = lista_perguntas

    def ainda_tem_perguntas(self):
        return self.numero_pergunta < len(self.lista_perguntas)

    def proxima_pergunta(self):
        pergunta_atual = self.lista_perguntas[self.numero_pergunta]
        self.numero_pergunta += 1
        resposta_usuario = input(f"Pergunta {self.numero_pergunta}: {pergunta_atual.texto} (Verdadeiro/Falso): ").strip().lower()
        self.verificar_resposta(resposta_usuario, pergunta_atual.resposta)

    def verificar_resposta(self, resposta_usuario, resposta_correta):
        if resposta_usuario.lower() == resposta_correta.lower():
            self.pontuacao += 1
            print("Você acertou!")
        else:
            print("Você errou.")
        print(f"A resposta correta era: {resposta_correta}.")
        print(f"Sua pontuação atual é: {self.pontuacao}/{self.numero_pergunta}")
        print("\n")
