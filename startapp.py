from settings import config
import time
import telebot
from telebot import types
from modules.calculations import assign_teams_names, add_point
from static.constants import variable, phrase
from modules.file_util import create_random_name, print_word
from static.objects import button
from modules.notification import declare_winner

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if variable.team_number <= 2:
        markup_request = button.create_name_button()
        msg = bot.send_message(message.chat.id, f'{variable.team_number}-ая выбери вариант названия',
                               reply_markup=markup_request)
        bot.register_next_step_handler(msg, create_team_name)
    if variable.team_number == 3:
        change_turn(message)


def create_team_name(message):
    if message.text == 'Своё название':
        msg = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg, custom_team_name)
    elif message.text == 'Случайное название':
        name = create_random_name()
        bot.send_message(message.chat.id, f"{phrase.x_team_name}: "
                                          f"<b><u>{create_random_name()}</u></b>\n", parse_mode='html')
        assign_teams_names(name)
        start(message)


def custom_team_name(message):
    bot.send_message(message.chat.id, f"{phrase.x_team_name}: <b><u>{message.text}</u></b>",
                     parse_mode='html')
    assign_teams_names(message.text)
    start(message)


def change_turn(message):
    if variable.turn == variable.second_team_name:
        variable.turn = variable.first_team_name
    else:
        variable.turn = variable.second_team_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ready = types.InlineKeyboardButton('Готов')
    markup.add(ready)
    if variable.first_team_points != 0 or variable.second_team_points != 0:
        show_points(message)
    if variable.rounds == 2:
        finish_game(message)
    else:
        msg = bot.send_message(message.chat.id, f"Команда <b><u>{variable.turn}</u></b> готова?", reply_markup=markup,
                               parse_mode='html')
        bot.register_next_step_handler(msg, turn_time)
        variable.rounds += 1


def show_word(message):
    markup_request = button.answer_button()
    msg = bot.send_message(message.chat.id, f'<b>{print_word()}</b>', reply_markup=markup_request, parse_mode='html')
    bot.register_next_step_handler(msg, check_respond)


def check_respond(message):
    add_point(message.text)
    show_word(message)


def turn_time(message):
    show_word(message)
    time.sleep(5)
    bot.send_message(message.chat.id, f"<b>{phrase.next_turn}</b>", parse_mode='html')
    change_turn(message)


def show_points(message):
    bot.send_message(message.chat.id, f"<b>{phrase.team_points} {variable.first_team_name}: "
                                      f"{variable.first_team_points}</b>\n<b>"
                                      f"{phrase.team_points} {variable.second_team_name}: "
                                      f"{variable.second_team_points}</b>",
                     parse_mode='html')


def finish_game(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f"{phrase.thanks}\n"
                                      f"{declare_winner()}", reply_markup=markup, parse_mode='html')


bot.polling(non_stop=True)