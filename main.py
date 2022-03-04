import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import markups as nav
from db import Database

TOKEN = '5203636918:AAEDMv7gz3cfkN37s1CAZ8PfGE6kyZQ8rBc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db = Database('database.db')

class Form(StatesGroup):
    name = State()
    birth_date = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    # print(message)
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Hi!\nI'm Makers!\nPowered by aiogram.")
        # if m is True:
            # await bot.send_message(message.from_user.id, 'ваша дата рождения')
        # await message.reply('name')
        await bot.send_message(message.from_user.id, 'Укажите ваш ник')
        await Form.name.set()

        # await message.reply('hi maaaan')
    else:
        await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы', reply_markup=nav.mainMenu)  
        # print("➡ msg :", msg)


@dp.message_handler(state=Form.name) 
async def process_name(message: types.Message, state):
    message.text # hasan
    # state.proxy()
    await bot.send_message(message.from_user.id, 'введи дату рождение ')
    await Form.next()

@dp.message_handler(state=Form.birth_date) 
async def process_birthday(message: types.Message, state):
    await message.reply('Birt')
    # message 
    # Form.next()
    async with state.proxy() as data:
        print("➡ data BEFORE :", data)
        data['birth_date'] = message.text
        print("➡ data AFTER :", data)
    
    await bot.send_message(message.from_user.id, "Сделано")

@dp.message_handler() 
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '👨Профиль':
            date_birth = 'Дата рождения: ' + db.get_date_of_birth(message.from_user.id)
            user_nickname = 'Ваш ник: ' + db.get_nickname(message.from_user.id)
            await bot.send_message(message.from_user.id, user_nickname)
            await bot.send_message(message.from_user.id, date_birth)  

        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if(len(message.text) > 15):
                    await bot.send_message(message.from_user.id, 'никнэйм не должен превышать 15 символов и больше 2 символов')
                elif '@' in  message.text or '/' in message.text:
                   await bot.send_message(message.from_user.id, 'вы ввели запрещенный символ')
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_date_of_birth(message.from_user.id, message.text)
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