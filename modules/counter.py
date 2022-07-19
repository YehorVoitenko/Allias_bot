from static.constants import variables


def compare(item):
    if variables.team_number == 1:
        variables.first_team_name = item
    if variables.team_number == 2:
        variables.second_team_name = item
    if variables.team_number <= 2:
        variables.team_number += 1
        return item


def check(text):
    if text == '+':
        if variables.turn == variables.second_team_name:
            variables.second_team_points += 1
        else:
            variables.first_team_points += 1
    if text == '-':
        if variables.turn == variables.second_team_name:
            variables.second_team_points -= 1
        else:
            variables.first_team_points -= 1
