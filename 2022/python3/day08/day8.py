"""
Looking for a spot to keep a tree house hidden. A tree is visible if
*all* trees between it and an edge of the grid are shorter than it.
Only look at trees in cardinal directions, not diagonally.
All trees on edge of grid are visible.

Part 1: How many trees are visible from outside?
Part 2: Scenic score = multiply together viewing distance in each
    cardinal direction. Viewing distance stops when reaching edge of
    forest or a tree that is same height or taller.
    What is the highest scenic score found in input?

"""

import sys


def generate_matrix(input_file):
    matrix = []
    index = 0
    with open(input_file, 'r') as file:
        for line in file:
            row = line.strip()
            matrix.append([])
            for char in row:
                matrix[index].append(char)
            index += 1
    return matrix


def trees_visible_outside_grid(input_file):
    tree_grid = generate_matrix(input_file)
    visible_count = 0
    max_scenic_score = 0

    for row_index, row in enumerate(tree_grid):
        for tree_index, tree in enumerate(row):
            visible_from_left = visible_from_right = True
            visible_from_bot = visible_from_top = True
            left_score = right_score = bot_score = top_score = 0
            total_scenic_score = 0
            for i in reversed(range(tree_index)):  # Iterate left
                left_score += 1
                if int(row[i]) >= int(tree):
                    visible_from_left = False
                    break
            for i in range(tree_index+1, len(row)):  # Iterate right
                right_score += 1
                if int(row[i]) >= int(tree):
                    visible_from_right = False
                    break
            for i in reversed(range(row_index)):  # Iterate up
                top_score += 1
                if int(tree_grid[i][tree_index]) >= int(tree):
                    visible_from_top = False
                    break
            for i in range(row_index+1, len(tree_grid)):  # Iterate down
                bot_score += 1
                if int(tree_grid[i][tree_index]) >= int(tree):
                    visible_from_bot = False
                    break

            if (visible_from_left or
                    visible_from_right or
                    visible_from_top or
                    visible_from_bot):
                visible_count += 1

            total_scenic_score = (left_score *
                                  right_score *
                                  top_score *
                                  bot_score)
            if total_scenic_score > max_scenic_score:
                max_scenic_score = total_scenic_score

    return f'Trees visible: {visible_count}, Highest scenic score: {max_scenic_score}'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(trees_visible_outside_grid(input_file))
