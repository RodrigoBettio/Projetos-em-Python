from banco_questoes import BANCO_DADOS
from modelo_questao import Questao
from quiz_controle import QuizControle

banco_questoes = []
for questao in BANCO_DADOS:
    texto_questao = questao ["questao"]
    resposta_questao = questao["resposta_correta"] #Pega do dicionário os respectivos values
    nova_questao = Questao(texto_questao, resposta_questao ) #Passar o texto e a resposta da questão pra classe modelo
    banco_questoes.append(nova_questao)

quiz = QuizControle(banco_questoes) #Classe para a lógica total do programa

while quiz.ainda_tem_perguntas():
    quiz.proxima_pergunta()
    

print("Você completou o quiz")
print(f"Sua pontuação foi de: {quiz.pontuacao}/{quiz.numero_pergunta}")