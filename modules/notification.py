from telebot import types
from static.constants import variable


def declare_winner():
    if variable.first_team_points > variable.second_team_points:
        winner = f'Победил: <b><u>{variable.second_team_name}</u></b>'
    elif variable.first_team_points < variable.second_team_points:
        winner = f'Победил: <b><u>{variable.second_team_name}</u></b>'
    elif variable.first_team_points == variable.second_team_points:
        winner = "Ничья"
    return winner