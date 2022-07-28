from static.variable import variable


def check_team_turn():
    if variable.team_turn_number % 2 == 1:
        current_team_turn = variable.first_team_name
    else:
        current_team_turn = variable.second_team_name
    return current_team_turn
