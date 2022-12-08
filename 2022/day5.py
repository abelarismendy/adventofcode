"""
-- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships.
Supplies are stored in stacks of marked crates, but because the needed supplies are buried
under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of
the crates get crushed or fall over, the crane operator will rearrange them in a series of
carefully-planned steps. After the crates are rearranged, the desired crates will be at the
top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they
forgot to ask her which crate will end up where, and they want to be ready to unload them as
soon as possible so they can embark.

More details in the puzzle description: https://adventofcode.com/2022/day/5
"""
import numpy as np

def interprete_stacks(data):
    data = data.splitlines()
    n_stacks = (len(data[0])+1)//4
    stacks = {i+1:[] for i in range(n_stacks)}
    for i, line in enumerate(data):
        if line[1] == "1":
            for i, stack in stacks.items():
                stacks[i] = stack[::-1]
            return stacks, data[i+2:]
        for j in range(n_stacks):
            if j == 0:
                letter = line[1]
            elif j == n_stacks-1:
                letter = line[-2]
            else:
                letter = line[4*j+1]
            if letter != " ":
                stacks[j+1].append(letter)

def first_part(stacks,data):
    for op in data:
        __, n, __, inp, __, out = op.split()
        n = int(n)
        inp = int(inp)
        out = int(out)
        # print(op)
        for i in range(n-1):
            # print(i)
            # print(stacks[inp], stacks[out])
            if len(stacks[inp]) > 0:
                print(f"move {stacks[inp][-1]} from {inp} to {out}")
                stacks[out].append(stacks[inp].pop())
            # print(stacks[inp], stacks[out])
        # break
    respone = ""
    print(stacks)
    for stack in stacks.values():
        respone += stack[-1]
    return respone

def second_part(stacks,data):
    incorrect = 0
    return incorrect

if __name__ == '__main__':
    print("--- Day 5: Supply Stacks ---")
    with open("day5.txt", "r") as f: data = f.read()
    stacks, data = interprete_stacks(data)
    print(stacks)
    print("First part:", first_part(stacks,data))
    print("Second part:", second_part(stacks,data))