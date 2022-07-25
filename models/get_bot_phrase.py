class Translation:
    def __init__(self, custom_name,
                 random_name, write_custom_team_name, get_winner_team_name,
                 pass_next_team_turn, get_teams_points_message, ready, plus, minus,
                 error101, error102, error103,button_ready):
        self.random_name = random_name
        self.custom_name = custom_name
        self.write_custom_team_name = write_custom_team_name
        self.get_winner_team_name = get_winner_team_name
        self.pass_next_team_turn = pass_next_team_turn
        self.get_teams_points_message = get_teams_points_message
        self.ready = ready
        self.button_ready = button_ready
        self.plus = plus
        self.minus = minus
        self.error101 = error101
        self.error102 = error102
        self.error103 = error103
