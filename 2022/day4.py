"""
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships,
and so several Elves have been assigned the job of cleaning up sections of the camp.
Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other,
they've noticed that many of the assignments overlap. To try to quickly find overlaps
and reduce duplicated effort, the Elves pair up and make a big list of the section
assignments for each pair (your puzzle input).

More details in the puzzle description: https://adventofcode.com/2022/day/4
"""
import numpy as np

def first_part(data):
    incorrect = 0
    data = data.splitlines()
    for pair in data:
        first_elve, second_elve = pair.split(",")
        first_elve_s, first_elve_e = first_elve.split("-")
        second_elve_s, second_elve_e = second_elve.split("-")

        first_range = set(np.arange(int(first_elve_s), int(first_elve_e)+1))
        second_range = set(np.arange(int(second_elve_s), int(second_elve_e)+1))

        if first_range.issubset(second_range) or second_range.issubset(first_range):
            incorrect += 1
    return incorrect

def second_part(data):
    incorrect = 0
    data = data.splitlines()
    for pair in data:
        first_elve, second_elve = pair.split(",")
        first_elve_s, first_elve_e = first_elve.split("-")
        second_elve_s, second_elve_e = second_elve.split("-")

        first_range = set(np.arange(int(first_elve_s), int(first_elve_e)+1))
        second_range = set(np.arange(int(second_elve_s), int(second_elve_e)+1))

        if first_range.intersection(second_range):
            incorrect += 1
    return incorrect

if __name__ == '__main__':
    print("--- Day 4: Camp Cleanup ---")
    with open("input/day4.txt", "r") as f: data = f.read()
    print("First part:", first_part(data))
    print("Second part:", second_part(data))