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
        return np.random.randint(0, len(game.states))

class FictitiousPlay(Player):
    title = "Fictitious Play"

    def play(self, opponent, game):
        play_distribution = np.zeros(len(game.states))
        for play in opponent.play_history: play_distribution[play] += 1

        play_rewards = game.rewards[:, :, 0].dot(play_distribution)
        play_index = np.argmax(play_rewards)
        return play_index

class Leader(Player):
    def __init__(self, name, offer, punishment):
        super().__init__(name)
        self.offer = offer
        self.punishment = punishment
        self.current_punishment = []

    def play(self, opponent, game):
        # If they reject the offer, extend their punishment
        if len(self.play_history) > 0 and opponent.play_history[-1] != self.offer[0]:
            self.current_punishment = self.punishment[:]

        if len(self.current_punishment) > 0:
            return self.current_punishment.pop()
        else:
            result = self.offer[1]
            if type(result) is int:
                return result
            elif type(result) is list:
                return np.random.choice(range(len(result)), p = result)
            else:
                raise Exception("Invalid offer!")

class Godfather(Leader):
    title = "Godfather"

    def __init__(self, name):
        super().__init__(name, [0, 0], [1, 1, 1])

class SoftBully(Leader):
    title = "Soft Bully"

    def __init__(self, name):
        super().__init__(name, [0, [.75, .25]], [1, 1, 1])

class Bully(Leader):
    title = "Bully"
    offer = [0, 1]
    punishment = 1

    def __init__(self, name):
        super().__init__(name, [0, 1], [1, 1, 1])
