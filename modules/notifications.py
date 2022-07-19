import telebot
from telebot import types
from static.constants import variables


def who_win():
    markup = types.ReplyKeyboardRemove()
    if variables.first_team_points > variables.second_team_points:
        winner = f'Победил: <b><u>{variables.second_team_name}</u></b>'
    elif variables.first_team_points < variables.second_team_points:
        winner = f'Победил: <b><u>{variables.second_team_name}</u></b>'
    elif variables.first_team_points == variables.second_team_points:
        winner = "Ничья"
    return winner