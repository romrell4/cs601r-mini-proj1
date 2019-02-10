import numpy as np

def start():
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

    states = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    state_distribution = np.zeros(len(states))
    scores = [0, 0]

    while True:
        print("\nAI: {}\tYou: {}".format(scores[0], scores[1]))

        ai_guess = np.argmax(state_distribution)
        ai_index = int(np.argmax(rewards[:,ai_guess]))
        ai_play = states[ai_index]

        print("I've decided my play. What do you play?")
        for index, state in enumerate(states):
            print("\t{} - {}".format(index, state))
        your_index = None
        while your_index is None:
            answer = input()
            if 0 <= int(answer) < len(states):
                your_index = int(answer)
            else:
                print("Try again")

        state_distribution[your_index] += 1
        your_play = states[your_index]
        print("I played {}, you played {}".format(ai_play, your_play))
        if verbs[ai_index, your_index] is not None:
            print("{} {} {}. I win!".format(states[ai_index], verbs[ai_index, your_index], states[your_index]))
            scores[0] += 1
        elif verbs[your_index, ai_index] is not None:
            print("{} {} {}. You win!".format(states[your_index], verbs[your_index, ai_index], states[ai_index]))
            scores[1] += 1
        else:
            print("It's a tie!")


if __name__ == '__main__':
    start()
