from aiogram import Router, Bot, F, Dispatcher
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# from keyboards.start_test import kb
from keyboards.test import question
from utils.functions import send_questions
from utils.states import QuestionsState

router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name} 👋!\nДобро пожаловать в нашего бота🤖\nдля прохождения"
                         f" профориентационного теста, который поможет определить вашу возможную будущую профессию!🧑‍🎓")
    await message.answer("Желаете пройти тест?")


# Хэндлер для начала самого теста (подтверждение от пользователя)
@router.message(F.text.lower().in_(['да', 'хочу', 'желаю']))
async def positive_answer(message: Message, state: FSMContext):
    await message.answer(
        text=f'<u>1-й вопрос:</u>\n\n<b>{send_questions(number=1)}</b>',
        reply_markup=await question(1))
    await state.set_state(QuestionsState.first)


# Хэндлер на отмену теста
@router.message(F.text.lower().in_(['нет', 'не хочу', 'в другой раз']))
async def negative_answer(message: Message, state: FSMContext):
    await message.answer(text='Очень жаль 😔\nВы всегда сможете пройти тест, воспользовавшись командой /start')
    await state.clear()


# Первый вопрос
@router.message(QuestionsState.first)
async def first(message: Message, state: FSMContext):
    print(message.text)
    # save_first()
    data = await state.get_data()
    print(data)
    await state.update_data(numbers=numbers,
                            used_numbers=used_numbers)
    await message.answer(
        text=f'<u>2-й вопрос:</u>\n\n<b>{send_questions(number=2)}</b>',
        reply_markup=await question(2))
    # await state.update_data(numbers=numbers,
    #                         used_numbers=used_numbers)
    await state.set_state(QuestionsState.second)
