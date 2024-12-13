#!/usr/bin/env python

from collections import defaultdict

def find_correct_page(pages: list, order_rules: dict) -> bool:
    found = []
    for i, page in enumerate(pages):
        if pages[i+1:]:
            found.append(all([x in order_rules[page] for x in pages[i+1:]]))
    return all(found)

def main(file_name):
    """
    Day 5
    """
    part1_count = 0
    order_rules = defaultdict(list)
    safety_manuals = []
    incorrect_manuals = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if "|" in line:
                n, u = line.split("|")
                order_rules[n].append(u)
            elif ',' in line:
                safety_manuals.append(line.split(","))

    for pages in safety_manuals:
        found = []
        for i, page in enumerate(pages):
            if pages[i+1:]:
                found.append(all([x in order_rules[page] for x in pages[i+1:]]))
        if all(found):
            part1_count += int(pages[len(pages) // 2])
        else:
            incorrect_manuals.append(pages)

    print(f"Part 1: {part1_count}")

    print(incorrect_manuals)
    part2_count = 0

    for incorrect_pages in incorrect_manuals:
        done = False
        while not done:
            if find_correct_page(incorrect_pages, order_rules):
                done = True
            else:
                # check per position if it is correct
                for i, incorrect_page in enumerate(incorrect_pages):
                    if (order_rules[incorrect_page] == []):
                        incorrect_page = incorrect_page + [incorrect_page.pop(i)]
                        continue
                    for x in order_rules[incorrect_page]:
                        print(i, incorrect_page, order_rules[incorrect_page])
                        if x not in incorrect_pages[i+1:]:
                            print(incorrect_pages)
                            incorrect_pages[i+1], incorrect_pages[i] = incorrect_pages[i], incorrect_pages[i+1]
                            break


    # Check if rule is correct
    # if not, then pop the element out of the list and put in in the back
    # keep doing this until the list is correct.
                

if __name__ == "__main__":
    file_name = "test5.txt"
    main(file_name=file_name)
