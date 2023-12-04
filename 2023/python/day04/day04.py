"""
Set of scratchcards: each has two lists of numbers separated by '|':
    A list of winning numbers and a list of numbers you have.
You need to figure out which of the numbers you have appear in the
list of winning numbers. First match = 1 pt, each match after doubles
the card's point value.

Part 1: How many points are the card's worth in total?
Part 2: You don't get points, cards cause you to win more scratchcards
    = to num of winning numbers you have.
    How many total scratchcards do you end up with?
"""

import sys


def total_scratchcard_count(input_file):
    cards_with_count = list()
    with open(input_file, 'r') as file:
        for line in file:
            card_num, scratch_nums = line.split(':')
            card = {"copies": 1, "card": scratch_nums.strip()}
            cards_with_count.append(card)
        for card_num, card in enumerate(cards_with_count):
            # print(card_num, card)
            winning, owned = card["card"].split('|')
            win_list = winning.split()
            own_list = owned.split()
            for _ in range(card["copies"]):
                wins = 0
                for number in own_list:
                    if number in win_list:
                        wins += 1
                        if card_num + wins >= len(cards_with_count):
                            cards_with_count[-1]["copies"] += 1
                        else:
                            # print(cards_with_count[card_num + wins])
                            cards_with_count[card_num + wins]["copies"] += 1
        total_card_count = sum(card["copies"] for card in cards_with_count)
        return f'The total number of scratchcards with copies is {total_card_count}.'


def total_scratchcard_points(input_file):
    sum = 0
    with open(input_file, 'r') as cardlist:
        for card in cardlist:
            card_worth = 0
            _, numbers = card.split(':')
            winning, owned = numbers.split('|')
            win_list = winning.split()
            own_list = owned.split()
            for number in own_list:
                if number in win_list and card_worth == 0:
                    card_worth = 1
                elif number in win_list:
                    card_worth *= 2
            sum += card_worth

    return f'The scratchcards are worth {sum} points in total.'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(total_scratchcard_points(input_file))
    print(total_scratchcard_count(input_file))
else:
    print("Please provide a input file!")
