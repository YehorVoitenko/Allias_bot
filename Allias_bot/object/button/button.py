from telebot import types

from object.phrase import phrase


def create_name_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(phrase.custom_name),
                       types.InlineKeyboardButton(phrase.random_name))
    return markup_request


def get_ready_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('Готов'))
    return markup_request


def add_point_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('+'),
                       types.InlineKeyboardButton('-'))
    return markup_request
