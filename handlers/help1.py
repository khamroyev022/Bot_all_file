import telebot 
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def yordam(message):
    first_name = message.from_user.first_name.user.id
    bot.reply_to(message,f'Sizga qanday yordam bera olamana {first_name}')
