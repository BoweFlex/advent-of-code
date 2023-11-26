"""
Radio's screen is broken. This is driven by a clock circuit,
ticking at constant rate (cycles). CPU has a register X which starts
with value of 1, and supports two instructions:
    addx V: takes two cycles to complete, after those cycles X is
        increased by V (positive or negative)
    noop: takes one cycle, does nothing else.
Signal strength is defined by cycle number multiplied by value of X register.

Part1: What is sum of signal strength during 20th cycle and every 40 following?
    (20, 60, 100, 140, 180, 220)
Part2: X register seems to control horizontal position of a sprite. Sprite is 3
pixels wide and X is middle of those three. CRT is 40 pixels by 6 pixels -
draws top row left to right, then row below, etc. Left most pixel is 0 and
right is 39. Single pixel each cycle.
If sprite is currently positioned so that one of three pixels is being drawn
screen produces lit pixel (#), otherwise screen leaves pixel dark (.).
    What are the 8 capital letters shown on CRT?

"""

import sys


# Loops through input file, finds signal strength at start_cycle
# and every num_cycle following
def solution(input_file, start_cycle, num_cycles):
    screen_height = 6
    screen_width = 40
    signal_strengths = []
    # "Naive method" > screen = [['.']*screen_width]*screen_height
    # This is dumb. This^ looks like it's creating the correct 2d array
    # but accessing screen[0][0] accesses the first of EVERY row.
    # Below method correctly creates separate arrays.
    screen = [['.' for _ in range(screen_width)] for _ in range(screen_height)]

    with open(input_file, "r") as file:
        current_cycle = 0
        registerX = 1
        signal_check = start_cycle
        add_cycles = 2
        noop_cycles = 1
        row = 0
        row_pos = 0

        for line in file:
            if line.startswith("addx"):
                for _ in range(add_cycles):
                    current_cycle += 1
                    if current_cycle == signal_check:
                        signal_strength = registerX * current_cycle
                        signal_strengths.append(signal_strength)
                        signal_check += num_cycles
                    if abs(registerX - row_pos) <= 1:
                        screen[row][row_pos] = '#'
                    if row_pos == 39:
                        row += 1
                        row_pos = 0
                    else:
                        row_pos += 1
                # After add_cycles completed, grab value and add to register
                _, value = line.split()
                registerX += int(value)
            else:
                for _ in range(noop_cycles):
                    current_cycle += 1
                    if current_cycle == signal_check:
                        signal_strength = registerX * current_cycle
                        signal_strengths.append(signal_strength)
                        signal_check += num_cycles
                    if abs(registerX - row_pos) <= 1:
                        screen[row][row_pos] = '#'
                    if row_pos == 39:
                        row += 1
                        row_pos = 0
                    else:
                        row_pos += 1

    print()
    for screen_row in screen:
        print(''.join(map(str, screen_row)))
    print(signal_strengths)

    result_string = f"""The sum of the signal strengths at {start_cycle}
and every following {num_cycles} cycles is {sum(signal_strengths)}"""
    return result_string


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(solution(input_file, 20, 40))
