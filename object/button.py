from telebot import types
from utils.file_utils import get_translation

bot_phrase = get_translation()


def create_name_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(bot_phrase.custom_name),
                       types.InlineKeyboardButton(bot_phrase.random_name))
    return markup_request


def get_ready_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(bot_phrase.ready))
    return markup_request


def add_point_button():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup_request.add(types.InlineKeyboardButton(bot_phrase.plus),
                       types.InlineKeyboardButton(bot_phrase.minus))
    return markup_request
