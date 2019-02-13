from all_games.games import *
from all_games.players import AI, Human, Player

if __name__ == '__main__':
    def get_player(title):
        print(title)
        player_type = input("Type? (0 - AI; 1 - Human) ")
        player_name = input("Name? ")
        if player_type == "0":
            return AI(player_name)
        else:
            return Human(player_name)

    print("Which game would you like to play?")
    games = [PrisonersDilemma, RockPaperScissorsLizardSpock, MatchingPennies]
    for index, game in enumerate(games):
        print("\t{} - {}".format(index, game.name))

    game = games[int(input())]

    game([get_player("Player 1"), get_player("Player 2")]).start()
