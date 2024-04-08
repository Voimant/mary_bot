import random

from aiogram import Router, F
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
    photo = FSInputFile("source/photo_sovet.jpg")
    if call.message.content_type == ContentType.PHOTO:
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=sovets_list[count],
                                                            parse_mode='Markdown'),reply_markup=sovets_markup)
    else:
        await call.message.answer(sovets_list[count], reply_markup=sovets_markup)