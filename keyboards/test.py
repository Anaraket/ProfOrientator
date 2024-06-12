import os

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.questions import questions_base


# Генератор клавиатуры
async def question(number):
    builder = ReplyKeyboardBuilder()
    answers = questions_base[number - 1]  # Учитывая, что номер вопроса начинается с 1
    for i in answers['answers']:
        builder.add(KeyboardButton(text=i))
    return builder.adjust(1).as_markup(resize_keyboard=True)


