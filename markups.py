from threading import main_thread
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnProfile = KeyboardButton("👨Профиль")
btnSub = KeyboardButton("💻Меню")


# mainMenu = InlineKeyboardMarkup(row_width=2)
# btnPosition = InlineKeyboardButton(text='Кнопка', callback_data='btnPosition')
# keyboard = types.InlineKeyboardMarkup(row_width=2, text='hello')

# mainMenu.insert(keyboard)





mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnProfile, btnSub)


