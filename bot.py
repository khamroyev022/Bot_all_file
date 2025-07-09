from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom! Bot ishga tushdi.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
