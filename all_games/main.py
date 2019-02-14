from all_games.games import *
from all_games.players import *
from all_games.utils import get_choice

if __name__ == '__main__':
    game = get_choice("Which game would you like to play?", [PrisonersDilemma, RockPaperScissorsLizardSpock, MatchingPennies, Chicken], lambda x: x.name)

    players = [Human, Random, FictitiousPlay, Godfather, SoftBully, Bully]
    me = Human # get_choice("Who would you like to be?", players, lambda x: x.title)
    opponent = get_choice("Who would you like to play against?", players, lambda x: x.title)

    game([opponent("AI"), me("Eric")]).start()
