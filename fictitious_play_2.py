import numpy as np

class Game:
    states = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    rewards = np.array([
        [0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0]
    ])
    verbs = np.array([
        [None, None, "crushes", "crushes", None],
        ["covers", None, None, None, "disproves"],
        [None, "cuts", None, "decapitates", None],
        [None, "eats", None, None, "poisons"],
        ["vaporizes", None, "smashes", None, None]
    ])

    def __init__(self, players):
        self.player1, self.player2 = players

    def start(self):
        while self.player1.score < 10 and self.player2.score < 10:
            print("\n{} {}".format(self.player1, self.player2))

            p1_index, p2_index = self.player1.play(self.player2), self.player2.play(self.player1)
            p1_state, p2_state = [self.states[index] for index in [p1_index, p2_index]]

            print("{} played {}, {} played {}".format(self.player1.name, p1_state, self.player2.name, p2_state))
            if self.rewards[p1_index, p2_index] > 0:
                print("{} {} {}. {} wins!".format(self.states[p1_index], self.verbs[p1_index, p2_index], self.states[p2_index], self.player1.name))
                self.player1.score += self.rewards[p1_index, p2_index]
            elif self.rewards[p2_index, p1_index] > 0:
                print("{} {} {}. {} wins!".format(self.states[p2_index], self.verbs[p2_index, p1_index], self.states[p1_index], self.player2.name))
                self.player2.score += self.rewards[p2_index, p1_index]
            else:
                print("It's a tie!")

        print("{} wins!".format(max([self.player1, self.player2], key = lambda p: p.score).name))

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.play_distribution = np.zeros(len(Game.states))

    def play(self, opponent): pass

    def __str__(self):
        return "{}: {}".format(self.name, self.score)

class Human(Player):
    def play(self, opponent):
        print("{} is ready. What do you play?".format(opponent.name))
        for index, state in enumerate(Game.states):
            print("\t{} - {}".format(index, state))
        play_index = None
        while play_index is None:
            answer = input()
            if 0 <= int(answer) < len(Game.states):
                play_index = int(answer)
            else:
                print("Try again")

        self.play_distribution[play_index] += 1
        return play_index

class AI(Player):
    def play(self, opponent):
        guess = np.argmax(opponent.play_distribution)
        play_index = int(np.argmax(Game.rewards[:, guess]))
        self.play_distribution[play_index] += 1
        return play_index


if __name__ == '__main__':
    players = []

    print("Player 1")
    type = input("Type? (0 - AI; 1 - Human) ")
    name = input("Name? ")
    if type == "0": players.append(AI(name))
    else: players.append(Human(name))

    print("Player 1")
    type = input("Type? (0 - AI; 1 - Human) ")
    name = input("Name? ")
    if type == "0": players.append(AI(name))
    else: players.append(Human(name))

    Game(players).start()
