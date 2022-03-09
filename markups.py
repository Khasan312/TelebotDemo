from threading import main_thread
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnProfile = KeyboardButton("👨Профиль")
btnSub = KeyboardButton("💻Меню")


mainMenu = InlineKeyboardMarkup(row_width=2)
# btnPosition = InlineKeyboardButton(text='Кнопка', callback_data='btnPosition')


# mainMenu.insert(btnPosition)





mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSub)


