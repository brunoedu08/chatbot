from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot')

conversa = open('frases.txt', 'r').readlines()

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    print('Bot: ', resposta)
