import telebot;
from config import TOKEN;
from handlers import start;
from data.database import sql_connect


bot = telebot.TeleBot(TOKEN)

db = sql_connect()
cursor = db.cursor()

user_data = {}  # Foydalanuvchilar uchun vaqtincha ma'lumot saqlanadigan joy

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Iltimos, ismingizni yuboring:")
    user_data[chat_id] = {}  # Bo‘sh lug‘at tayyorlaymiz
    bot.register_next_step_handler(message, process_name_step)

def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    user_data[chat_id]['name'] = name

    bot.send_message(chat_id, "Iltimos, yoshingizni yuboring:")
    bot.register_next_step_handler(message, process_age_step)

def process_age_step(message):
    chat_id = message.chat.id
    age = message.text
    user_data[chat_id]['age'] = age

    bot.send_message(chat_id, "Iltimos, telefon raqamingizni yuboring:")
    bot.register_next_step_handler(message, process_phone_step)

def process_phone_step(message):
    chat_id = message.chat.id
    phone = message.text
    user_data[chat_id]['phone'] = phone

    # Ma'lumotlarni bazaga yozish
    name = user_data[chat_id]['name']
    age = user_data[chat_id]['age']
    phone = user_data[chat_id]['phone']

    cursor.execute(
        "INSERT INTO foydalanuvchi (name, yoshi, tel) VALUES (%s, %s, %s)",
        (name, age, phone)
    )
    db.commit()

    bot.send_message(chat_id, f"{name} ma'lumotlaringiz bazaga saqlandi. Rahmat!")
    # Tozalash
    del user_data[chat_id]
@bot.message_handler(func=lambda  message:True)
def save_baza(message):
    name = message.text

    cursor.execute("INSERT INTO foydalanuvchi (name) VALUES (%s)", (name,))
    db.commit()

    bot.reply_to(message, f"{name} ismli foydalanuvchi bazaga qo'shildi")
    


# @bot.message_handler(commands=["help"])
# def help_1(message):
#     help1.yordam(message)



bot.polling()