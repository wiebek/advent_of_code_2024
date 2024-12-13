#!/usr/bin/env python

def grid_char(r, c, h, w, data):
    if 0 <= r < h and 0 <= c < w:
        return data[r][c]
    return ''

def part1_count(r: int, c: int, h: int, w: int, data: list) -> int:
    if data[r][c] != 'X':
        return 0

    deltas = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    count = 0

    for dr, dc in deltas:
        rr, cc = r, c
        for i in range(3):
            rr += dr
            cc += dc
            if grid_char(rr, cc, h, w, data) != 'MAS'[i]:
                break
        else:
            count += 1
    
    return count

def part2_count(r: int, c: int, h: int, w: int, data: list) -> bool:
    if data[r][c] != 'A':
        return False

    a = grid_char(r-1, c-1, h, w, data) + grid_char(r+1, c+1, h, w, data)
    if a != 'MS' and a != 'SM':
        return False

    b = grid_char(r+1, c-1, h, w, data) + grid_char(r-1, c+1, h, w, data)
    return b == 'MS' or b == 'SM'

def main(file_name):
    """
    Day 4 with help from mebeim
    https://github.com/mebeim/aoc/blob/master/2024/solutions/day04.py
    """
    data = None
    with open(file_name, 'r') as f:
        data = f.read().splitlines()

    h = len(data)
    w = len(data[0])

    print(f"Part 1: {sum(part1_count(r, c, h, w, data) for r in range(h) for c in range(w))}")
    print(f"Part 2: {sum(part2_count(r, c, h, w, data) for r in range(h) for c in range(w))}")

if __name__ == "__main__":
    file_name = "data4.txt"
    main(file_name=file_name)
