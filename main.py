import telebot
from telebot import types
import PIL
from PIL import Image
from requests import get

commands = {"привет": "привет",
            "мур": "мур"}

bot = telebot.TeleBot('token')

markup = types.InlineKeyboardMarkup()
markup2 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("text", url='example')
button2 = types.InlineKeyboardButton("text", url='example')
markup.add(button1)
markup2.add(button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() in commands:
        bot.send_message(message.chat.id, commands[message.text.lower()].format(message.from_user))
    elif message.text.lower() == "автор":
        bot.send_message(message.chat.id, "Мой хозяин".format(message.from_user), reply_markup=markup2)
    else:
        bot.send_message(message.chat.id, 'Что ?')


bot.polling()