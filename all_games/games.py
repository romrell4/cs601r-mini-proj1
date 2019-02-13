import numpy as np

class Game:
    name = "Un-named game"
    states = []
    rewards = np.array(0)
    winning_score = 10

    def __init__(self, players):
        for player in players:
            player.play_distribution = np.zeros(len(self.states))
        self.player1, self.player2 = players

    def start(self):
        print("Welcome to {}. The game is simple. Try to maximize your rewards and reach {} points. Here is the reward matrix:".format(self.name, self.winning_score))
        matrix = [["", *self.states]]
        [matrix.append([state, *row]) for state, row in zip(self.states, self.rewards)]
        for row in matrix: print("".join([str(cell).rjust(10) for cell in row]))

        while self.player1.score < self.winning_score and self.player2.score < self.winning_score:
            print("\n{} {}".format(self.player1, self.player2))

            p1_index, p2_index = self.player1.play(self.player2, self), self.player2.play(self.player1, self)
            p1_state, p2_state = [self.states[index] for index in [p1_index, p2_index]]

            print("{} played {}, {} played {}".format(self.player1.name, p1_state, self.player2.name, p2_state))
            reward = self.rewards[p1_index, p2_index]
            self.player1.score += reward[0]
            self.player2.score += reward[1]

        print("\n{} reached 10 points first! We have a winner!".format(max([self.player1, self.player2], key = lambda p: p.score).name))

class PrisonersDilemma(Game):
    name = "Prisoner's Dilemma"
    states = ["Cooperate", "Defect"]
    rewards = np.array([
        [[3, 3], [1, 4]],
        [[4, 1], [1, 1]]
    ])
    winning_score = 10

class RockPaperScissorsLizardSpock(Game):
    name = "Rock, Paper, Scissors, Lizard, Spock"
    states = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    rewards = np.array([
        [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 1], [1, 0]],
        [[0, 1], [1, 0], [0, 0], [1, 0], [0, 1]],
        [[0, 1], [1, 0], [0, 1], [0, 0], [1, 0]],
        [[1, 0], [0, 1], [1, 0], [0, 1], [0, 0]]
    ])
    winning_score = 10

class MatchingPennies(Game):
    name = "Matching Pennies"
    states = ["Heads", "Tails"]
    rewards = np.array([
        [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 1], [1, 0]],
        [[0, 1], [1, 0], [0, 0], [1, 0], [0, 1]],
        [[0, 1], [1, 0], [0, 1], [0, 0], [1, 0]],
        [[1, 0], [0, 1], [1, 0], [0, 1], [0, 0]]
    ])
    winning_score = 10
