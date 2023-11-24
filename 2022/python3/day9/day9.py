"""
Head is being moved, we need to know where the tail is going.

Part 1: How many positions does the tail visit at least once?
"""

import sys


def solution(input_file, num_knots):
    visited = set()

    with open(input_file, "r") as file:
        directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
        knots = [[0, 0] for _ in range(num_knots)]

        for line in file:
            direction, distance = line.split()
            # repeat direction move as many times as specified
            for _ in range(int(distance)):
                # adjust x coordinate of head by specified direction
                knots[0][0] += directions[direction][0]
                # adjust y coordinate of head by specified direction
                knots[0][1] += directions[direction][1]

                # adjust position of each of the following knots
                for knot in range(1, num_knots):
                    # calculate how far current knot is from the previous knot
                    move_x = knots[knot][0] - knots[knot - 1][0]
                    move_y = knots[knot][1] - knots[knot - 1][1]

                    if move_x >= 2 or move_x <= -2 or move_y >= 2 or move_y <= -2:
                        # make sure neither direction offset is greater than 1
                        move_x = max(-1, min(1, move_x))
                        move_y = max(-1, min(1, move_y))

                        # move the knot
                        knots[knot][0] -= move_x
                        knots[knot][1] -= move_y
                # Add the location of the tail if it's unique
                visited.add((knots[-1][0], knots[-1][1]))
    return f'The tail of the rope visited {len(visited)} unique positions!'

try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(solution(input_file, 2))
    print(solution(input_file, 10))
