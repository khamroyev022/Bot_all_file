import telebot 
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


def start(message): 
    first_name = message.from_user.first_name 

    if first_name:
        bot.reply_to(message,f"salom {first_name} xush kelipsiz botga ro'yxatdan otish uchun ismingizni kiriting")
    else:
        bot.reply_to(message,"Salom,botga xush kelipsz")