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

First half: What is total score according to strategy guide?
Second half: Second column is what result should be:
    X=lose, Y=draw, Z=win.
"""

import sys


def rps_round_outcome(input_file):
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
        opponent = plays[0]
        outcome = plays[1]

        match outcome:
            case "X":
                round_score = loss
                match opponent:  # Make sure you lose
                    case "A":
                        round_score += scissors
                    case "B":
                        round_score += rock
                    case _:
                        round_score += paper
            case "Y":
                round_score = draw
                match opponent:  # Make sure you draw
                    case "A":
                        round_score += rock
                    case "B":
                        round_score += paper
                    case _:
                        round_score += scissors
            case "Z":
                round_score = win
                match opponent:  # Make sure you win
                    case "A":
                        round_score += paper
                    case "B":
                        round_score += scissors
                    case _:
                        round_score += rock
            case _:
                round_score = 0
        total_score += round_score
    return total_score


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(rps_round_outcome(input_file))
    print(strat_guide_outcome(input_file))
