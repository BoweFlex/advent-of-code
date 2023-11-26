"""
The elves are carrying calories via different snacks. These calores are
denoted by items on a line, with a blank line between different
elf's inventories. For example:
-----
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
-----
First: We'd like to take food first from the elf with carrying the most *total*
calories. Figure out who that is by totaling up subsequent calorie amounts.
Solution should: read in input file, loop through lines to total each
group of calories, then return the highest total.
Second: We'd like to know the total calories of the top three elves *combined*.
Find the three highest, then find the sum of those three.

**MUST PROVIDE PATH TO INPUT FILE WHEN EXECUTING
"""

import sys


def sum_elves(elves):
    final_total = 0
    for elf in elves:
        final_total += elf
    return final_total


def highest_total(input_file, num_top_elves=1):
    file = open(input_file, "r")
    total = 0
    top_elves = []
    # print(file.read())
    for line in file:
        if line.strip():
            total += int(line)
        else:
            if len(top_elves) < num_top_elves:
                top_elves.append(total)
            else:
                top_elves.sort()
                for elf in top_elves:
                    if total > elf:
                        top_elves.remove(elf)
                        top_elves.append(total)
                        break
            total = 0
    return sum_elves(top_elves)


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print("Highest elf:", highest_total(input_file))
    print("Highest three elves combined:", highest_total(input_file, 3))
