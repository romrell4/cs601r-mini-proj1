import numpy as np

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.play_distribution = None

    def play(self, opponent, game): pass

    def __str__(self):
        return "{}: {}".format(self.name, self.score)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self, opponent, game):
        print("{} is ready. What do you play?".format(opponent.name))
        for index, state in enumerate(game.states):
            print("\t{} - {}".format(index, state))
        play_index = None
        while play_index is None:
            answer = input()
            if answer.isdigit() and 0 <= int(answer) < len(game.states):
                play_index = int(answer)
            else:
                print("Try again")

        self.play_distribution[play_index] += 1
        return play_index

class AI(Player):
    def play(self, opponent, game):
        play_rewards = game.rewards[:, :, 0].dot(opponent.play_distribution)
        play_index = np.argmax(play_rewards)
        self.play_distribution[play_index] += 1
        return play_index