import asyncio
import random

from aiogram import Router, F, types
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto

from keyboards.keyboard_actions import sovets_markup
from source.main_text import main_texts
from keyboards.main_menu import main_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from source.sovets_text import sovets_list


router = Router()


@router.callback_query(F.data == 'mary_sovets')
async def get_sovets(call: CallbackQuery, state: FSMContext):
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
    photo_1 = FSInputFile('source/otzivi/ot_1.jpg')
    photo_2 = FSInputFile('source/otzivi/ot_2.jpg')
    photo_4  = FSInputFile('source/otzivi/ot_3.jpg')

    media = [InputMediaPhoto(media=photo_1, caption='Отзывы клиентов'), InputMediaPhoto(media=photo_2), InputMediaPhoto(media=photo_4)]
    await call.message.answer_media_group(media=media)
    await asyncio.sleep(5)
    photo_3 = FSInputFile('source/mzg.jpg')
    await call.message.answer_photo(photo=photo_3, caption='Жду вас на консультации', reply_markup=main_markup)
