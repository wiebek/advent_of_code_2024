#!/usr/bin/env python

from re import findall

def main(file_name):
    """
    Solution taken from mebeim (https://github.com/mebeim)
    https://github.com/mebeim/aoc/blob/master/2024/solutions/day03.py
    """

    total1 = total2 = 0
    enabled = True
    data = open(file_name).read()

    for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        print(a,b)
        print(bool(do))
        print(bool(dont))
        if do or dont:
            enabled = bool(do)
        else:
            x = int(a) * int(b)
            total1 += x
            total2 += x * enabled

    print(total1, total2)

if __name__ == "__main__":
    file_name = "test3.txt"
    main(file_name)