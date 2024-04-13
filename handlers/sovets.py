import asyncio
import os
import random

from aiogram import Router, F, types, Bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from dotenv import load_dotenv

from keyboards.keyboard_actions import sovets_markup
from source.main_text import main_texts
from keyboards.main_menu import main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from source.sovets_text import sovets_list


router = Router()
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)


@router.callback_query(F.data == 'mary_sovets')
async def get_sovets(call: CallbackQuery, state: FSMContext):
    await bot.send_message(-1002054778396, f'@{call.from_user.username}, Перешел в советы')
    await state.clear()
    count = random.randint(0, len(sovets_list) - 1)
    if call.message.content_type == ContentType.PHOTO:
        photo = FSInputFile("source/photo_sovet.jpg")
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=sovets_list[count]), reply_markup=sovets_markup)
    else:
        photo = FSInputFile("source/photo_sovet.jpg")
        await call.message.answer_photo(photo=photo, caption=sovets_list[count], reply_markup=sovets_markup)


@router.callback_query(F.data == 'button_3')
async def otziv(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await bot.send_message(-1002054778396, f'@{call.from_user.username}, Перешел в отзывы')
    photo_1 = FSInputFile('source/otzivi/ot_1.jpg')
    photo_2 = FSInputFile('source/otzivi/ot_2.jpg')
    photo_4 = FSInputFile('source/otzivi/ot_3.jpg')
    photo_5 = FSInputFile('source/otzivi/ot_4.jpg')
    photo_6 = FSInputFile('source/otzivi/ot_5.jpg')
    photo_7 = FSInputFile('source/otzivi/ot_6.jpg')

    media = [InputMediaPhoto(media=photo_4), InputMediaPhoto(media=photo_1), InputMediaPhoto(media=photo_5),
             InputMediaPhoto(media=photo_6), InputMediaPhoto(media=photo_7)]
    await call.message.answer_media_group(media=media)
    await call.message.answer_photo(photo=photo_2, caption='Жду вас на консультации', reply_markup=main_markup)
