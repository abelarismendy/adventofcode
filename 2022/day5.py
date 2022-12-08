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

def interprete_stacks(data):
    data = data.splitlines()
    n_stacks = (len(data[0])+1)//4
    stacks = {i+1:[] for i in range(n_stacks)}
    for i, line in enumerate(data):
        if line[1] == "1":
            for i, stack in stacks.items():
                stacks[i] = stack[::-1]
            return stacks, data[i+1:]
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
    temp_stacks = {i+1:stacks[i+1].copy() for i in range(len(stacks))}
    for op in data:
        _, n, _, from_stack, _, to_stack = op.split()
        n = int(n)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        # print(temp_stacks)
        # print("#"*20)
        # print(op)
        while n > 0:
            # print(f"move {temp_stacks[from_stack][-1]} from {from_stack} to {to_stack}")
            temp_stacks[to_stack].append(temp_stacks[from_stack].pop())
            n -= 1
    respone = ""
    # print(stacks)
    for stack in temp_stacks.values():
        respone += stack.pop()
    return respone

def second_part(stacks,data):
    temp_stacks = {i+1:stacks[i+1].copy() for i in range(len(stacks))}
    for op in data:
        _, n, _, from_stack, _, to_stack = op.split()
        n = int(n)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        # print(temp_stacks)
        # print("#"*20)
        # print(op)
        temp = []
        while n > 0:
            # print(f"move {stacks[from_stack][-1]} from {from_stack} to {to_stack}")
            temp.append(temp_stacks[from_stack].pop())
            n -= 1
        temp = temp[::-1]
        # print(temp)
        temp_stacks[to_stack] += temp
    respone = ""
    # print(stacks)
    for stack in temp_stacks.values():
        respone += stack.pop()
    return respone

if __name__ == '__main__':
    print("--- Day 5: Supply Stacks ---")
    with open("day5.txt", "r") as f: data = f.read()
    stacks, data = interprete_stacks(data)
    # print(stacks)
    print("First part:", first_part(stacks,data))
    print("Second part:", second_part(stacks,data))