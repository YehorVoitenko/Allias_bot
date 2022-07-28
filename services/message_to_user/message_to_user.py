import telebot

from object.phrase import phrase
from settings.config import config
from static.variable import variable

bot = telebot.TeleBot(config.TOKEN)


def pick_winner():
    if variable.first_team_points > variable.second_team_points:
        winner = variable.first_team_name
    elif variable.first_team_points < variable.second_team_points:
        winner = variable.second_team_name
    elif variable.first_team_points == variable.second_team_points:
        winner = "Ничья"
    return winner


def show_teams_points(message):
    bot.send_message(message.chat.id, f"<b>{phrase.get_teams_points} {variable.first_team_name}: "
                                      f"{variable.first_team_points}</b>\n"
                                      f"<b>{phrase.get_teams_points} {variable.second_team_name}: "
                                      f"{variable.second_team_points}</b>", parse_mode='html')

