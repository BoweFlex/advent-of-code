"""
First column: A = rock, B = paper, C = Scissors
Second column: X = rock, Y = paper, Z = Scissors
Total score = sum of score for each round
Round score = score for shape (rock=1, paper=2, scissor=3)
    plus outcome (loss=0, draw=3, win=6)
Example:
    A Y -> paper=2 + win=6 = 8
    B X -> rock=1 + loss=0 = 1
    C Z -> scissors=3 + draw=3 = 6
    Total = 15

What is total score according to strategy guide?
Pseudocode:
read in file
for line in file
opponent=first value, player=second value
round_score=value for player pick
determine win/draw/loss for player
add to round_score
add round_score to total_score
"""

import sys


def strat_guide_outcome(input_file):
    file = open(input_file, "r")
    rock = 1
    paper = 2
    scissors = 3
    draw = 3
    win = 6
    loss = 0
    total_score = 0

    for line in file:
        plays = line.split()
        player = plays[1]
        opponent = plays[0]
        match player:
            case "X":
                round_score = rock
            case "Y":
                round_score = paper
            case "Z":
                round_score = scissors
            case _:
                round_score = 0

        if (opponent == "A" and player == "X" or
                opponent == "B" and player == "Y" or
                opponent == "C" and player == "Z"):
            round_score += draw
        elif (opponent == "A" and player == "Y" or
                opponent == "B" and player == "Z" or
                opponent == "C" and player == "X"):
            round_score += win
        else:
            round_score += loss

        total_score += round_score
    return total_score


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(strat_guide_outcome(input_file))
