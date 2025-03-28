from pprint import pprint
from re import fullmatch
from time import sleep
import phonenumbers
from aiogram.types import FSInputFile, InputMedia, InputMediaPhoto
from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from DB.db_func import db_cats_list, db_sub_cats_list, search_delo, db_records
from keyboards.keyboard_actions import paginator_markup, record_markup, egrul_markup
from keyboards.main_menu import spec_markup, cancel_markup, contacts_markup, sub_cats_markup, main_markup, \
    sub_bank_markup
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
import os

from source.main_text import t_contacts

router = Router()
load_dotenv()
PIC_PATH = os.getenv('PIC_PATH')
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)

# @router.callback_query(F.data == 'button_2')
# async def get_specialization(call: types.CallbackQuery):
#     await call.message.answer('Мои специализации и опыт', reply_markup=spec_markup)

class Affiers(StatesGroup):
    cat = State()
    sub_cat = State()
    my_delo = State()


class Record(StatesGroup):
    name = State()
    number_phone = State()
    about = State()
    ready = State()


@router.callback_query(F.data == 'button_2')
async def get_spec(call: types.CallbackQuery, state: FSMContext):
    photo = FSInputFile("source/Машенька.jpg")
    await bot.send_message(-1002204508059, f'@{call.from_user.username}, перешел в мои специализации')
    #await call.message.answer_photo(photo=photo, caption="Моя специализация и опыт",
    #                                reply_markup=spec_markup())
    await call.message.edit_media(media=InputMediaPhoto(media=photo, caption="Моя специализация и опыт", parse_mode='Markdown'),
                                  reply_markup=spec_markup())
    await state.set_state(Affiers.cat)


@router.callback_query(Affiers.cat)
async def get_cats(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(cat=call.data)
    data = await state.get_data()
    if data['cat'] == 'внесение изменений в ЕГРЮЛ':
        photo = FSInputFile('source/vnesenie_izmenenii.jpg')
    else:
        photo = FSInputFile("source/Машенька.jpg")
    print(data['cat'])
    await bot.send_message(-1002204508059, f'@{call.from_user.username}, нажал {call.data}')
    # await call.message.edit_text('выберете подкатегорию', reply_markup=sub_cats_markup(data['cat']))
    if data['cat'] == 'банкротство':
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption='выберите подкатегорию', parse_mode='Markdown'),
                                      reply_markup=sub_bank_markup(data['cat']))
    else:
        await call.message.edit_media(
            media=InputMediaPhoto(media=photo, caption='выберите подкатегорию', parse_mode='Markdown'),
            reply_markup=sub_cats_markup(data['cat']))
    await state.set_state(Affiers.sub_cat)


@router.callback_query(Affiers.sub_cat)
async def get_sub_cat(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(sub_cat=call.data)
    await state.update_data(my_delo=0)
    data = await state.get_data()
    x = 0
    list_affiars = search_delo(data['sub_cat'])
    photo = FSInputFile(f'{PIC_PATH}{list_affiars[x]["image_result"]}')
    if data['cat'] == 'банкротство':
        text = (f'*Дата решения*: {list_affiars[x]["date"]}\n'
                f'*Cуд (город)*: {list_affiars[x]["court"]}\n'
                f'*Сумма иска*: {list_affiars[x]["summ_plaintiff"]}\n'
                f'*Суть спора*: {list_affiars[x]["dispute"]}\n'
                f'*Результат*: {list_affiars[x]["result_court"]}\n'
                f'*Роль*: {list_affiars[x]["role"]}\n'
                f'*Выгода клиента*: {list_affiars[x]["result_client"]}\n'
                f'*Должник*: {list_affiars[x]["defendant"]}\n'
                f'*Кредитор*: {list_affiars[x]["plaintiff"]}\n'
                f'[Ссылка на судебный акт]({str(list_affiars[x]["urls"])})')
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                      reply_markup=paginator_markup)

    elif data['cat'] in ['внесение изменений в ЕГРЮЛ', 'ликвидация бизнеса']:
        text = f'{list_affiars[x]["result_court"]}'
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                      reply_markup=egrul_markup)

    elif data['cat'] in ['®️ защита Франшиз', 'семейное право']:
        text = f'{list_affiars[x]["result_court"]}'
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                      reply_markup=paginator_markup)

    else:
        text = (f'*Дата решения*: {list_affiars[x]["date"]}\n'
                f'*Cуд (город)*: {list_affiars[x]["court"]}\n'
                f'*Сумма иска*: {list_affiars[x]["summ_plaintiff"]}\n'
                f'*Суть спора*: {list_affiars[x]["dispute"]}\n'
                f'*Результат*: {list_affiars[x]["result_court"]}\n'
                f'*Роль*: {list_affiars[x]["role"]}\n'
                f'*Выгода клиента*: {list_affiars[x]["result_client"]}\n'
                f'*Истец*: {list_affiars[x]["defendant"]}\n'
                f'*Ответчик*: {list_affiars[x]["plaintiff"]}\n'
                f'[Ссылка на судебный акт]({str(list_affiars[x]["urls"])})')
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                      reply_markup=paginator_markup)
    await state.set_state(Affiers.my_delo)


@router.callback_query(Affiers.my_delo)
async def get_sub_cat(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    x = data['my_delo']
    list_affiars = search_delo(data['sub_cat'])
    if call.data == 'next':
        if x < len(list_affiars) - 1:
            x = x + 1
        else:
            x = 0
        photo = FSInputFile(f'{PIC_PATH}{list_affiars[x]["image_result"]}')
        if data['cat'] == 'банкротство':
            text = (f'*Дата решения*: {list_affiars[x]["date"]}\n'
                    f'*Cуд (город)*: {list_affiars[x]["court"]}\n'
                    f'*Сумма иска*: {list_affiars[x]["summ_plaintiff"]}\n'
                    f'*Суть спора*: {list_affiars[x]["dispute"]}\n'
                    f'*Результат*: {list_affiars[x]["result_court"]}\n'
                    f'*Роль*: {list_affiars[x]["role"]}\n'
                    f'*Выгода клиента*: {list_affiars[x]["result_client"]}\n'
                    f'*Должник*: {list_affiars[x]["defendant"]}\n'
                    f'*Кредитор*: {list_affiars[x]["plaintiff"]}\n'
                    f'[Ссылка на судебный акт]({str(list_affiars[x]["urls"])})')
            await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                          reply_markup=paginator_markup)
            await state.update_data(my_delo=x)

        elif data['cat'] in ['внесение изменений в ЕГРЮЛ', 'ликвидация бизнеса']:
            text = f'{list_affiars[x]["result_court"]}'
            await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                          reply_markup=egrul_markup)

        elif data['cat'] in ['®️ защита Франшиз', 'семейное право']:
            text = f'{list_affiars[x]["result_court"]}'
            await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'),
                                          reply_markup=paginator_markup)
            await state.update_data(my_delo=x)

        else:
            text = (f'*Дата решения*: {list_affiars[x]["date"]}\n'
                    f'*Cуд (город)*: {list_affiars[x]["court"]}\n'
                    f'*Сумма иска*: {list_affiars[x]["summ_plaintiff"]}\n'
                    f'*Суть спора*: {list_affiars[x]["dispute"]}\n'
                    f'*Результат*: {list_affiars[x]["result_court"]}\n'
                    f'*Роль*: {list_affiars[x]["role"]}\n'
                    f'*Выгода клиента*: {list_affiars[x]["result_client"]}\n'
                    f'*Истец*: {list_affiars[x]["defendant"]}\n'
                    f'*Ответчик*: {list_affiars[x]["plaintiff"]}\n'
                    f'[Ссылка на судебный акт]({str(list_affiars[x]["urls"])})')
            await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode='Markdown'), reply_markup=paginator_markup)
            await state.update_data(my_delo=x)
        await state.set_state(Affiers.my_delo)

    elif call.data == 'record':
        await state.clear()
        photo = FSInputFile("source/Машенька.jpg")
        await call.message.edit_media(
            media=InputMediaPhoto(media=photo, caption="Опишите суть вашего вопроса. Я с вами свяжусь для согласования времени онлайн консультации", parse_mode='Markdown'),
            reply_markup=cancel_markup)
        await state.set_state(Record.about)


@router.callback_query(F.data == 'record')
async def get_new_record(call: types.CallbackQuery, state:FSMContext):
    await bot.send_message(-1002204508059, f'@{call.from_user.username}, нажал Записаться на консультацию')
    await state.clear()
    photo = FSInputFile("source/Машенька.jpg")
    await call.message.edit_media(media=InputMediaPhoto(media=photo, caption="Опишите суть вашего вопроса. Я с вами свяжусь для согласования времени онлайн консультации", parse_mode='Markdown'),
                                  reply_markup=cancel_markup)
    await state.set_state(Record.about)


@router.message(Record.about)
async def get_about(mess: Message, state: FSMContext):
    if mess.text is None:
        print(mess.text)
        await mess.answer('Введите текст', reply_markup=cancel_markup)
        await state.set_state(Record.about)
    else:
        await state.update_data(about=mess.text)
        await mess.answer('Проверьте правильность данных и нажмите "заказать консультацию"',
                          reply_markup=record_markup)
        await state.set_state(Record.ready)


@router.callback_query(Record.ready)
async def get_ready(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'record_go':
        db_records(
            data['about'],
            f'https://t.me/{call.from_user.username}')
    photo = FSInputFile("source/Машенька.jpg")
    await call.message.answer_photo(photo=photo, caption='Заявка отправлена, свяжусь с вами в ближайшее время', reply_markup=main_markup)
    await bot.send_message(-1002204508059, f'#order НОВАЯ_ЗАЯВКА\n'
                                      f'@{call.from_user.username}\n'
                                      f'{data["about"]}')
    await state.clear()


@router.callback_query(F.data == 'contacts')
async def contacts(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(-1002204508059, f'@{call.from_user.username}, перешел в контакты')
    await state.clear()
    try:
        await call.message.edit_text(text=t_contacts, inline_message_id=call.inline_message_id,
                                     reply_markup=contacts_markup)
    except Exception as e:
        photo = FSInputFile("source/Машенька.jpg")
        await call.message.edit_media(media=InputMediaPhoto(media=photo, caption=t_contacts, parse_mode='Markdown'),
                                      reply_markup=contacts_markup)


