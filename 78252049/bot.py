import os

import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    pass


@bot.callback_query_handler(func=lambda callback: True)
def handle_query(call):
    pass


bot.polling(non_stop=True)
