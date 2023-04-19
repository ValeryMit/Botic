from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



bot = Bot(token='5869963349:AAH28nFv8e3WImIAMg3K-qZgKR1ex9vCIEg')
dp = Dispatcher(bot)

start_btn = ReplyKeyboardMarkup(resize_keyboard=True)
start_btn.add(KeyboardButton('Старт'))
start_btn.add(KeyboardButton('Привет'))

second_btn = ReplyKeyboardMarkup(resize_keyboard=True)
second_btn.add(KeyboardButton('Поехали'))

third_btn = ReplyKeyboardMarkup(resize_keyboard=True)
third_btn.add(KeyboardButton('Книги?'))
third_btn.add(KeyboardButton('Или может быть фильмы?'))

inline_btn = InlineKeyboardMarkup()
inline_btn.add(InlineKeyboardButton('Да', callback_data='inline_btn1'))
inline_btn.add(InlineKeyboardButton('Нет', callback_data='inline_btn2'))

line_btn = InlineKeyboardMarkup()
line_btn.add(InlineKeyboardButton('Любовные романы?', callback_data='line_btn1'))
line_btn.add(InlineKeyboardButton('Детективы?', callback_data='line_btn2'))

ine_btn = InlineKeyboardMarkup()
ine_btn.add(InlineKeyboardButton('Дорамы?', callback_data='ine_btn1'))
ine_btn.add(InlineKeyboardButton('Турецкие сериалы?', callback_data='ine_btn2'))

ne_btn = InlineKeyboardMarkup()
ne_btn.add(InlineKeyboardButton('Озвучка SoftBox', callback_data='ne_btn1'))
ne_btn.add(InlineKeyboardButton('Что-то другое', callback_data='ne_btn2'))

e_btn = InlineKeyboardMarkup()
e_btn.add(InlineKeyboardButton('Винченцо', url = 'https://softboxtv.com/doramy-s-russkoj-ozvuchkoj/6441-vincenzo-2021-smotret-onlajn.html' ))
e_btn.add(InlineKeyboardButton('История девятихвостого лиса', callback_data='e_btn2'))
e_btn.add(InlineKeyboardButton('Пентхаус', callback_data='e_btn3'))
e_btn.add(InlineKeyboardButton('Истинная красота', callback_data='e_btn4'))

o_btn = InlineKeyboardMarkup()
o_btn.add(InlineKeyboardButton('https://softboxtv.com/doramy-s-russkoj-ozvuchkoj/6441-vincenzo-2021-smotret-onlajn.html', callback_data='o_btn1'))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Чего бы вы хотели?", reply_markup=start_btn)
    

@dp.message_handler(text='Старт')
async def echo(message: types.Message):
    await message.answer("Вам уже нравится наш бот?", reply_markup=inline_btn)
@dp.message_handler(text='Привет')
async def echo(message: types.Message):
    await message.answer("Вы готовы начать работу?", reply_markup=inline_btn)

@dp.callback_query_handler(text='inline_btn2')
async def inline_btn1(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Тогда увмдимся потом!', reply_markup=start_btn )

@dp.callback_query_handler(text='inline_btn1')
async def inline_btn1(callback: types.CallbackQuery):
    await callback.message.answer('Тогда приступим!', reply_markup=second_btn )

@dp.message_handler(text='Поехали')
async def echo(message: types.Message):
    await message.answer("Выбирай:", reply_markup=third_btn)
    
    
@dp.message_handler(text='Книги?')
async def echo(message: types.Message):
    await message.answer("Какой жанр предпочитаете?", reply_markup=line_btn)
    
@dp.message_handler(text='Или может быть фильмы?')
async def echo(message: types.Message):
    await message.answer("Что предпочитаете?", reply_markup=ine_btn)
    
@dp.callback_query_handler(text='ine_btn1')
async def inline_btn1(callback: types.CallbackQuery):
    await callback.message.answer('Может быть есть предпочтения?', reply_markup=ne_btn )


@dp.callback_query_handler(text='ne_btn1')
async def inline_btn1(callback: types.CallbackQuery):
    await callback.message.answer('Что то из этого?', reply_markup= e_btn )


executor.start_polling(dp)


