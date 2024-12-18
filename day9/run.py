#!/usr/bin/env python

def main(file_name):
    """
    Day 9

    The disk map uses a dense format to represent the layout of files and free space on the disk.
    The digits alternate between indicating the length of a file and the length of free space.

    Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged,
    starting with ID 0. So, the disk map 12345 has three files:
        a one-block file with ID 0,
        a three-block file with ID 1,
        and a five-block file with ID 2.
    Using one character for each block where digits are the file ID and . is free space,
    the disk map 12345 represents these individual blocks: 0..111....22222
    """
    with open(file_name, 'r') as f:
        data = [x for x in f.read()]
    
    s = []
    index = 0
    for i in range(len(data)):
        if i % 2 == 0:
            s = s + int(data[i]) * [str(index)]
            # print(i, int(data[i]), str(index), int(data[i]) * str(index))
            index += 1
        else:
            s = s + int(data[i]) * ['.']
    # print(s)
    l = [x for x in s]
    l_d = [x for x in l if x != '.']

    for i in range(len(l), 0, -1):
        n = l.pop()
        if n != '.':
            try:
                l[l.index(".")] = n
            except ValueError:
                l = l + [n]
                break

    total = 0
    # print(l)
    for i, n in enumerate(l):
        total += (i * int(n))
    print(f"Part1: {total}")

if __name__ == "__main__":
    file_name = "data9.txt"
    main(file_name = file_name)