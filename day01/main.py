#!/usr/bin/env python


def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def value_for_line(l):
    numbers = [int(char) for char in l if char.isnumeric()]
    return 10*numbers[0] + numbers[-1]

def substiture_numbers(l):
    mapping = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    for s, i in mapping.items():
        l = l.replace(s, s+str(i)+s)
    print(l)
    return l


def main():
    puzzle_input = read_input('input.txt')
    values = []
    for line in puzzle_input:
        l = substiture_numbers(line)
        values.append(value_for_line(l))

    print(sum(values))


if __name__ == '__main__':
    main()

