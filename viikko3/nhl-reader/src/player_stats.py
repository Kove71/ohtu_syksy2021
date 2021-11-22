class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        print(nationality)
        players_by_nationality = []
        for player in self.players:
            if player.nationality == nationality:
                players_by_nationality.append(player)
        
        players_sorted = sorted(players_by_nationality, key=lambda x: x.score, reverse=True)

        return players_sorted