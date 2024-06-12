from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да')],
    [KeyboardButton(text='Нет')]
], resize_keyboard=True, one_time_keyboard=True)

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да')],
    [KeyboardButton(text='Нет')]
], resize_keyboard=True, one_time_keyboard=False)
