from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
trainer= ListTrainer(bot)

for file in os.listdir('C:\\Users\\sudhi\\Downloads\\pycharm\\venv\\Lib\\site-packages\\chatterbot_corpus\\data\\english\\'):
    data = open('C:\\Users\\sudhi\\Downloads\\pycharm\\venv\\Lib\\site-packages\\chatterbot_corpus\\data\\english\\' + file, 'r').readlines()
    trainer.train(data)

while True:
    message = input('You:')
    if message.strip()!=  "Bye":
        reply = bot.get_response(message)
        print('ChatBot: ', reply)
    if message.strip() == 'Bye':
        print("ChatBot : Bye")
        break

