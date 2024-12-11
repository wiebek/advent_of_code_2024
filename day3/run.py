#!/usr/bin/env python

import re

def mul(i: int, j: int) -> int:
    """
    Return multiplication of the numbers
    """
    return i * j

def zip_ranges(do_list: list, dont_list: list) -> list:
    """
    Take 2 lists of unequal length and find the ranges that go from low (in list1) to high (in list2) and have no overlap between them
    """
    range_result = []
    dont_tmp_list = dont_list.copy()
    dont_int = None
    for i, pos in enumerate(do_list):
        if not any([pos in zip_range for zip_range in range_result]): # and not any([dont_tmp_list[i] in zip_range for zip_range in range_result])
            find = True
            previous = True
            while find:
                if previous:
                    dont_int = dont_tmp_list.pop(0)
                    previous = False
                if pos < dont_int:
                    range_result.append(range(pos, dont_int))
                    find = False
                else:
                    dont_int = dont_tmp_list.pop(0)
    return range_result


def main(file_name):
    """
    Day 3
    Part1:
    Example: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).    

    Part2:
    Example: xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    There are two new instructions you'll need to handle:
        The do() instruction enables future mul instructions.
        The don't() instruction disables future mul instructions.
    """
    total_part1 = 0
    pattern_mul = "mul\(\d+,\d+\)"
    pattern_do = "do\(\)"
    pattern_dont = "don't\(\)"

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            muls = re.findall(pattern_mul, line)
            total_part1 += sum([eval(call) for call in muls])
    print(f"Part 1: {total_part1}")

    total_part2 = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()

            muls = re.findall(pattern_mul, line)
            mul_indexes = re.finditer(pattern_mul, line)
            mul_starts = [[i.start(0), i.end(0)] for i in mul_indexes]

            do_indexes = re.finditer(pattern_do, line)
            do_starts = [0] + [i.start(0) for i in do_indexes]

            dont_indexes = re.finditer(pattern_dont, line)
            dont_starts = [i.start(0) for i in dont_indexes]
            dont_starts.append(len(line))

            ranges = zip_ranges(do_starts, dont_starts)

            for i, mul_start in enumerate(mul_starts):
                in_do = any([mul_start[0] in zip_range for zip_range in ranges])
                if in_do:
                    # print(zip_ranges)
                    # print(mul_start)
                    total_part2 += eval(muls[i])
    print(f"Part 2: {total_part2}")



if __name__ == "__main__":
    file_name = "data3.txt"
    main(file_name=file_name)
