from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('👨Профиль')
btnSub = KeyboardButton('💻Меню')

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
mainMenu.add(btnProfile, btnSub)