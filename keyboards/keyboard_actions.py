from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import pandas as pd

paginator_button = [
    [InlineKeyboardButton(text='➡️', callback_data='next')],
    [InlineKeyboardButton(text='👩🏽‍💻 Запись на консультацию', callback_data='record')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]
paginator_markup = InlineKeyboardMarkup(inline_keyboard=paginator_button)


egrul_button = [
    [InlineKeyboardButton(text='Передать сведения', url='https://t.me/mplatunova')],
    [InlineKeyboardButton(text='👩🏽‍💻 Запись на консультацию', callback_data='record')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]
egrul_markup = InlineKeyboardMarkup(inline_keyboard=paginator_button)


record_button = [
    [InlineKeyboardButton(text='Заказать консультацию', callback_data='record_go')],
    [InlineKeyboardButton(text='Назад', callback_data='cancel')]
]
record_markup = InlineKeyboardMarkup(inline_keyboard=record_button)


sovets_button = [
    [InlineKeyboardButton(text='Следующий "случайный" совет', callback_data="mary_sovets")],
    [InlineKeyboardButton(text='Главное меню', callback_data='cancel')]

]

sovets_markup = InlineKeyboardMarkup(inline_keyboard=sovets_button)