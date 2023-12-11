"""
Puzzle Input: Maps
    One document seems to contain left/right instructions, other describes
    some kind of network of labeled nodes. Seems like you're supposed to
    use left/right instructions to navigate the network.
    Start = AAA, Goal = ZZZ
    If LR instructions don't get you there in time, they repeat.
    RL really means RLRLRLRLRLRLRLRLRL....
Part 1: How many steps are required to reach ZZZ?
Part 2: Multiple starting nodes, anything ending with A. Follow instructions
    until ALL current nodes end with Z. How many steps does it take for all
    current nodes to end with Z?
"""

import sys
from math import lcm


# I originally tried writing this by looping until all locations were at an XXZ
# node simultaneously. This worked on small sets but ran forever on long sets.
# This rewrite finds the number of steps for each starting location, then finds
# the least common multiple of those counts.
def find_steps_count_ghost(input_file):
    nodes = {}
    step_count = 0
    step_counts = []
    max_steps = 1
    current_locations = []
    with open(input_file, 'r') as file:
        instructions, map = file.readline(), file.readlines()
        for line in map:
            if line != '\n':
                source, dirs = line.split('=')
                source = source.strip()
                left, right = dirs.replace('(', '').replace(')', '').split(',')
                options = [left.strip(), right.strip()]
                node = {source.strip(): options}
                nodes.update(node)
                if source[-1] == 'A':
                    current_locations.append(source)

        instr_index = 0
        while len(step_counts) < len(current_locations):
            for index, current_location in enumerate(current_locations):
                if current_location[-1] == 'Z':
                    step_counts.append(step_count)
                if instructions[instr_index].upper() == 'L':
                    current_locations[index] = nodes[current_location][0]
                else:
                    current_locations[index] = nodes[current_location][1]
            if instr_index < len(instructions) - 2:
                instr_index += 1
            else:
                instr_index = 0
            step_count += 1

        for count in step_counts:
            max_steps = lcm(count, max_steps)
        return f'The number of steps from all XXA nodes to XXZ nodes is {max_steps}'


def find_steps_count_single(input_file):
    nodes = {}
    step_count = 0
    with open(input_file, 'r') as file:
        instructions, map = file.readline(), file.readlines()
        for line in map:
            if line != '\n':
                source, dirs = line.split('=')
                left, right = dirs.replace('(', '').replace(')', '').split(',')
                options = [left.strip(), right.strip()]
                node = {source.strip(): options}
                nodes.update(node)

        current_location = 'AAA'
        instr_index = 0
        while current_location != 'ZZZ':
            if instructions[instr_index].upper() == 'L':
                current_location = nodes[current_location][0]
            else:
                current_location = nodes[current_location][1]
            if instr_index < len(instructions) - 2:
                instr_index += 1
            else:
                instr_index = 0
            step_count += 1
        return f'The number of steps from AAA to ZZZ is {step_count}'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_steps_count_single(input_file))
    print(find_steps_count_ghost(input_file))
else:
    print('Please provide a valid file path!')
