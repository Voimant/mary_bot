import os
import random

from aiogram import Router, F, Bot
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from pydantic import ValidationError
from DB.db_func import db_user_topic, db_delete_chat, db_new_chat, db_user_id
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
async def get_talk(mess: Message):
    if mess.chat.id != -1002204508059:
        topic = db_user_topic(mess.from_user.id)
        try:
            try:
                if mess.sticker is not None:
                    await bot.send_sticker(-1002204508059, mess.sticker.file_id, message_thread_id=int(topic))
                elif mess.photo is not None:
                    await bot.send_photo(-1002204508059, mess.photo[0].file_id, caption=mess.caption, message_thread_id=int(topic))
                else:
                    await bot.send_message(-1002204508059, mess.text, message_thread_id=int(topic))
            except ValidationError:
                await mess.answer('Можно отправлять Стикер, фото и картинки', reply_markup=main_markup)
        except TelegramBadRequest:
            db_delete_chat(mess.chat.id)
            topic = await bot.create_forum_topic(-1002204508059, f'{str(mess.from_user.username)}')
            db_new_chat(mess.from_user.id, mess.from_user.username, topic.message_thread_id)
            topic = db_user_topic(mess.from_user.id)
            try:
                if mess.sticker is not None:
                    await bot.send_sticker(-1002204508059, mess.sticker.file_id, message_thread_id=int(topic))
                elif mess.photo is not None:
                    await bot.send_photo(-1002204508059, mess.photo[0].file_id, caption=mess.caption, message_thread_id=int(topic))
                else:
                    await bot.send_message(-1002204508059, mess.text, message_thread_id=int(topic))
            except ValidationError:
                await mess.answer('Можно отправлять Стикер, фото и картинки', reply_markup=main_markup)

    elif mess.chat.id == -1002204508059 and mess.from_user.is_bot is False:
        topic = mess.message_thread_id
        user_id = db_user_id(topic)
        if mess.sticker is not None:
            await bot.send_sticker(int(user_id), mess.sticker.file_id)
        elif mess.photo is not None:
            await bot.send_photo(int(user_id), mess.photo[0].file_id, caption=mess.caption)
        else:
            await bot.send_message(int(user_id), mess.text)