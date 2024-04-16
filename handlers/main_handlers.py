import os

from aiogram import Router, F, Bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from dotenv import load_dotenv

from DB.db_func import db_add_new_user, db_member
from source.main_text import main_texts
from keyboards.main_menu import main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from source.test_api import test_api

router = Router()
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)


@router.message(Command('start'))
async def cmd_start(message: Message):
    photo = FSInputFile('source/start_photo.jpg')
    await message.answer_photo(photo=photo, caption=main_texts, reply_markup=main_markup)
    try:
        await bot.send_message(-1002054778396, f'@{message.from_user.username}, Нажал старт.\n номер телефона: {message.contact.phone_number}')
        member = db_member(message.chat.id)
        if member is None:
            db_add_new_user(str(message.from_user.username), str(message.chat.id))
    except Exception as e:
        await bot.send_message(-1002054778396,
                               f'@{message.from_user.username}, Нажал старт.\n')

@router.callback_query(F.data == 'cancel')
async def cancel(call: CallbackQuery, state: FSMContext):
    photo = FSInputFile('source/start_photo.jpg')
    text = 'Вы вернулись в главное меню'
    await state.clear()
    if call.message.content_type == ContentType.PHOTO:
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                      reply_markup=main_markup)
    else:
        await call.message.delete()
        await call.message.answer_photo(photo=photo, caption=text, reply_markup=main_markup)



class Fsdata(StatesGroup):
    inn = State()

@router.callback_query(F.data == 'go_ddata')
async def get_data(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Введите ИНН организации')
    await state.set_state(Fsdata.inn)

@router.message(Fsdata.inn)
async def final_data(mess: Message, state: FSMContext):
    try:
        await state.update_data(inn=mess.text)
        data = await state.get_data()
        x = test_api(data['inn'])
        await mess.answer(x)
    except Exception as e:
        await mess.answer('Что то пошло не так, нужно проверить правильность ввода ИНН', reply_markup=main_markup)