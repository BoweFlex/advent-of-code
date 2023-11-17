"""
Input is a seemingly random sequence of characters.
To decode the signal, must find a start-of-packet marker -
Indicated by four characters that are all different.

Puzzle 1: How many characters need to be processed before the first
start-of-packet marker is detected?
Puzzle 2: What if the start-of-message marker is 14 characters long?
"""

import sys


def find_marker(input_file, marker_length=4):
    occurrences = {}

    with open(input_file, "r") as file:
        count = 0
        signal = file.read().strip()
        for char in range(marker_length, len(signal)-1):
            chunk = signal[char-marker_length:char]
            occurrences.clear()
            count = 0

            for letter in chunk:
                if letter in occurrences:
                    occurrences[letter] += 1
                else:
                    occurrences.update({letter: 1})

            for num in occurrences.values():
                if num == 1:
                    count += 1
            if count == marker_length:
                return char

        # Default case, no starter found
        return -1


def find_marker_set(input_file, marker_length=4):
    result = -1

    with open(input_file, "r") as file:
        signal = file.read().strip()
        for char in range(len(signal)):
            if len(set(signal[char:char+marker_length])) == marker_length:
                result = char + marker_length
                break
        return result


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_marker(input_file))
    print(find_marker_set(input_file))
    print(find_marker(input_file, 14))
    print(find_marker_set(input_file, 14))
