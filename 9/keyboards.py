from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="Вэб камеры",
                           url="https://egegesh.ru/online/sheregesh-kaskad-gora")
ib2 = InlineKeyboardButton(text="Погода",
                           url="https://egegesh.ru/weather")
ib3 = InlineKeyboardButton(text="Схема трасс",
                           url="https://www.sheregesh.su/skhema-gornolyzhnykh-trass-v-sheregeshe")
ib4 = InlineKeyboardButton(text="Шерегеш в VK",
                           url="https://vk.com/gesh_info")

ikb.add(ib1).add(ib2).add(ib3).add(ib4)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
b = KeyboardButton(text="/Link")
kb.add(b)