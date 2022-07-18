from Allias_bot.settings import config
import time
import random
import telebot
from telebot import types
# from modules.counter import compare
from Allias_bot.static.constants import variables, phrases
from modules.work_with_files import output_random_name, show_word

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def greeting(message):
    if variables.team_number <= 2:
        markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup_request.add(types.InlineKeyboardButton(phrases.own_name),
                           types.InlineKeyboardButton(phrases.random_name))
        msg = bot.send_message(message.chat.id, f'{variables.team_number}-ая выбери вариант названия',
                               reply_markup=markup_request)
        bot.register_next_step_handler(msg, choose_name_way)
    if variables.team_number == 3:
        are_you_ready(message)


def choose_name_way(message):

    if message.text == 'Своё название':
        msg = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg, own_team_name)
    elif message.text == 'Случайное название':
        name = output_random_name()
        bot.send_message(message.chat.id, f"Название {variables.team_number}-ой команды: "
                                          f"<b><u>{output_random_name()}</u></b>\n",
                                          parse_mode='html')
        if variables.team_number == 1:
            variables.first_team_name = name
        if variables.team_number == 2:
            variables.second_team_name = name
        if variables.team_number <= 2:
            variables.team_number += 1
            greeting(message)


def own_team_name(message):
    bot.send_message(message.chat.id, f"Название {variables.team_number}-ой команды: <b><u>{message.text}</u></b>",
                     parse_mode='html')
    if variables.team_number == 1:
        variables.first_team_name = message.text
    if variables.team_number == 2:
        variables.second_team_name = message.text
    if variables.team_number <= 2:
        variables.team_number += 1
        greeting(message)


def are_you_ready(message):
    if variables.turn == variables.second_team_name:  # Create class for check
        variables.turn = variables.first_team_name
    else:
        variables.turn = variables.second_team_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start = types.InlineKeyboardButton('Готов')
    markup.add(start)
    if variables.first_team_points != 0 or variables.second_team_points != 0:
        show_points(message)
    if variables.rounds == 2:
        game_over(message)
    else:
        msg = bot.send_message(message.chat.id, f"Команда <b><u>{variables.turn}</u></b> готова?", reply_markup=markup,
                               parse_mode='html')
        bot.register_next_step_handler(msg, timer)
        variables.rounds += 1


def show_word(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.InlineKeyboardButton('+'),
               types.InlineKeyboardButton('-'))
    with open('static/words.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        word = random.choice(splited)
    msg = bot.send_message(message.chat.id, f'<b>{word}</b>', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(msg, plus_or_minus)


def plus_or_minus(message):
    if message.text == '+':
        if variables.turn == variables.second_team_name:
            variables.second_team_points += 1
        else:
            variables.first_team_points += 1
        bot.send_message(message.chat.id, '+1 балл')
        show_word(message)
    elif message.text == '-':
        if variables.turn == variables.second_team_name:
            variables.second_team_points -= 1
        else:
            variables.first_team_points -= 1
        bot.send_message(message.chat.id, '-1 балл')
        show_word(message)


def timer(message):
    show_word(message)
    time.sleep(5)
    bot.send_message(message.chat.id, "<b>Ход переходит следующей команде</b>", parse_mode='html')
    are_you_ready(message)


def show_points(message):
    bot.send_message(message.chat.id, f"<b>Баллы команды {variables.first_team_name}: {variables.first_team_points}</b>\n<b>"
                                      f"Баллы команды {variables.second_team_name}: {variables.second_team_points}</b>",
                     parse_mode='html')


def game_over(message):
    markup = types.ReplyKeyboardRemove()
    if variables.first_team_points > variables.second_team_points:
        winner = variables.first_team_name
    elif variables.first_team_points < variables.second_team_points:
        winner = variables.second_team_name
    elif variables.first_team_points == variables.second_team_points:
        winner = "Ничья"

    bot.send_message(message.chat.id, f"Игра окончена, спасибо за игру)\n"
                                      f"Победитель: {winner}", reply_markup=markup)


bot.polling(non_stop=True)