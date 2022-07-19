from static.constants import variable


def assign_teams_names(item):
    if variable.team_number == 1:
        variable.first_team_name = item
    if variable.team_number == 2:
        variable.second_team_name = item
    if variable.team_number <= 2:
        variable.team_number += 1
        return item


def add_point(text):
    if text == '+':
        if variable.turn == variable.second_team_name:
            variable.second_team_points += 1
        else:
            variable.first_team_points += 1
    if text == '-':
        if variable.turn == variable.second_team_name:
            variable.second_team_points -= 1
        else:
            variable.first_team_points -= 1
