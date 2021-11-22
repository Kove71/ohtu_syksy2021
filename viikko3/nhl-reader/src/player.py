class Player:
    def __init__(self, name, nationality, team, assists, goals, penalties, games):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.games = games
        self.score = self.goals + self.assists
        self.format_string()
    
    def format_string(self):
        self.player_string = self.name + (20-len(self.name)) * " "
        self.player_string += self.team + " "
        if self.goals < 10:
            self.player_string += " "
        self.player_string += str(self.goals) + " + "
        if self.assists < 10:
            self.player_string += " "
        self.player_string += str(self.assists)
        self.player_string += " = "
        if self.score < 10:
            self.player_string += " "
        self.player_string += str(self.score)

    def __str__(self):
        return self.player_string
