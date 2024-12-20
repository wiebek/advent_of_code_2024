#!/usr/bin/env python

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main(file_name):
    """
    Day 10
    """
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            data.append([x for x in line])
    print(data)

if __name__ == "__main__":
    file_name = "test10.txt"
    main(file_name=file_name)
