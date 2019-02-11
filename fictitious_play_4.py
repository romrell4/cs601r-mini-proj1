import numpy as np

class Game:
    states = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    rewards = np.array([
        [0, -1, 1, 1, -1],
        [1, 0, -1, -1, 1],
        [-1, 1, 0, 1, -1],
        [-1, 1, -1, 0, 1],
        [1, -1, 1, -1, 0]
    ])
    verbs = np.array([
        [None, "is covered by", "crushes", "crushes", "is vaporized by"],
        ["covers", None, "is cut by", "is eaten by", "disproves"],
        ["is crushed by", "cuts", None, "decapitates", "is smashed by"],
        ["is crushed by", "eats", "is decapitated by", None, "poisons"],
        ["vaporizes", "is disproved by", "smashes", "is poisoned by", None]
    ])

    def __init__(self, players):
        self.player1, self.player2 = players

    def start(self):
        while self.player1.score < 10 and self.player2.score < 10:
            print("\n{} {}".format(self.player1, self.player2))

            p1_index, p2_index = self.player1.play(self.player2), self.player2.play(self.player1)
            p1_state, p2_state = [self.states[index] for index in [p1_index, p2_index]]

            print("{} played {}, {} played {}".format(self.player1.name, p1_state, self.player2.name, p2_state))
            reward = self.rewards[p1_index, p2_index]
            if reward == 0:
                print("It's a tie")
            else:
                print("{} {} {}. {} wins!".format(self.states[p1_index], self.verbs[p1_index, p2_index], self.states[p2_index], (self.player1 if reward > 0 else self.player2).name))
            self.player1.score += reward
            self.player2.score -= reward

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
        play_rewards = Game.rewards.dot(opponent.play_distribution)
        play_index = np.argmax(play_rewards)
        self.play_distribution[play_index] += 1
        return play_index


if __name__ == '__main__':
    players = []

    print("Player 1")
    player_type = input("Type? (0 - AI; 1 - Human) ")
    print("Great! You typed: '{}'".format(player_type))
    player_name = input("Name? ")
    if player_type == "0": players.append(AI(player_name))
    else: players.append(Human(player_name))

    print("Player 2")
    player_type = input("Type? (0 - AI; 1 - Human) ")
    print("Great! You typed: '{}'".format(player_type))
    player_name =  input("Name? ")
    if player_type == "0": players.append(AI(player_name))
    else: players.append(Human(player_name))

    Game(players).start()
