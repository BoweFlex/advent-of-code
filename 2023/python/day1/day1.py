"""

Being sent into the sky via trebuchet to figure out issue w/ snow.
Calibration document has been amended, and needs to be "decoded".

Part 1: Find calibration value - combination of first and last digit -
    for each line. Should form a single two digit number.
Part 2: Some digits are spelled out as words. Find the new sum of values.
"""

import sys


# This function doesn't work, because one word being replaced will potentially
# keep another word from being replaced. i.e: "oneight", both one and eight
# should be found and replaced, but when one is replaced with 1
# eight is no longer found. Not sure how to fix it, going a different route.
def replace_num_dict(value):
    value = value.lower()
    locations = {}
    locations.update({"one": value.find("one")})
    locations.update({"two": value.find("two")})
    locations.update({"three": value.find("three")})
    locations.update({"four": value.find("four")})
    locations.update({"five": value.find("five")})
    locations.update({"six": value.find("six")})
    locations.update({"seven": value.find("seven")})
    locations.update({"eight": value.find("eight")})
    locations.update({"nine": value.find("nine")})

    sorted_locations = sorted(locations.items(), key=lambda x:x[1])

    for location in sorted_locations:
        if location[1] == -1:
            continue
        match location[0]:
            case "one":
                value = value.replace("one", "1")
            case "two":
                value = value.replace("two", "2")
            case "three":
                value = value.replace("three", "3")
            case "four":
                value = value.replace("four", "4")
            case "five":
                value = value.replace("five", "5")
            case "six":
                value = value.replace("six", "6")
            case "seven":
                value = value.replace("seven", "7")
            case "eight":
                value = value.replace("eight", "8")
            case "nine":
                value = value.replace("nine", "9")
    return value


# This function retains existing words, enabling multiple replacements to work.
def replace_num_words(value):
    value = value.lower()

    value = (
            value.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
    )
    return value


def get_calibration_values(input_file, part=1):
    calibration_sum = 0

    with open(input_file, 'r') as file:
        for line in file:
            calibration = ''
            if part == 2:
                line = replace_num_words(line)
            for char in line:
                if char.isdigit():
                    calibration += char
                    break
            for char in reversed(line):
                if char.isdigit():
                    calibration += char
                    break
            calibration_sum += int(calibration)
    return f'The sum of the calibration values is: {calibration_sum}'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(get_calibration_values(input_file))
    print(get_calibration_values(input_file, 2))
else:
    print("Please provide a input file!")
