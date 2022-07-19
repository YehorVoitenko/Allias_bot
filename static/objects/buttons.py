from telebot import types
from static.constants import phrases


def choose_name():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(phrases.own_name),
                       types.InlineKeyboardButton(phrases.random_name))
    return markup_request


def plus_minus():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('+'),
               types.InlineKeyboardButton('-'))
    return markup_request