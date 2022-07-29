import telebot
from constants import config, variable
from repositories.base import engine, Base
from repositories.retreives import get_first_team, get_second_team
from utils.db_utils.teams import FirstTeam, SecondTeam
from utils.file_utils import get_translation

bot_phrase = get_translation()

bot = telebot.TeleBot(config.TOKEN)

Base.metadata.create_all(engine)

first_team = FirstTeam()
second_team = SecondTeam()


def pick_winner():
    if variable.first_team_points > variable.second_team_points:
        winner = get_first_team().pop().name
    elif variable.first_team_points < variable.second_team_points:
        winner = get_second_team().pop().name
    elif variable.first_team_points == variable.second_team_points:
        winner = "Ничья"
    return winner


def show_teams_points(message):
    bot.send_message(message.chat.id, f"<b>{bot_phrase.get_teams_points_message} {get_first_team().pop().name}: "
                                      f"{variable.first_team_points}</b>\n"
                                      f"<b>{bot_phrase.get_teams_points_message} {get_second_team().pop().name}: "
                                      f"{variable.second_team_points}</b>", parse_mode='html')

