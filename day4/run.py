#!/usr/bin/env python

def main(file_name):
    """
    Day 4
    """
    data = None
    with open(file_name, 'r') as f:
        data = f.read().splitlines()

    total_xmax_part1 = 0

    data2 = [[i for i in x] for x in data]
    for i in range(len(data2)):
        for j in range(len(data2[i])):
            # Check left to right:
            if j+3 < len(data[i]):
                if (data2[i][j] + data2[i][j+1] + data2[i][j+2] + data2[i][j+3]) == "XMAS" or (data2[i][j] + data2[i][j+1] + data2[i][j+2] + data2[i][j+3]) == "SAMX":
                    total_xmax_part1 += 1
            # Check down and up
            if i+3 < len(data2):
                if (data2[i][j] + data2[i+1][j] + data2[i+2][j] + data2[i+3][j]) == "XMAS" or (data2[i][j] + data2[i+1][j] + data2[i+2][j] + data2[i+3][j]) == "SAMX":
                    total_xmax_part1 += 1

            # Check diagonal right checked
            if i+3 < len(data2) and j+3 < len(data[i]):
                if (data2[i][j] + data2[i+1][j+1] + data2[i+2][j+2] + data2[i+3][j+3]) == "XMAS" or (data2[i][j] + data2[i+1][j+1] + data2[i+2][j+2] + data2[i+3][j+3]) == "SAMX":
                    total_xmax_part1 += 1

            # Check diagonal left checked
            if i-3 > -1 and j-3 > -1:
                if (data2[i][j] + data2[i-1][j-1] + data2[i-2][j-2] + data2[i-3][j-3]) == "XMAS" or (data2[i][j] + data2[i-1][j-1] + data2[i-2][j-2] + data2[i-3][j-3]) == "SAMX":
                   total_xmax_part1 += 1

    print(f"Part1: {total_xmax_part1}")

if __name__ == "__main__":
    file_name = "test4.txt"
    main(file_name=file_name)
