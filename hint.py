from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton('Backend', callback_data='Backend'),
    InlineKeyboardButton('Frontend', callback_data='Frontend'),
    InlineKeyboardButton('Ux/Ui', callback_data='ux/ui'),
    InlineKeyboardButton('Android-разработка', callback_data='Android'),
    InlineKeyboardButton('IOS-разработка', callback_data='ios'),
]
button = InlineKeyboardMarkup().add(*buttons)