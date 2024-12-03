"""
Puzzle Input: Camel Cards
Part 1: Find the rank of every hand in your set. What are the total winnings?
    Total winnings = sum(rank * bid)
    CURRENT SOLUTION WORKS FOR EXAMPLE BUT NOT FULL INPUT
Part 2:
"""

import sys


def get_hand_strength(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts.keys():
            card_counts[card] += 1
        else:
            card_counts.update({card: 1})
    if 5 in card_counts.values():
        return 7
    elif 4 in card_counts.values():
        return 6
    elif 3 in card_counts.values() and 2 in card_counts.values():
        return 5
    elif 3 in card_counts.values():
        return 4
    elif sum(count for count in card_counts.values() if count == 2) == 4:
        return 3
    elif 2 in card_counts.values():
        return 2
    else:
        return 1


def sort_by_rank(hands):
    swapped = True
    while swapped is True:
        swapped = False
        for index, hand in enumerate(hands):
            if index > 0:
                prev_hand = hands[index-1]
                if prev_hand[2] > hand[2]:
                    temp = prev_hand
                    hands[index-1] = hand
                    hands[index] = temp
                    swapped = True
                elif prev_hand[2] == hand[2]:
                    card_priorities = "AKQJT98765432"
                    print(prev_hand, hand)
                    for i in range(len(hand[0])):
                        if (card_priorities.index(prev_hand[0][i]) <
                                card_priorities.index(hand[0][i])):
                            print(prev_hand[0][i], hand[0][i])
                            temp = prev_hand
                            hands[index-1] = hand
                            hands[index] = temp
                            break
    return hands


def get_total_winnings(input_file):
    hand_ranks = []
    winnings = 0
    with open(input_file, 'r') as file:
        for line in file:
            hand, bid = line.split()
            hand_str = get_hand_strength(hand)
            hand_ranks.append([hand, int(bid), hand_str])
        print(f'unsorted: {hand_ranks}')
        hand_ranks = sort_by_rank(hand_ranks)
        print(f'sorted: {hand_ranks}')
        for index, ranked_hand in enumerate(hand_ranks):
            winnings += (index + 1) * ranked_hand[1]
    return f'The total winnings for these hands is {winnings}'


try:
    input_file = sys.argv[1]
except NameError:
    input_file = None

if input_file is not None:
    print(get_total_winnings(input_file))
else:
    print("Please provide a input file!")
