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
We'd like to take food first from the elf with carrying the most *total*
calories. Figure out who that is by totaling up subsequent calorie amounts.
Solution should: read in input file, loop through lines to total each
group of calories, then return the highest total.

**MUST PROVIDE PATH TO INPUT FILE WHEN EXECUTING
"""

import sys


def highest_total(input_file):
    file = open(input_file, "r")
    total = 0
    highest_total = 0
    # print(file.read())
    for line in file:
        if line.strip():
            # print(line)
            total += int(line)
        else:
            # print("This line is blank!")
            if total > highest_total:
                highest_total = total
            total = 0
    return highest_total


print(highest_total(sys.argv[1]))
