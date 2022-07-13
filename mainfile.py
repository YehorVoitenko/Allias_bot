import telebot
import random
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")
global team_number
team_number = 1


@bot.message_handler(commands=['start'])
def greeting(message):
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('Своё название'), types.InlineKeyboardButton('Случайное название'))
    msg = bot.send_message(message.chat.id, "Выбери вариант названия", reply_markup=markup_request)
    bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if message.text == 'Своё название':
        msg1 = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg1, are_you_ready_own)
    elif message.text == 'Случайное название':
        with open('first name.txt', 'r') as file:
            content = file.read()
            splited = content.split(", ")
            random_fir_name = random.choice(splited)
        with open('second name.txt', 'r') as file:
            content = file.read()
            splited = content.split(", ")
            random_sec_name = random.choice(splited)
        bot.send_message(message.chat.id, f"Название 1-ой команды: <b><u>{random_fir_name}  {random_sec_name}</u></b>", parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        msg = bot.send_message(message.chat.id, f" 1-ая команда <b><u>{random_fir_name}  {random_sec_name}</u></b> "
                                                f"готова начать? '\n' Нажми на кнопку, если готов!",
                               reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(msg, show_word)


def are_you_ready_own(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        msg = bot.send_message(message.chat.id, f"1-ая команда <b><u>{message.text}</u></b> "
                                                f"готова начать? '\n'Нажми на кнопку, если готов!", reply_markup=markup,
                               parse_mode='html')
        bot.register_next_step_handler(msg, show_word)


def show_word(message):
    bot.send_message(message.chat.id, 'Game over')

bot.polling(non_stop=True)
