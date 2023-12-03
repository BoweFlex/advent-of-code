"""
Engine part is missing, should be easy to find if you add up all part numbers
in the engine schematic. Any number adjacent to a symbol (other than '.')
is a part number.

Part 1: What is the sum of all the part numbers in the schematic?
Part 2: What is the sum of all the gear ratios in the schematic?
    Gear ratio: Product of two numbers that are adjacent to
    the same '*' symbol.
"""

import sys


# assumes object is an iterable
def product_of_iterable(obj):
    result = 1
    for i in obj:
        result = result * i
    return result


def find_part_numbers_and_gear_ratios(input_file):
    gear_sum = 0
    with open(input_file, 'r') as file:
        schematic = []
        for line in file:
            schematic.append(line)
        chars = {(row, col): [] for row in range(len(schematic))
                 for col in range(len(schematic[0]))
                 if not schematic[row][col].isdigit()
                 and schematic[row][col] != '.'
                 and schematic[row][col] != '\n'}
        for line_index, line in enumerate(schematic):
            chunk = {"word": '', "indexes": []}
            line_above = line_index - 1
            line_below = line_index + 1
            for index, char in enumerate(line):
                if char.isdigit():
                    chunk["word"] += char
                    chunk["indexes"].append(index)
                else:
                    if chunk["word"] == '':
                        continue
                    pre_chunk = min(chunk["indexes"]) - 1
                    post_chunk = max(chunk["indexes"]) + 1
                    chunk_border = {(row, col) for row in (line_above, line_index, line_below)
                                    for col in range(pre_chunk, post_chunk+1)}
                    # & is set intersection, finds coordinate pairs that only exist in both
                    # chunk_border (coordinates around the number) and chars.keys
                    # (coordinates of found symbols)
                    for symbol in chunk_border & chars.keys():
                        chars[symbol].append(int(chunk["word"]))
                    chunk = {"word": '', "indexes": []}
        for part in chars.values():
            if len(part) == 2:
                gear_sum += product_of_iterable(part)
    part1 = f'The sum of all part numbers is: {sum(sum(part) for part in chars.values())}'
    part2 = f'The sum of all gear ratios is: {gear_sum}'
    result = f'Part 1 solution: {part1}\nPart 2 solution: {part2}'
    return result


# I had originally written this function as a solution to part 1.
# It works, but I couldn't think of a way to adjust it nicely to
# handle part 2's puzzle. While putting together the solution to
# part 2 (which was based more around the numbers), I found a
# cleaner solution that would solve both parts. This is no longer
# needed but I'm leaving it here as a reminder of different paths I went down.
def sum_part_numbers(input_file):
    sum = 0
    part_numbers = []
    with open(input_file, 'r') as file:
        schematic = []
        for line in file:
            schematic.append(line)
        for index, line in enumerate(schematic):
            chunk = {"word": '', "indexes": []}
            line_above = index - 1
            line_below = index + 1
            for index, char in enumerate(line):
                if char.isdigit():
                    chunk["word"] += char
                    chunk["indexes"].append(index)
                else:
                    if chunk["word"] == '':
                        continue
                    pre_chunk = min(chunk["indexes"]) - 1
                    post_chunk = max(chunk["indexes"]) + 1
                    if pre_chunk >= 0 and (
                            line[pre_chunk] != '.' and
                            not line[pre_chunk].isdigit()):
                        part_numbers.append(int(chunk["word"]))
                        sum += int(chunk["word"])
                    elif post_chunk < len(line) and (
                            line[post_chunk] != '.' and
                            not line[post_chunk].isdigit() and
                            line[post_chunk] != '\n'):
                        part_numbers.append(int(chunk["word"]))
                        sum += int(chunk["word"])
                    else:
                        # 1 is added to post_chunk because end is not included
                        for space in range(pre_chunk, post_chunk+1):
                            if space < 0 or space > len(line):
                                continue
                            if line_above >= 0 and (
                                    schematic[line_above][space] != '.' and
                                    not schematic[line_above][space].isdigit() and
                                    schematic[line_above][space] != '\n'):
                                part_numbers.append(int(chunk["word"]))
                                sum += int(chunk["word"])
                            elif line_below < len(schematic) and (
                                    schematic[line_below][space] != '.' and
                                    not schematic[line_below][space].isdigit() and
                                    schematic[line_below][space] != '\n'):
                                part_numbers.append(int(chunk["word"]))
                                sum += int(chunk["word"])
                    chunk = {"word": '', "indexes": []}
        return f'The sum of all part numbers found is: {sum}'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_part_numbers_and_gear_ratios(input_file))
else:
    print("Please provide a input file!")
