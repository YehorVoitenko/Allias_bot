import time
import telebot
from telebot import types
from object import button
from constants import config, variable
from utils.file_utils import get_translation
from calculation.check_value import check_team_turn
from utils.file_utils import get_random_name, give_word_for_round
from services.notificate_user import pick_winner, show_teams_points

bot_phrase = get_translation()
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if variable.team_turn_number <= variable.total_teams_quantity:
        markup_request = button.create_name_button()
        msg = bot.send_message(message.chat.id, f'{variable.team_turn_number}-ая выбери вариант названия',
                               reply_markup=markup_request)
        bot.register_next_step_handler(msg, create_team_name)
    if variable.team_turn_number == variable.total_teams_quantity + 1:
        change_team_turn(message)


def create_team_name(message):
    if message.text == bot_phrase.custom_name:
        msg = bot.send_message(message.chat.id, bot_phrase.write_custom_team_name)
        bot.register_next_step_handler(msg, custom_team_name)
    elif message.text == bot_phrase.random_name:
        name = get_random_name()
        bot.send_message(message.chat.id, f"Название {variable.team_turn_number}-ой команды: "
                                          f"<b><u>{name}</u></b>\n", parse_mode='html')
        give_team_name_by_turn_number(message, name)
    else:
        bot.send_message(message.chat.id, bot_phrase.error102)
        start(message)


def give_team_name_by_turn_number(message, team_name_by_creation_name_type):
    if variable.team_turn_number == variable.total_teams_quantity - 1:
        variable.first_team_name = team_name_by_creation_name_type
    else:
        variable.second_team_name = team_name_by_creation_name_type
    if variable.team_turn_number <= variable.total_teams_quantity:
        variable.team_turn_number += 1
        start(message)


def custom_team_name(message):
    bot.send_message(message.chat.id, f"Название {variable.team_turn_number}-ой команды: "
                                      f"<b><u>{message.text}</u></b>", parse_mode='html')
    give_team_name_by_turn_number(message, message.text)


def change_team_turn(message):
    markup_request = button.get_ready_button()
    if variable.current_round != variable.total_round_number + 1:
        current_team_turn = check_team_turn()
        variable.team_turn_number += 1
        msg = bot.send_message(message.chat.id, f"Команда <b><u>{current_team_turn}</u></b> готова?",
                               reply_markup=markup_request, parse_mode='html')
        bot.register_next_step_handler(msg, get_round_time)
    else:
        finish_game(message)


def get_round_time(message):
    if message.text == bot_phrase.ready:
        show_word(message)
        time.sleep(variable.round_time_value)
        show_teams_points(message)
        bot.send_message(message.chat.id, bot_phrase.pass_next_team_turn, parse_mode='html')
        variable.current_round += 1
        change_team_turn(message)
    else:
        markup_request = button.get_ready_button()
        bot.send_message(message.chat.id, bot_phrase.error103)
        msg = bot.send_message(message.chat.id, bot_phrase.button_ready,
                               reply_markup=markup_request, parse_mode='html')
        bot.register_next_step_handler(msg, get_round_time)


def show_word(message):
    word = give_word_for_round()
    markup_request = button.add_point_button()
    msg = bot.send_message(message.chat.id, f'<b>{word}</b>', reply_markup=markup_request, parse_mode='html')
    bot.register_next_step_handler(msg, add_point)


def add_point(message):
    if message.text == bot_phrase.plus:
        if variable.current_round % 2 == 1:
            variable.first_team_points += 1
        else:
            variable.second_team_points += 1
        show_word(message)
    if message.text == bot_phrase.minus:
        if variable.current_round % 2 == 1:
            variable.first_team_points -= 1
        else:
            variable.second_team_points -= 1
        show_word(message)
    if message.text != bot_phrase.plus and message.text != bot_phrase.minus and message.text != bot_phrase.ready:
        markup_request = button.add_point_button()
        bot.send_message(message.chat.id, bot_phrase.error101, reply_markup=markup_request)
        show_word(message)


def finish_game(message):
    markup_request = types.ReplyKeyboardRemove()
    winner_team = pick_winner()
    bot.send_message(message.chat.id, f"{bot_phrase.get_winner_team_name}: <b><u>{winner_team}</u></b>",
                     parse_mode='html', reply_markup=markup_request)


bot.polling(non_stop=True)
