"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest
to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds;
in each round, the players each simultaneously choose one of Rock, Paper, or Scissors
using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors,
Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape,
the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide
(your puzzle input) that they say will be sure to help you win. "The first column is
what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock,
Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses
must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is
the sum of your scores for each round. The score for a single round is the score for the shape
you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of
the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate
the score you would get if you were to follow the strategy guide.

More details in the puzzle description: https://adventofcode.com/2022/day/2
"""

def first_part(data):
    score_info = {
        "A": {"X": 1+3, "Y": 2+6, "Z": 3+0},
        "B": {"X": 1+0, "Y": 2+3, "Z": 3+6},
        "C": {"X": 1+6, "Y": 2+0, "Z": 3+3}
    }
    score = 0
    for line in data.splitlines():
        opponent, me = line.split()
        score += score_info[opponent][me]
    return score


def second_part(data):
    score_info = {
        "A": {"X": 3+0, "Y": 1+3, "Z": 2+6},
        "B": {"X": 1+0, "Y": 2+3, "Z": 3+6},
        "C": {"X": 2+0, "Y": 3+3, "Z": 1+6}
    }
    score = 0
    for line in data.splitlines():
        opponent, decision = line.split()
        score += score_info[opponent][decision]
    return score

if __name__ == '__main__':
    print("--- Day 2: Rock Paper Scissors ---")
    with open("input/day2.txt", "r") as f: data = f.read()
    score = first_part(data)
    print(f"My total score following first strategy is: {score}")
    score = second_part(data)
    print(f"My total score following second strategy is: {score}")
