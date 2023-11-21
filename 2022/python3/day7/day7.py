"""
Input is output of terminal commands (starting with $).
Example commands:
    cd: change directory
    cd x moves in one level
    cd .. moves back one level
    cd / moves to / directory.
    ls: list files/directories
    123 abc means directory has file abc with size 123
    dir xyz means directory contains directory named xyz


Puzzle 1: Find all directories w/ total size of at most 100000.
    What is the sum of their total sizes?
Puzzle 2: What is the total size of the smallest directory
    that would free up enough space to run the update (30000000).
"""

import sys
from itertools import accumulate


def find_directories_of_size(input_file,
                             total_size=100000,
                             show_smallest=False):
    sizes = dict()
    cwd = []

    with open(input_file, "r") as file:
        for line in file:
            args = line.split()
            if line.strip() == "$ cd ..":
                cwd.pop()
            elif line.startswith("$ cd"):
                cwd.append(args[-1])
            elif args[0].isnumeric():
                for path in accumulate(cwd, func=lambda a, b: a + "/" + b):
                    if path in sizes.keys():
                        sizes[path] += int(args[0])
                    else:
                        sizes.update({path: int(args[0])})

    if show_smallest:
        return min(size for size in sizes.values()
                   if size >= sizes["/"] - total_size)
    else:
        return sum(size for size in sizes.values()
                   if size <= total_size)


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_directories_of_size(input_file))
    print(find_directories_of_size(input_file, 40000000, True))
