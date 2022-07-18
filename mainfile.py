import time
import telebot
import random
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")
team_number = 1
first_team_name = None
second_team_name = None
first_team_points = 0
second_team_points = 0
turn = 2
rounds = 0


@bot.message_handler(commands=['start'])
def greeting(message):
    global team_number
    if team_number <= 2:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup_request.add(types.InlineKeyboardButton('Своё название'), types.InlineKeyboardButton('Случайное название'))
        msg = bot.send_message(message.chat.id, f'{team_number}-ая выбери вариант названия', reply_markup=markup_request)
        bot.register_next_step_handler(msg, choose_name_way)
    if team_number == 3:
        are_you_ready(message)


def choose_name_way(message):
    global team_number
    global first_team_name
    global second_team_name
    if message.text == 'Своё название':
        msg = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg, own_team_name)
    elif message.text == 'Случайное название':
        name = random_name()
        bot.send_message(message.chat.id, f"Название {team_number}-ой команды: <b><u>{name}</u></b>\n",
                                          parse_mode='html')
        if team_number == 1:
            first_team_name = name
        if team_number == 2:
            second_team_name = name
        if team_number <= 2:
            team_number += 1
            greeting(message)


def random_name():
    with open('static/nouns.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        nouns = random.choice(splited)

    with open('static/adjectives.txt', 'r') as file:  # Instead of adjectives.txt - use file with adjectives
        content = file.read()
        splited = content.split("\n")
        adjectives = random.choice(splited)
    return f'{adjectives} {nouns} '


def own_team_name(message):
    global first_team_name
    global second_team_name
    global team_number
    bot.send_message(message.chat.id, f"Название {team_number}-ой команды: <b><u>{message.text}</u></b>",
                     parse_mode='html')
    if team_number == 1:
        first_team_name = message.text
    if team_number == 2:
        second_team_name = message.text
    if team_number <= 2:
        team_number += 1
        greeting(message)


def are_you_ready(message):
    global first_team_name
    global second_team_name
    global first_team_points
    global second_team_points
    global turn
    global rounds
    if turn == second_team_name:  # Create class for check
        turn = first_team_name
    else:
        turn = second_team_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start = types.InlineKeyboardButton('Готов')
    markup.add(start)
    if first_team_points != 0 or second_team_points != 0:
        show_points(message)
    if rounds == 2:
        game_over(message)
    else:
        msg = bot.send_message(message.chat.id, f"Команда <b><u>{turn}</u></b> готова?", reply_markup=markup,
                               parse_mode='html')
        bot.register_next_step_handler(msg, timer)
        rounds += 1


def show_word(message):
    with open('static/words.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        word = random.choice(splited)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton(text='+', callback_data='plus'),
               types.InlineKeyboardButton(text='-', callback_data='minus'))
    msg = bot.send_message(message.chat.id, f'<b>{word}</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(msg, plus_or_minus)


def plus_or_minus(message):
    global turn
    global first_team_points
    global second_team_points
    if message.text == '+':
        if turn == second_team_name:
            second_team_points += 1
        else:
            first_team_points += 1
        bot.send_message(message.chat.id, '+1 балл')
        show_word(message)
    elif message.text == '-':
        if turn == second_team_name:
            second_team_points -= 1
        else:
            first_team_points -= 1
        bot.send_message(message.chat.id, '-1 балл')
        show_word(message)


def timer(message):
    show_word(message)
    time.sleep(5)
    bot.send_message(message.chat.id, "<b>Ход переходит следующей команде</b>", parse_mode='html')
    are_you_ready(message)


def show_points(message):
    global first_team_points
    global second_team_points
    global first_team_points
    global second_team_points
    bot.send_message(message.chat.id, f"<b>Баллы команды {first_team_name}: {first_team_points}</b>\n<b>"
                                      f"Баллы команды {second_team_name}: {second_team_points}</b>", parse_mode='html')


def game_over(message):
    global first_team_name
    global second_team_name
    global first_team_points
    global second_team_points
    markup = types.ReplyKeyboardRemove()
    if first_team_points > second_team_points:
        winner = first_team_name
    elif first_team_points < second_team_points:
        winner = second_team_name
    elif first_team_points == second_team_points:
        winner = "Ничья"

    bot.send_message(message.chat.id, f"Игра окончена, спасибо за игру)\n"
                                      f"Победитель: {winner}", reply_markup=markup)


bot.polling(non_stop=True)