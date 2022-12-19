"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately,
that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.
The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors.
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments,
so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

More details in the puzzle description: https://adventofcode.com/2022/day/3
"""

a_z = "abcdefghijklmnopqrstuvwxyz"
A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = a_z + A_Z
priorities = {alphabet[i]: i+1 for i in range(len(alphabet))}

def first_part(data):
    priorities_sum = 0
    for line in data.splitlines():
        first_compartment = set(line[:len(line)//2])
        second_compartment = set(line[len(line)//2:])
        letter = first_compartment.intersection(second_compartment).pop()
        priorities_sum += priorities[letter]
    return priorities_sum

def second_part(data):
    priorities_sum = 0
    i = 0
    data = data.splitlines()
    while i < len(data):
        first_elve = set(data[i])
        second_elve = set(data[i+1])
        third_elve =   set(data[i+2])
        badge = first_elve.intersection(second_elve).intersection(third_elve).pop()
        priorities_sum += priorities[badge]
        i += 3
    return priorities_sum

if __name__ == '__main__':
    print("--- Day 3: Rucksack Reorganization ---")
    with open("input/day3.txt", "r") as f: data = f.read()
    print("First part:", first_part(data))
    print("Second part:", second_part(data))