"""
Secret number of cubes in different colors is placed in bag.
These "games" are revealed and recorded one line at a time.

Part 1: Which games would have been possible with only
    12 red cubes, 13 green cubes, and 14 blue cubes?
    What is the sum of their IDs?
Part 2: What is the fewest number of cubes for each color you could have
    used to play each game? For each game, find the "power" of the set,
    aka the number of each color required multiplied by each other.
"""

import sys


def min_possible_cubes(input_file):
    sum = 0
    with open(input_file, 'r') as file:
        for line in file:
            game_power = 0
            colors_required = {"red": 0, "green": 0, "blue": 0}
            rounds = line.split(':')[1]
            for round in rounds.split(';'):
                for color in round.split(','):
                    count, cube = color.split()
                    match cube:
                        case "blue":
                            if int(count) > colors_required["blue"]:
                                colors_required["blue"] = int(count)
                        case "green":
                            if int(count) > colors_required["green"]:
                                colors_required["green"] = int(count)
                        case "red":
                            if int(count) > colors_required["red"]:
                                colors_required["red"] = int(count)
            game_power = colors_required["red"] * colors_required["green"] * colors_required["blue"]
            sum += game_power
        return f"The sum of the power of each game's set is: {sum}"


def sum_possible_games_ids(input_file, red, green, blue):
    sum = 0

    with open(input_file, 'r') as file:
        game_id = 0
        for line in file:
            game_impossible = False
            game_id += 1
            rounds = line.split(':')[1]
            for round in rounds.split(';'):
                for color in round.split(','):
                    count, cube = color.split()
                    match cube:
                        case "blue":
                            if int(count) > blue:
                                game_impossible = True
                                break
                        case "green":
                            if int(count) > green:
                                game_impossible = True
                                break
                        case "red":
                            if int(count) > red:
                                game_impossible = True
                                break
            if not game_impossible:
                sum += game_id
        return f'The sum of all possible game IDs is {sum}.'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(sum_possible_games_ids(input_file, 12, 13, 14))
    print(min_possible_cubes(input_file))
else:
    print("Please provide a input file!")
