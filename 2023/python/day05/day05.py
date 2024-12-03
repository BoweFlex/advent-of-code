"""
Puzzle Input: Almanac
    Lists all seeds that need to be planted, what type of soil to use w/ each
    seed, what type of fertilizer to use w/ each soil, what type of water to
    use w/ each fert. Each identified w/ a number, but numbers reused by
    category, soil 123 and fert 123 can both exist and not necessarily related.
Lines:
    - "seeds" line w/ list of seed numbers.
    - map identifier: i.e. "water-to-light map:"
    - map: how to convert source category to dest.
      - first num: destination range start
      - second num: source range start
      - third num: range length
Sources not mapped correspond to same dest number.
Part 1: Find the lowest location number that corresponds to any of the
    initial seeds.
Part 2: Seeds line is actually a range of seed numbers. Split into
pairs, first value is start of range and second value is length of range.
    What is the lowest location number that corresponds to any
    initial seed numbers?
"""

import sys


def find_lowest_location_range(input_file):
    # seeds is a list of dictionaries, with values:
    # seed, soil, fertilizer, water, light, temperature, humidity, location
    seeds = []
    with open(input_file, 'r') as almanac:
        maps = {}
        source, dest = '', ''
        is_seed = True
        seed_start, seed_range = 0, 0
        for line in almanac:
            if line.startswith("seeds"):
                for seed_num in line.split(':')[-1].split():
                    if is_seed:
                        seed_start = int(seed_num)
                        is_seed = False
                        continue
                    else:
                        seed_range = int(seed_num)
                        is_seed = True
                        # This makes it take WAY too much CPU and eventually times out
                        # for seed in range(seed_start, seed_start + seed_range):
                        # seeds.append({"seed": seed})
                        seeds.append({"seed": seed_start, "range": seed_range})
                print(seeds)
            elif line.endswith("map:\n"):
                if source != '':
                    for seed in seeds:
                        if seed.get(dest) is None:
                            seed.update({dest: seed[source]})
                source, _, dest = line.split()[0].split('-')
                maps.update({dest: {}})
            elif not line.isspace():
                dest_start, source_start, range_length = list(map(int, line.split()))
                maps[dest].update({"dest": dest_start, "source_range": [i for i in range(source_start, source_start + range_length)]})
        for mapping in maps:
            print(mapping)
        for seed in seeds:
            if seed.get(dest) is None:
                seed.update({dest: seed[source]})
            print(seed)
        return f'The lowest location in the provided almanac is {min(seed["location"] for seed in seeds)}'


def find_lowest_location(input_file):
    # seeds is a list of dictionaries, with values:
    # seed, soil, fertilizer, water, light, temperature, humidity, location
    seeds = []
    with open(input_file, 'r') as almanac:
        source, dest = '', ''
        for line in almanac:
            if line.startswith("seeds"):
                for seed_num in line.split(':')[-1].split():
                    seeds.append({"seed": int(seed_num)})
            elif line.endswith("map:\n"):
                if source != '':
                    for seed in seeds:
                        if seed.get(dest) is None:
                            seed.update({dest: seed[source]})
                source, _, dest = line.split()[0].split('-')
            elif not line.isspace():
                dest_start, source_start, range_length = list(map(int, line.split()))
                for seed in seeds:
                    if seed[source] in range(source_start, source_start + range_length):
                        dest_num = dest_start + (seed[source] - source_start)
                        seed.update({dest: dest_num})
        for seed in seeds:
            if seed.get(dest) is None:
                seed.update({dest: seed[source]})
        return f'The lowest location in the provided almanac is {min(seed["location"] for seed in seeds)}'



try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(find_lowest_location(input_file))
    print(find_lowest_location_range(input_file))
else:
    print('Please provide a valid file path!')
