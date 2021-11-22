import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict["nationality"],
                player_dict["team"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["games"]
            )

            players.append(player)

    print("Oliot:")
    players_sorted = sorted(players, key=lambda x: x.score, reverse=True)
    for player in players_sorted:
        print(player)

if __name__ == "__main__":
    main()
