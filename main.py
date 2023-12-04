import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, start_text
from aiogram.dispatcher.filters import Text
from keyboards_buttons import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

rep = {}

class Replyes:
    def __init__(self, id):
        self.id = id
        self.text = []

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начать", callback_data="begin"))
    await message.answer(start_text, reply_markup=keyboard)


@dp.callback_query_handler(text="begin")
async def begin(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttonWeb)
    await call.message.edit_text("Укажи желаемое направление разработки", reply_markup=keyboard)
    rep[f"{call.from_user.id}"] = Replyes(call.from_user.id)


@dp.callback_query_handler(Text(startswith="web_"))
async def OOP(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttonOOP)
    await call.message.edit_text("Должна ли использоваться ООП парадигма в проекте?", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="OOP_"))
async def performance(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonPerformance)
    await call.message.edit_text("Насколько важна производительность? ", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="performance_"))
async def security(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonSecurity)
    await call.message.edit_text("Укажите необходимость высоких критериев безопасности", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="security_"))
async def entry_level(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttonEntryLevel)
    await call.message.edit_text("Укажите порог входа", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="entry_level_"))
async def development_speed(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonDevSpeed)
    await call.message.edit_text("Насколько важна скорость разработки?", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[2])


@dp.callback_query_handler(Text(startswith="development_speed_"))
async def cross_platform(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonCrossPlatform)
    await call.message.edit_text("Важная ли кроссплатформенность? ", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="cross_platform_"))
async def frameworks(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonFrameworks)
    await call.message.edit_text("Важно ли обилие сторонних фреймворков и библиотек? ", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[2])


@dp.callback_query_handler(Text(startswith="frameworks_"))
async def select_part(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttonPart)
    await call.message.edit_text("Предпочитаемая часть разработки проектов", reply_markup=keyboard)
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[1])


@dp.callback_query_handler(Text(startswith="select_part_"))
async def end(call: types.CallbackQuery):
    rep[f"{call.from_user.id}"].text.append(call.data.split("_")[2])
    await call.message.edit_text("Спасибо за ответы! \nТест окончен" + "\n" + str(rep[f"{call.from_user.id}"].text))

if __name__ == '__main__':
    print("Бот запущен!")
    executor.start_polling(dp, skip_updates=True)