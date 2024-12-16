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

    #print(incorrect_manuals)
    part2_count = 0

    #######################################
    ############### Part 2 ################
    #######################################


    def findInvalid(nums,i, rule):
        v = nums[i]
        if v not in rule:
            return -1
        for j in range(i):
            if nums[j] in rule[v]:
                return j
        return -1

    def mySort(nums, rule, step=0):
        p=-1
        for i in range(len(nums)):
            p = findInvalid(nums, i, rule)
            if(p!=-1):
                nums = nums[:p]+[nums[i]]+nums[p:i]+nums[i+1:]
                break
        if(p==-1):
            return nums
        return mySort(nums, rule, step+1)

    def process(nums, rule):
        read = set()
        for n in nums:
            if n in rule and len(rule[n].intersection(read))>0:
                return 0
            read.add(n)
        return nums[len(nums)//2]

    rule = {}

    with open(file=file_name, mode='r') as f:
        for l in f:
            if len(l.strip())==0 or "," in l:
                continue
            a,b = [int(x) for x in l.strip().split("|")]
            if a not in rule:
                rule[a]=set()
            rule[a].add(b)

    #print(rule)

    with open(file=file_name, mode='r') as f:
        for l in f:
            if len(l.strip())==0 or "|" in l:
                continue
            nums= [int(x) for x in l.strip().split(",")]
            points = process(nums, rule)
            if points != 0:
                #already valid
                continue
            nums = mySort(nums, rule)
            part2_count+=process(nums, rule)
    print(f"Part1: {part2_count}")


if __name__ == "__main__":
    file_name = "data5.txt"
    main(file_name=file_name)
