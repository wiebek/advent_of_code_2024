#!/usr/bin/env python
from collections import Counter


def main(file_name):
    """
    Day 1 of Advent of code
    Example list:
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3

    Part1:
    Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
    In the example list above, the pairs and distances would be as follows:
    The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
    The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
    The third-smallest number in both lists is 3, so the distance between them is 0.
    The next numbers to pair up are 3 and 4, a distance of 1.
    The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
    Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.

    Part 2:
    This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.

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
