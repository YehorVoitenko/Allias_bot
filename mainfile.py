import asyncio
import time
import telebot
import random
import schedule
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")
team_number = 1
first_team_name = 'team name'
second_team_name = 'team name'


"""@bot.message_handler(commands=['teaminfo'])
def give_name(message):
    global first_team_name
    global second_team_name
    bot.send_message(message.chat.id, f'<b>First team name: {first_team_name}</b>\n'
                                      f'<b>Second team name: {second_team_name}</b>', parse_mode='html')"""


@bot.message_handler(commands=['start'])
def greeting(message):
    global team_number
    if team_number <= 2:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_request.add(types.InlineKeyboardButton('Своё название'), types.InlineKeyboardButton('Случайное название'))
        msg = bot.send_message(message.chat.id, f'{team_number}-ая выбери вариант названия', reply_markup=markup_request)
        bot.register_next_step_handler(msg, choose_name_way)
    if team_number == 3:
        are_you_ready(message)


def choose_name_way(message):
    global team_number
    if message.text == 'Своё название':
        msg = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg, own_team_name)
    elif message.text == 'Случайное название':
        name = random_name()
        bot.send_message(message.chat.id, f"Название {team_number}-ой команды: <b><u>{name}</u></b>\n",
                               parse_mode='html')
        if team_number <= 2:
            team_number += 1
            greeting(message)


def random_name():
    with open('first name.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split(", ")
        first_random = random.choice(splited)

    with open('second name.txt', 'r') as file:  # Instead of second name.txt - use file with adjectives
        content = file.read()
        splited = content.split(", ")
        second_random = random.choice(splited)
    return f'{first_random} {second_random}'


def own_team_name(message):
    global team_number
    bot.send_message(message.chat.id, f"Название {team_number}-ой команды: <b><u>{message.text}</u></b>",
                     parse_mode='html')
    if team_number <= 2:
        team_number += 1
        greeting(message)


turn = 2


def are_you_ready(message):
    global turn
    if turn == 2:
        turn = 1
    else:
        turn = 2
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.InlineKeyboardButton('Готов')
    markup.add(start)
    msg = bot.send_message(message.chat.id, f"Команда {turn} готова?", reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(msg, timer)


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
    bot.send_message(message.chat.id, "<b>Ход переходит следующей команде</b>", parse_mode='html')
    are_you_ready(message)


bot.polling(non_stop=True)

