#/usr/bin/env python

import re

PATTERN = r'^Card[\s]{1,3}(\d+): ([\d\s]+) \| ([\d\s]+)$'

puzzle_input = [re.match(PATTERN, line.strip()).groups() for line in open("input.txt").readlines()]
card_counter = [1] * len(puzzle_input)

def number_of_winning_numbers(winning, yours):
    w = set(winning.split(' ')) - set({''})
    y = set(yours.split(' ')) - set({''})
    return len(y.intersection(w))

def score_of_ticket(winning, yours):
    overlap = number_of_winning_numbers(winning, yours)
    return int(2 ** (overlap - 1))

def main():
    # Calculate Part A
    part_a = sum([ score_of_ticket(winning, yours) for round_no, winning, yours in puzzle_input])


    # Calculate Part B
    for index, j in enumerate(puzzle_input):
        game, winning, yours = j
        
        current_ticket_count = card_counter[index]
        overlap = number_of_winning_numbers(winning, yours)

        for next_index in range(overlap):
            card_counter[index + next_index + 1] += current_ticket_count


    print(f"Part A: {part_a}")
    print(f"Part B: {sum(card_counter)}")

if __name__ == '__main__':
    main()