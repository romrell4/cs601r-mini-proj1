import numpy as np

class Game:
    states = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    rewards = np.array([
        [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 1], [1, 0]],
        [[0, 1], [1, 0], [0, 0], [1, 0], [0, 1]],
        [[0, 1], [1, 0], [0, 1], [0, 0], [1, 0]],
        [[1, 0], [0, 1], [1, 0], [0, 1], [0, 0]]
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
            if sum(reward) == 0:
                print("It's a tie")
            else:
                print("{} wins!".format((self.player1 if reward[0] > 0 else self.player2).name))
            self.player1.score += reward[0]
            self.player2.score += reward[1]

        print("\n{} reached 10 points first! We have a winner!".format(max([self.player1, self.player2], key = lambda p: p.score).name))

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
        play_rewards = Game.rewards[:,:,0].dot(opponent.play_distribution)
        play_index = np.argmax(play_rewards)
        self.play_distribution[play_index] += 1
        return play_index


if __name__ == '__main__':
    def get_player(title):
        print(title)
        player_type = input("Type? (0 - AI; 1 - Human) ")
        player_name = input("Name? ")
        if player_type == "0":
            return AI(player_name)
        else:
            return Human(player_name)

    players = [get_player("Player 1"), get_player("Player 2")]

    Game(players).start()
