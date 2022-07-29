from constants import variable
from repositories.retreives import get_first_team, get_second_team


def check_team_turn():
    if variable.team_turn_number % 2 == 1:
        team = get_first_team()
        current_team_turn = team.pop()
    else:
        team = get_second_team()
        current_team_turn = team.pop()
    return current_team_turn.name


