"""
Puzzle Input: boat_races
    Boat races are set amt of time, try to go furthest.
    Boat has starting speed of 0mm/ms, each ms you hold button at the
    beginning of the race +1mm/ms.
Lines:
    - Time: Amount of time allowed for each race
    - Distance: Record distance for time
Part 1: Determine the number of ways you could beat the record for each
    race. What do you get if you multiple these numbers (for all races)
    together?
Part 2: Ignore spaces between numbers, it's actually one very long race.
    How many ways can you beat this longer race?
"""

import sys


def find_ways_to_beat_record(input_file, part=1):
    product = 1
    with open(input_file, 'r') as boat_races:
        if part == 2:
            time = ""
            times = boat_races.readline().split(":")[1]
            for num in times.split():
                time += num
            times = [int(time)]

            distance = ""
            distances = boat_races.readline().split(":")[1]
            for num in distances.split():
                distance += num
            distances = [int(distance)]
        else:
            times = list(map(int, boat_races.readline().split(":")[1].split()))
            distances = list(map(int, boat_races.readline().split(":")[1].split()))

        for index, time in enumerate(times):
            min_time = 0
            max_time = 0
            for ms in range(int(time/2)):
                total_dist = ms * (time - ms)
                if (total_dist > distances[index]):
                    min_time = ms
                    break

            for ms in range(time, int(time/2), -1):
                total_dist = ms * (time - ms)
                if (total_dist > distances[index]):
                    max_time = ms
                    break

            number_ways = max_time - min_time + 1
            product *= number_ways
        if part == 2:
            return f'You can beat the longer race in {product} ways!'
        return f'The product of the number of ways to beat each race is {product}!'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_ways_to_beat_record(input_file))
    print(find_ways_to_beat_record(input_file, 2))
else:
    print('Please provide a valid file path!')
