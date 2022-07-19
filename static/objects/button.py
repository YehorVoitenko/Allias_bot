from telebot import types
from static.constants import phrase


def create_name_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(phrase.own_name),
                       types.InlineKeyboardButton(phrase.random_name))
    return markup_request


def answer_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('+'),
                       types.InlineKeyboardButton('-'))
    return markup_request