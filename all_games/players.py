import numpy as np
from all_games.utils import get_choice

class Player:
    title = "Unknown"

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.play_history = []

    def play(self, opponent, game): pass

    def __str__(self):
        return "{}: {} (avg: {})".format(self.name, self.score, round(self.score / len(self.play_history), 2) if len(self.play_history) > 0 else 0)

class Human(Player):
    title = "Human"

    def __init__(self, name):
        super().__init__(name)

    def play(self, opponent, game):
        return get_choice("{} is ready. What do you play?".format(opponent.name), game.states, lambda x: x, return_index = True)

class Random(Player):
    title = "Random"

    def play(self, opponent, game):
        return np.random.randint(0, len(game.states) - 1)

class FictitiousPlay(Player):
    title = "Fictitious Play"

    def play(self, opponent, game):
        play_distribution = np.zeros(len(game.states))
        for play in opponent.play_history: play_distribution[play] += 1

        play_rewards = game.rewards[:, :, 0].dot(play_distribution)
        play_index = np.argmax(play_rewards)
        return play_index

class Godfather(Player):
    title = "Godfather"
    offer = [0, 0]
    punishment = 1

    def play(self, opponent, game):
        if len(self.play_history) == 0 or opponent.play_history[-1] == self.offer[0]:
            return self.offer[1]
        else:
            return self.punishment

class SoftBully(Player):
    title = "Soft Bully"
    offer = [0, [.75, .25]]
    punishment = 1

    def play(self, opponent, game):
        if len(self.play_history) == 0 or opponent.play_history[-1] == self.offer[0]:
            return np.random.choice([0, 1], p = self.offer[1])
        else:
            return self.punishment


class Bully(Player):
    title = "Bully"
    offer = [0, 1]
    punishment = 1

    def play(self, opponent, game):
        if len(self.play_history) == 0 or opponent.play_history[-1] == self.offer[0]:
            return self.offer[1]
        else:
            return self.punishment
