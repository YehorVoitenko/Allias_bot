from settings import config
import time
import telebot
from telebot import types
from modules.counter import compare, check
from static.constants import variables, phrases
from modules.work_with_files import output_random_name, print_word
from static.objects import buttons
from modules.notifications import who_win

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if variables.team_number <= 2:
        markup_request = buttons.choose_name()
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
        bot.send_message(message.chat.id, f"{phrases.x_team_name}: "
                                          f"<b><u>{output_random_name()}</u></b>\n", parse_mode='html')
        compare(name)
        start(message)


def own_team_name(message):
    bot.send_message(message.chat.id, f"{phrases.x_team_name}: <b><u>{message.text}</u></b>",
                     parse_mode='html')
    compare(message.text)
    start(message)


def are_you_ready(message):
    if variables.turn == variables.second_team_name:
        variables.turn = variables.first_team_name
    else:
        variables.turn = variables.second_team_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ready = types.InlineKeyboardButton('Готов')
    markup.add(ready)
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
    markup_request = buttons.plus_minus()
    msg = bot.send_message(message.chat.id, f'<b>{print_word()}</b>', reply_markup=markup_request, parse_mode='html')
    bot.register_next_step_handler(msg, plus_minus_check)


def plus_minus_check(message):
    check(message.text)
    show_word(message)


def timer(message):
    show_word(message)
    time.sleep(5)
    bot.send_message(message.chat.id, f"<b>{phrases.next_turn}</b>", parse_mode='html')
    are_you_ready(message)


def show_points(message):
    bot.send_message(message.chat.id, f"<b>{phrases.team_points} {variables.first_team_name}: "
                                      f"{variables.first_team_points}</b>\n<b>"
                                      f"{phrases.team_points} {variables.second_team_name}: "
                                      f"{variables.second_team_points}</b>",
                     parse_mode='html')


def game_over(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f"{phrases.thanks}\n"
                                      f"{who_win()}", reply_markup=markup, parse_mode='html')


bot.polling(non_stop=True)