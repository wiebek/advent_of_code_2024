#!/usr/bin/env python

from itertools import product

def calculate_results(l: list) -> int:
    total = int(l[0])
    for i in range(len(l[1:])):
        if i % 2 != 0:
            n = int(l[i + 1])
            if l[i] == '+':
                total += n
            elif l[i] == '*':
                total *= n
            elif l[i] == "||":
                total = int(f"{total}{l[i+1]}")
    return total

def generate_permutations(numbers):
    operators = ["+", "*"]
    num_slots = len(numbers) - 1  # Number of operator slots
    all_operator_combinations = product(operators, repeat=num_slots)
    
    permutations = []
    for operator_combo in all_operator_combinations:
        # Interleave numbers and operators
        result = []
        for i, num in enumerate(numbers):
            result.append(num)
            if i < len(operator_combo):
                result.append(operator_combo[i])
        # permutations.append(eval("".join(result)))
        permutations.append(result)
    return permutations

def generate_permutations_p2(numbers):
    operators = ["+", "*", "||"]
    num_slots = len(numbers) - 1  # Number of operator slots
    all_operator_combinations = product(operators, repeat=num_slots)
    
    permutations = []
    for operator_combo in all_operator_combinations:
        # Interleave numbers and operators
        result = []
        for i, num in enumerate(numbers):
            result.append(num)
            if i < len(operator_combo):
                result.append(operator_combo[i])
        # permutations.append(eval("".join(result)))
        permutations.append(result)
    return permutations


def main(file_name):
    """
    Day 7
    Each line represents a single equation. The test value appears before the colon on each line;
    it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

    Operators are always evaluated left-to-right, not according to precedence rules.
    Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle,
    you can see elephants holding two different types of operators: add (+) and multiply (*).

    Only three of the above equations can be made true by inserting operators:

    190: 10 19 has only one position that accepts an operator: between 10 and 19.
        Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
    3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators,
        two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
    292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
    """
    results_p1 = 0
    with open(file=file_name, mode='r') as f:
        for line in f:
            r, e = line.strip().split(":")
            e = e.strip().split(" ")
            m = ["+", "*"]

            permutations = generate_permutations(e)
            for p in permutations:
                if int(r) == calculate_results(p):
                    results_p1 += int(r)
                    break

    print(f"Part1: {results_p1}")

    ## Part 1
    results_p2 = 0
    with open(file=file_name, mode='r') as f:
        for line in f:
            r, e = line.strip().split(":")
            e = e.strip().split(" ")

            permutations = generate_permutations_p2(e)
            for p in permutations:
                if int(r) == calculate_results(p):
                    results_p2 += int(r)
                    break
    print(f"Part2: {results_p2}")
    

if __name__ == "__main__":
    file_name = "data7.txt"
    main(file_name=file_name)
