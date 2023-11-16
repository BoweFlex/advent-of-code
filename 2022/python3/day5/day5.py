"""
Input defines:
    Initial crate layout
    Rearrangement that should happen
Example
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

Crates are moved one at a time, so top crate moves before crate underneath

Puzzle 1: Which crate will end up on top of each stack?

"""

import sys


def setup_stacks(stack_lines):
    stacks = [[] for _ in range(int(stack_lines[-1].split()[-1]))]

    for line in stack_lines[0:-1]:
        i = 0
        for idx, letter in enumerate(line):
            if idx % 4 == 0:
                i += 1
            if letter.isupper():
                stacks[i-1].insert(0, letter)
    return stacks


def predict_top_crate_stack(input_file):
    instructions = []

    with open(input_file, "r") as file:
        stack_start, movements = file.read().split('\n\n')
        stack_lines = stack_start.split('\n')
        stacks = setup_stacks(stack_lines)

        for move in movements.split('\n'):
            instructions.clear()

            for chunk in move.split(' '):
                if chunk.isnumeric():
                    instructions.append(chunk)

            if len(instructions) > 0:
                num_crates_move = int(instructions[0])
                source_stack = int(instructions[1]) - 1
                dest_stack = int(instructions[2]) - 1
                for _ in range(num_crates_move):
                    swap = stacks[source_stack].pop(-1)
                    stacks[dest_stack].append(swap)
        for stack in stacks:
            print(stack[-1])


def predict_top_crate_sublist(input_file):
    instructions = []
    swap = []

    with open(input_file, "r") as file:
        stack_start, movements = file.read().split('\n\n')
        stack_lines = stack_start.split('\n')
        stacks = setup_stacks(stack_lines)

        for move in movements.split('\n'):
            instructions.clear()
            swap.clear()

            for chunk in move.split(' '):
                if chunk.isnumeric():
                    instructions.append(chunk)

            if len(instructions) > 0:
                num_crates_move = int(instructions[0])
                source_stack = int(instructions[1]) - 1
                dest_stack = int(instructions[2]) - 1

                swap = stacks[source_stack][0-num_crates_move:]
                stacks[dest_stack].extend(swap)
                stacks[source_stack] = stacks[source_stack][:0-num_crates_move]

        for stack in stacks:
            print(stack[-1])


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print("Top crates w/ stack:")
    predict_top_crate_stack(input_file)
    print("Top crates w/ sublist:")
    predict_top_crate_sublist(input_file)
