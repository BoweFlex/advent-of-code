"""
Each rucksack (input line) has two large compartments of equal sizes.
First half of each string is first compartment, second half is the second.
We want to know which item appears in both compartments of each rucksack.
Once we know which item (upper/lowercase letter) is in both compartments,
we can assign that item a priority.
Priorities:
    - lowercase items a-z: 1-26
    - uppercase items A-Z: 27-52

Puzzle 1: What is the sum of the priorities for all rucksacks?
"""

import sys


def rucksack_priorities(input_file):
    file = open(input_file, "r")
    total = 0

    for line in file:
        priority = 0
        first_compartment = line[0:int(len(line)/2)]
        second_compartment = line[int(len(line)/2):-1]

        for first_char in first_compartment:
            if priority > 0:
                break
            for second_char in second_compartment:
                if first_char == second_char:
                    # Adjusting ascii value to find priority
                    if first_char.isupper():
                        adjust = 38
                    else:
                        adjust = 96
                    priority = ord(first_char) - adjust
        total += priority
    return total


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(rucksack_priorities(input_file))
