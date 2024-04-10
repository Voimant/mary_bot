import os
import random

from aiogram import Router, F, Bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from source.main_text import main_texts
from keyboards.main_menu import main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from dotenv import load_dotenv


router = Router()
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)


@router.message()
async def get_say(mess: Message, state: FSMContext):
    await state.clear()
    photo = FSInputFile("source/Машенька.jpg")
    text = [
        'Не поняла вас 🤷🏽‍♀️ выберете одну из кнопок меню',
        'Вы можете писать все что угодно, но лучше нажать кнопку',
        'Кодер старался и делал кнопки для вас, так воспользуйтесь!',
        'Ну зачем писать, если можно жать!'
    ]
    x = random.randint(0, len(text) - 1)
    await mess.answer_photo(photo=photo, caption=text[x], reply_markup=main_markup)