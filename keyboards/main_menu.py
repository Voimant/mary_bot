from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import pandas as pd

from DB.db_func import db_cats_list, db_sub_cats_list

main_menu_button = [
    [InlineKeyboardButton(text='👩🏽‍💻 Запись на консультацию', callback_data='record')],
    [InlineKeyboardButton(text='⚖️ Моя специализация и опыт', callback_data='button_2')],
    [InlineKeyboardButton(text='🎖 Отзывы Доверителей', callback_data='button_3')],
    [InlineKeyboardButton(text='💁🏽‍♀️ Советы от юриста', callback_data='mary_sovets')],
    [InlineKeyboardButton(text='⁉️ Задать открытый вопрос юристу', url='https://t.me/+Ds1Aiq4m0hg2NzFi')],
    [InlineKeyboardButton(text='📲 Контакты', callback_data='contacts')],
    # [InlineKeyboardButton(text='📲 Проверить котрагента', callback_data='go_ddata')]
]

main_markup = InlineKeyboardMarkup(inline_keyboard=main_menu_button)


# specialization_button = [
#     [InlineKeyboardButton(text='Семейное право', callback_data='family'),
#     InlineKeyboardButton(text='Судебные споры', callback_data='dispute')],
#     [InlineKeyboardButton(text='Банкротство', callback_data='bankrupt'),
#     InlineKeyboardButton(text='Интелектуальное право', callback_data='intel')],
#     [InlineKeyboardButton(text='Корпоративное право', callback_data='corp'),
#     InlineKeyboardButton(text='Ликвидация бизнеса', callback_data='licvid')],
#     [InlineKeyboardButton(text='Назад', callback_data='cancel')]

# ]
# spec_markup = InlineKeyboardMarkup(inline_keyboard=specialization_button)


def spec_markup():
    list_cats = db_cats_list()
    builder = InlineKeyboardBuilder()
    for cat in list_cats:
        builder.button(text=cat, callback_data=cat)
    builder.button(text='Назад', callback_data='cancel')
    builder.adjust(1)
    return builder.as_markup()


def sub_cats_markup(cat):
    sub_cats_list = db_sub_cats_list(cat)
    builder = InlineKeyboardBuilder()
    for cat in sub_cats_list:
        builder.button(text=cat, callback_data=cat)
    builder.button(text='Назад', callback_data='cancel')
    builder.adjust(1)
    return builder.as_markup()


def sub_bank_markup(cat):
    sub_cats_list = db_sub_cats_list(cat)
    builder = InlineKeyboardBuilder()
    for cat in sub_cats_list:
        builder.button(text=cat, callback_data=cat)
    builder.button(text='Банкротство физических лиц', url='https://t.me/bankrot_naminimalkah')
    builder.button(text='Назад', callback_data='cancel')
    builder.adjust(1)
    return builder.as_markup()


cancel_button = [[InlineKeyboardButton(text="Главное меню", callback_data='cancel')]]
cancel_markup = InlineKeyboardMarkup(inline_keyboard=cancel_button)

contacts_button = [
    [InlineKeyboardButton(text='🌐 VK', url='https://vk.com/the_lawyer_isa_maniac')],
    [InlineKeyboardButton(text='📷 instagram', url='https://instagram.com/platunova.mara?igshid=OGQ5ZDc2ODk2ZA==')],
    [InlineKeyboardButton(text='ТГ канал Банкротство на минималках', url='https://t.me/bankrot_naminimalkah')],
    [InlineKeyboardButton(text='ТГ канал Мозг для правообладателей', url='https://t.me/+SLUgWFJB8wZWRUn2')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]
contacts_markup = InlineKeyboardMarkup(inline_keyboard=contacts_button)


# def dela_mark(path_exl):
#     builder = InlineKeyboardBuilder()
#     df = pd.read_excel(path_exl)
#     dela = df.to_dict()
#     count = 0
#     for dict_1 in dela:
#         dela['Номер дела'][count]
#         builder.row(InlineKeyboardButton(text=str(key), callback_data=str(key)))
#     builder.row(InlineKeyboardButton(text=str('Назад'), callback_data='cancel'))
#     builder.adjust(1)
#     return builder


# for k,v in dela().items():
#     print(k + " ", v)