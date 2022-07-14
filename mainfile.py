import asyncio
import time

import telebot
import random
import schedule
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")


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
        with open('first name.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
            content = file.read()
            splited = content.split(", ")
            random_fir_name = random.choice(splited)
        with open('second name.txt', 'r') as file:  # Instead of second name.txt - use file with adjectives
            content = file.read()
            splited = content.split(", ")
            random_sec_name = random.choice(splited)
        bot.send_message(message.chat.id, f"Название 1-ой команды: <b><u>{random_fir_name}  {random_sec_name}</u></b>", parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        msg = bot.send_message(message.chat.id, f" 1-ая команда <b><u>{random_fir_name}  {random_sec_name}</u></b> "  # Create another def for print this phrace func
                                                f"готова начать? '\n' Нажми на кнопку, если готов!",
                               reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(msg, timer)


def are_you_ready(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.InlineKeyboardButton('Готов')
    markup.add(start)
    msg = bot.send_message(message.chat.id, f"Команда готова?", reply_markup=markup, parse_mode='html') # Create another def for print this phrace func
    bot.register_next_step_handler(msg, timer)

def are_you_ready_own(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        msg = bot.send_message(message.chat.id, f"1-ая команда <b><u>{message.text}</u></b> "
                                                f"готова начать? '\n'Нажми на кнопку, если готов!", reply_markup=markup,
                               parse_mode='html')
        bot.register_next_step_handler(msg, timer)  # Create another def for print this phrace func + add intuction "if you guessed - put '+'
        print("запуск готов?")


def show_word(message):
    with open('words.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
            content = file.read()
            splited = content.split(", ")
            word = random.choice(splited)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton('+'), types.InlineKeyboardButton('-'))
    msg = bot.send_message(message.chat.id, f'<b>{word}</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(msg, again)


def again(message):
    if message.text == '+':
        bot.send_message(message.chat.id, '+1 балл')
        show_word(message)
    elif message.text == '-':
        bot.send_message(message.chat.id, '-1 балл')
        show_word(message)


def timer(message):
    show_word(message)
    time.sleep(5)
    bot.send_message(message.chat.id, "Следующая команда")
    are_you_ready(message)


bot.polling(non_stop=True)

