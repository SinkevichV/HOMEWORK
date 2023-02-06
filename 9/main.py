from aiogram import Bot, executor, Dispatcher, types
from logg import logging
from config import TOKEN_API
from keyboards import kb, ikb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я был запущен!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    logging.info('Start bot')
    await message.answer(text='Добро пожаловать в меню с полезными ссылками',
                         reply_markup=kb)

@dp.message_handler(commands=['Link'])
async def links_command(message: types.Message):
    logging.info('select Link')
    await message.answer(text='Выберите ссылку...',
                         reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
