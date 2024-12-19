#!/usr/bin/env python

import re

def create_new_elements(dots, number):
    """
    number will always be shorter or as long as dots
    dots = '...'
    number = "99"

    return "99." and ".."
    """
    if len(dots) == len(number):
        return [[number], dots]
    else:
        result = '.' * (len(dots) - len(number))
        return [[number, result], len(number) * '.']


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

    #### PART 2
    s = []
    index = 0
    for i in range(len(data)):
        if i % 2 == 0:
            s = s + [int(data[i]) * str(index)]
            index += 1
        else:
            s = s + [int(data[i]) * '.']

    len_s = list(map(len, s))
    print(s)
    for i in range(len(s)-1, 0, -1):
        if "." not in s[i] and s[i]:
            lc = [(len_s[i] <= len_s[n], n) for n in range(len(len_s[:i])) if "." in s[n]]
            # >>> re.findall("\.+", "0099.1117772...333.44.5555.6666.....8888..")
            # ['.', '...', '.', '.', '.', '.....', '..']
            # >>> re.finditer("\.+", "0099.1117772...333.44.5555.6666.....8888..")
            # <callable_iterator object at 0x7f77936ff940>
            # >>> [m.start(0) for m in re.finditer("\.+", "0099.1117772...333.44.5555.6666.....8888..")]
            # [4, 12, 18, 21, 26, 31, 40]
            # >>> 
            if any(lc):
                lc2 = [i for i, _ in lc]
                if any(lc2):
                    print(s[i])
                    index_first_true = lc[[i for i, _ in lc].index(1)][1] # [(True, 1), (True, 3), (True, 5), (False, 7), (False, 9), (False, 11), (False, 13), (False, 15)]
                    new_l = create_new_elements(s[index_first_true], s[i])
                    s[i] = new_l[-1]
                    s_str = "".join(s[:index_first_true] + new_l[0] + s[index_first_true+1:])
                    s = re.findall(r'\d+|\.+', s_str)
                    print(s)
                    len_s = list(map(len, s))
    s = "".join(s)
    l = [x for x in s]
    total_p2 = 0
    for i, n in enumerate(l):
        if n != '.':
            total_p2 += (i * int(n))
    print(f"Part2: {total_p2}")


if __name__ == "__main__":
    file_name = "test9.txt"
    main(file_name = file_name)