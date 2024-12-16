#!/usr/bin/env python

def turn(directions: list) -> None:
    d = directions.pop(0)
    directions.append(d)

def main(file_name: str) -> None:
    """
    Day 6
    Test input:
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
    Rules:
        - If there is something directly in front of you, turn right 90 degrees.
        - Otherwise, take a step forward.
    """
    with open(file_name, 'r') as f:
        data = f.read().splitlines()

    #print(data)
    barrels = set()
    guard_start_pos = None
    directions = ["up", "right", "down", "left"]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                barrels.add((i, j))
            elif data[i][j] == "^":
                guard_start_pos = [i, j]

    #print(barrels)
    #print(guard_start_pos)

    steps = [guard_start_pos]
    walking = True
    while walking:
        last_step = steps[-1].copy()
        if directions[0] == "up":
            last_step[0] -= 1
        if directions[0] == "right":
            last_step[1] += 1
        if directions[0] == "down":
            last_step[0] += 1
        if directions[0] == "left":
            last_step[1] -= 1

        if last_step[0] > len(data) - 1 or last_step[0] < 0 or last_step[1] > len(data[0]) - 1 or last_step[1] < 0:
            walking = False

        if tuple(last_step) in barrels:
            turn(directions)
        else:
            steps.append(last_step)

    print(f"Part1: {len(set(tuple(i) for i in steps)) - 1}")
    print(steps)

if __name__ == "__main__":
    file_name = "test6.txt"
    main(file_name=file_name)
