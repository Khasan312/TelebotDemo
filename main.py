import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
import markups as nav
from db import Database

TOKEN = '5203636918:AAEDMv7gz3cfkN37s1CAZ8PfGE6kyZQ8rBc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

class Form(StatesGroup):
    name = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Укажите ваш ник')
        # await Form.name.set()
        # await message.reply('hi maaaan')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы', reply_markup=nav.mainMenu)  
        # print("➡ msg :", msg)


@dp.message_handler() 
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '👨Профиль':
            user_nickname = 'Ваш ник: ' + db.get_nickname(message.from_user.id)
            await bot.send_message(message.from_user.id, user_nickname)  

        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if(len(message.text) > 15):
                    await bot.send_message(message.from_user.id, 'никнэйм не должен превышать 15 символов')
                elif '@' in  message.text or '/' in message.text:
                   await bot.send_message(message.from_user.id, 'вы ввели запрещенный символ')
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'Готово')
                    await bot.send_message(message.from_user.id, 'Регистрация прошла успешно', reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, 'Что?')



# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.chat.type == 'private':
#         if message.text == 'Профиль':
#             user_nickname = 'ваш ник: ' + db.get_nickname(message.from_user.id)
#             await bot.send_message(message.from_user.id, user_nickname)

#         else:
#             if db.get_signup(message.from_user.id) == 'signup':
#                 if(len(message.text) > 15):
#                     await bot.send_message(message.from_user.id, 'никнэйм не должен превышать 15 символов')
#                 elif '@' in  message.text or '/' in message.text:
#                    await bot.send_message(message.from_user.id, 'вы ввели запрещенный символ')
#                 else:
#                     db.set_nickname(message.from_user.id, message.text)
#                     await bot.send_message(message.from_user.id, 'Регистрация прошла успешно', reply_markup=nav.mainMenu)
#             else:
#                         await bot.send_message(message.from_user.id, 'Что?')







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)