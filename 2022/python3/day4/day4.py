"""
Elves have been assigned ranges of section IDs to clean.
Example line: 2-8,3-7
Puzzle 1: Find count of assignment pairs where ranges fully overlap
Puzzle 2: Find count of pairs that overlap at all.
"""

import sys


def section_overlaps(input_file):
    file = open(input_file, "r")
    count = 0
    count2 = 0

    for line in file:
        sections = line.split(',')
        start1, end1 = sections[0].split('-')
        start2, end2 = sections[1].split('-')
        start1, start2, end1, end2 = (
            int(start1), int(start2), int(end1), int(end2))

        if ((start1 >= start2 and end1 <= end2) or
                (start2 >= start1 and end2 <= end1)):
            count += 1

        if ((start1 >= start2 and start1 <= end2) or
                (start2 >= start1 and start2 <= end1)):
            count2 += 1

    return count, count2


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(section_overlaps(input_file))
