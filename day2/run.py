#!/usr/bin/env python
from itertools import combinations


def check_safe(new_list: list) -> bool:
    """
    Check the new list if it will pass the tests
    """
    if all(n > 0 for n in new_list) and all(n1 <= 3 for n1 in new_list):
        return True
    elif all(n < 0 for n in new_list) and all(n1 >= -3 for n1 in new_list):
        return True
    return False


def main(file_name):
    """
    Day 2 solution
    Part 1 rules:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Part 2 rules:
    Now, the same rules apply as before, except if removing a single level from an
    unsafe report would make it safe, the report instead counts as safe.
    """
    safe_part1 = 0
    safe_part2 = 0
    with open(file_name) as f:
        for line in f:
            line = list(map(int, line.strip().split()))
            calculated = [y - x for x, y in zip(line, line[1:])]
            if check_safe(calculated):
                safe_part1 += 1
                safe_part2 += 1
            else:
                checked = False
                results = [list(comb) for comb in combinations(line, len(line) - 1)]
                for result in results:
                    calculated2 = [y - x for x, y in zip(result, result[1:])]
                    if check_safe(calculated2) and not checked:
                        safe_part2 += 1
                        checked = True

    print(f"Part 1: {safe_part1}")
    print(f"Part 2: {safe_part2}")


if __name__ == "__main__":
    file_name = "data2.txt"
    main(file_name=file_name)
