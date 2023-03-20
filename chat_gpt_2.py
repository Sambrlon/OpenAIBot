#importing the necessary libraries
import telebot
import requests
from telebot import types
import openai

#creating the bot
bot = telebot.TeleBot("6156348707:AAGkB5qG_Bq5k5SHdYvpMV-ixs1CKOApa2U")

#handling the start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    #sending the welcome message
    bot.reply_to(message, "Hello! I'm a bot powered by the OpenAI API. Ask me any question and I'll try to answer it!")

#handling user messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    #getting the user's question
    question = message.text
    #sending the question to the OpenAI API
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions',
    json={
        "engine": "text-davinci-003",

        "prompt": f"{message.text}",
        "max_tokens": 1024,
        "n": 1,
        "stop" : None,
        "temperature": 0.5,
        
    },
    headers={
        "Authorization": "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"
    })
    #extracting the answer from the OpenAI API response
    answer = response.json()["choices"][0]["text"]
    #sending the answer to the user
    bot.reply_to(message, answer)

#running the bot
bot.polling()