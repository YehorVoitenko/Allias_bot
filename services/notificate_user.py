import telebot
from constants import config, variable
from utils.file_utils import get_translation

bot_phrase = get_translation()

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
    bot.send_message(message.chat.id, f"<b>{bot_phrase.get_teams_points_message} {variable.first_team_name}: "
                                      f"{variable.first_team_points}</b>\n"
                                      f"<b>{bot_phrase.get_teams_points_message} {variable.second_team_name}: "
                                      f"{variable.second_team_points}</b>", parse_mode='html')

