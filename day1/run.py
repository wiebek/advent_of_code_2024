#!/usr/bin/env python
from collections import Counter


def main(file_name):
    """
    Day 1 of Advent of code
    """
    first_row = []
    second_row = []
    with open(file_name) as f:
        for line in f:
            x, y = list(map(int, line.strip().split()))
            first_row.append(x)
            second_row.append(y)

    first_row.sort()
    second_row.sort()

    print(
        f"Part 1: {sum([abs(first_row[i] - second_row[i]) for i in range(len(first_row))])}"
    )

    first_row_counter = Counter(first_row)
    second_row_counter = Counter(second_row)
    total = 0

    for k, v in first_row_counter.items():
        # This will loop through the amount of times a value is in the first row
        # Then it will multiply it with the amount of times it is in the second row
        total += sum([k * second_row_counter[k] for _ in range(first_row_counter[k])])

    print(f"Part 2: {total}")


if __name__ == "__main__":
    file_name = "data1.txt"
    main(file_name=file_name)
