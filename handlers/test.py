import os

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.test import kb, kb1
from utils.db import UserDatabase
from utils.functions import send_questions
from utils.states import QuestionsState
from utils.functions import result

router = Router()


# start
@router.message(Command(commands=['start']))
async def start_command(message: Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.first_name} 👋!\nДобро пожаловать в нашего бота🤖\nДля прохождения"
                         f" профориентационного теста, который поможет определить вашу возможную будущую профессию!🧑‍🎓")
    await message.answer("Желаете пройти тест?", reply_markup=kb1)
    await state.set_state(QuestionsState.wait)


# Хэндлер для ввода ФИО
@router.message(F.text.lower().in_(['да', 'хочу', 'желаю']), QuestionsState.wait)
async def positive_answer(message: Message, state: FSMContext):
    await message.answer(text="Введите ФИО (в полном виде):")
    await state.set_state(QuestionsState.fio)
    db = UserDatabase(os.getenv('DATABASE_NAME'))
    # Добавление пользователя
    db.add_user(message.from_user.id, message.from_user.username)


# Переход в состояние ввода ФИО. Реагирует только на корректно введённое ФИО
@router.message(QuestionsState.fio, lambda message: message.text == message.text.isalpha() or ' ' in message.text)
async def correct_fio(message: Message, state: FSMContext):
    db = UserDatabase(os.getenv('DATABASE_NAME'))
    # Добавление полного имени пользователя
    db.add_full_name(message.from_user.id, message.text)
    await message.answer("Теперь введите Ваше учебное заведение:")
    await state.set_state(QuestionsState.institution)


# Хэндлер на неправильно введённое ФИО
@router.message(QuestionsState.fio)
async def incorrect_fio(message: Message):
    await message.answer('Введите ФИО (Иванов Иван Иванович - пример)')


# Переход в состояние ввода уч. заведения. Реагирует только на корректно введённое ФИО
@router.message(QuestionsState.institution)
async def institution(message: Message, state: FSMContext):
    db = UserDatabase(os.getenv('DATABASE_NAME'))
    # Добавление учебного заведения пользователя
    db.add_institution(message.from_user.id, message.text)
    await message.answer(text="Замечательно, приступим к тесту 😊")
    await message.answer(
        text=f'<b><u>1-й вопрос❓:</u></b>\n\n<b>{send_questions(number=1)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.first)


# Хэндлер на отмену теста
@router.message(F.text.lower().in_(['нет', 'не хочу', 'в другой раз']), QuestionsState.wait)
async def negative_answer(message: Message, state: FSMContext):
    await message.answer(text='Очень жаль 😔\nВы всегда сможете пройти тест, воспользовавшись командой /start')
    await state.clear()


# Первый вопрос
@router.message(QuestionsState.first)
async def first(message: Message, state: FSMContext):
    await state.update_data(nature=0, technic=0, sign=0, art=0, human=0)
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 1
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>2-й вопрос❓:</u></b>\n\n<b>{send_questions(number=2)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.second)


# Второй вопрос
@router.message(QuestionsState.second)
async def second(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 1
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>3-й вопрос❓:</u></b>\n\n<b>{send_questions(number=3)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.third)


# Третий вопрос
@router.message(QuestionsState.third)
async def third(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 1
    await state.update_data(art=art)
    await message.answer(
        text=f'<b><u>4-й вопрос❓:</u></b>\n\n<b>{send_questions(number=4)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.fourth)


# Четвертый вопрос
@router.message(QuestionsState.fourth)
async def fourth(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 1
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>5-й вопрос❓:</u></b>\n\n<b>{send_questions(number=5)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.fifth)


# Пятый вопрос
@router.message(QuestionsState.fifth)
async def fifth(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 1
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>6-й вопрос❓:</u></b>\n\n<b>{send_questions(number=6)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.sixth)


# Шестой вопрос
@router.message(QuestionsState.sixth)
async def sixth(message: Message, state: FSMContext):
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 1
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>7-й вопрос❓:</u>\n\n<b></b>{send_questions(number=7)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.seventh)


# Седьмой вопрос
@router.message(QuestionsState.seventh)
async def seventh(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 1
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>8-й вопрос❓:</u></b>\n\n<b>{send_questions(number=8)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.eighth)


# Восьмой вопрос
@router.message(QuestionsState.eighth)
async def eight(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 1
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>9-й вопрос❓:</u></b>\n\n<b>{send_questions(number=9)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.ninth)


# Девятый вопрос
@router.message(QuestionsState.ninth)
async def ninth(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 2
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>10-й вопрос❓:</u></b>\n\n<b>{send_questions(number=10)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.tenth)


# Десятый вопрос
@router.message(QuestionsState.tenth)
async def tenth(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 2
    await state.update_data(art=art)
    await message.answer(
        text=f'<b><u>11-й вопрос❓:</u></b>\n\n<b>{send_questions(number=11)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.eleventh)


# Одиннадцатый вопрос
@router.message(QuestionsState.eleventh)
async def eleventh(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 1
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>12-й вопрос❓:</u></b>\n\n<b>{send_questions(number=12)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twelfth)


# Двенадцатый вопрос
@router.message(QuestionsState.twelfth)
async def twelfth(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 1
    await state.update_data(art=art)
    await message.answer(
        text=f'<b><u>13-й вопрос❓:</u></b>\n\n<b>{send_questions(number=13)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.thirteenth)


# Тринадцатый вопрос
@router.message(QuestionsState.thirteenth)
async def thirteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 1
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>14-й вопрос❓:</u></b>\n\n<b>{send_questions(number=14)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.fourteenth)


# Четырнадцатый вопрос
@router.message(QuestionsState.fourteenth)
async def fourteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 2
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>15-й вопрос❓:</u></b>\n\n<b>{send_questions(number=15)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.fifteenth)


# Пятнадцатый вопрос
@router.message(QuestionsState.fifteenth)
async def fifteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 2
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>16-й вопрос❓:</u>\n\n<b></b>{send_questions(number=16)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.sixteenth)


# Шестнадцатый вопрос
@router.message(QuestionsState.sixteenth)
async def sixteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 2
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>17-й вопрос❓:</u></b>\n\n<b>{send_questions(number=17)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.seventeenth)


# Семнадцатый вопрос
@router.message(QuestionsState.seventeenth)
async def seventeenth(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 2
    await state.update_data(art=art)
    await message.answer(
        text=f'<b><u>18-й вопрос❓:</u></b>\n\n<b>{send_questions(number=18)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.eighteenth)


# Восемнадцатый вопрос
@router.message(QuestionsState.eighteenth)
async def eighteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 2
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>19-й вопрос❓:</u></b>\n\n<b>{send_questions(number=19)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.nineteenth)


# Девятнадцатый вопрос
@router.message(QuestionsState.nineteenth)
async def nineteenth(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 2
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>20-й вопрос❓:</u></b>\n\n<b>{send_questions(number=20)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twentieth)


# Двадцатый вопрос
@router.message(QuestionsState.twentieth)
async def twentieth(message: Message, state: FSMContext):
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 1
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>21-й вопрос❓:</u></b>\n\n<b>{send_questions(number=21)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_first)


# Двадцать первый вопрос
@router.message(QuestionsState.twenty_first)
async def twenty_first(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 1
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>22-й вопрос❓:</u></b>\n\n<b>{send_questions(number=22)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_second)


# Двадцать второй вопрос
@router.message(QuestionsState.twenty_second)
async def twenty_second(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 1
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>23-й вопрос❓:</u></b>\n\n<b>{send_questions(number=23)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_third)


# Двадцать третий вопрос
@router.message(QuestionsState.twenty_third)
async def twenty_third(message: Message, state: FSMContext):
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 2
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>24-й вопрос❓:</u></b>\n\n<b>{send_questions(number=24)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_fourth)


# Двадцать четвёртый вопрос
@router.message(QuestionsState.twenty_fourth)
async def twenty_fourth(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 1
    await state.update_data(art=art)
    await message.answer(
        text=f'<b><u>25-й вопрос❓:</u></b>\n\n<b>{send_questions(number=25)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_fifth)


# Двадцать пятый вопрос
@router.message(QuestionsState.twenty_fifth)
async def twenty_fifth(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 2
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>26-й вопрос❓:</u></b>\n\n<b>{send_questions(number=26)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_sixth)


# Двадцать шестой вопрос
@router.message(QuestionsState.twenty_sixth)
async def twenty_sixth(message: Message, state: FSMContext):
    data = await state.get_data()
    technic = data['technic']
    if message.text.lower() == "да":
        technic += 1
    await state.update_data(technic=technic)
    await message.answer(
        text=f'<b><u>27-й вопрос❓:</u></b>\n\n<b>{send_questions(number=27)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_seventh)


# Двадцать седьмой вопрос
@router.message(QuestionsState.twenty_seventh)
async def twenty_seventh(message: Message, state: FSMContext):
    data = await state.get_data()
    human = data['human']
    if message.text.lower() == "да":
        human += 1
    await state.update_data(human=human)
    await message.answer(
        text=f'<b><u>28-й вопрос❓:</u></b>\n\n<b>{send_questions(number=28)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_eighth)


# Двадцать восьмой вопрос
@router.message(QuestionsState.twenty_eighth)
async def twenty_eighth(message: Message, state: FSMContext):
    data = await state.get_data()
    nature = data['nature']
    if message.text.lower() == "да":
        nature += 1
    await state.update_data(nature=nature)
    await message.answer(
        text=f'<b><u>29-й вопрос❓:</u></b>\n\n<b>{send_questions(number=29)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.twenty_ninth)


# Двадцать девятый вопрос
@router.message(QuestionsState.twenty_ninth)
async def twenty_ninth(message: Message, state: FSMContext):
    data = await state.get_data()
    sign = data['sign']
    if message.text.lower() == "да":
        sign += 1
    await state.update_data(sign=sign)
    await message.answer(
        text=f'<b><u>30-й вопрос❓:</u></b>\n\n<b>{send_questions(number=30)}</b>',
        reply_markup=kb)
    await state.set_state(QuestionsState.thirtieth)


# Тридцатый вопрос
@router.message(QuestionsState.thirtieth)
async def thirtieth(message: Message, state: FSMContext):
    data = await state.get_data()
    art = data['art']
    if message.text.lower() == "да":
        art += 1
    await state.update_data(art=art)
    data = await state.get_data()

    # Получаем результат и дополнительный текст
    final_result, additional_text = result(data)

    # Отправляем основной результат
    await message.answer(text=final_result)

    # Отправляем дополнительное сообщение
    await message.answer(text=additional_text)

    db = UserDatabase(os.getenv('DATABASE_NAME'))
    # Добавление результата пользователя
    db.add_result(message.from_user.id, data)


# help
@router.message(Command(commands=['help']))
async def start_command(message: Message):
    await message.answer("""👋 Добро пожаловать в ПрофОриентир!

🔍 <b>Как использовать бота:</b>

1. <b>Начало теста:</b> Нажмите /start, чтобы начать профориентационный тест.
2. <b>Ответы на вопросы:</b> Последовательно отвечайте на 30 вопросов.
3. <b>Результаты:</b> После завершения теста вы получите анализ ваших склонностей и рекомендации по профессиям.

📚 <b>Доступные команды:</b>

/start - Начать тест
/help - Получить помощь

📊 <b>Категории профессий:</b>

• Природный мир: Профессии, связанные с растениями и животными.
• Технологический мир: Технические и инженерные профессии.
• Мир знаков и цифр: Работа с текстами, цифрами и схемами.
• Творческий мир: Профессии в сфере искусства и дизайна.
• Социальный мир: Профессии, требующие взаимодействия с людьми.

❓ <b>Поддержка</b>:
Если у вас возникли вопросы или нужна помощь, обратитесь к нам в телеграмм за поддержкой: https://t.me/Championnsss1

🚀 Начните свой путь к успешной карьере с ПрофОриентир!""")


# hz
@router.message()
async def start_command(message: Message):
    await message.answer("Извините, но я не знаю такой команды")
