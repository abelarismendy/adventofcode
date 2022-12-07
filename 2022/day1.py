"""
--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas.
For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you
on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves
assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is
unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally
goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food
- in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought
with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

More details in the puzzle description: https://adventofcode.com/2022/day/1
"""

def first_part(data):
    max_calories = 0
    actual_calories = 0
    for line in data.splitlines():
        if line == "":
            if actual_calories > max_calories:
                max_calories = actual_calories
            actual_calories = 0
        else:
            actual_calories += int(line)
    return max_calories

def second_part(data):
    top_3 = [0,0,0]
    actual_calories = 0
    for line in data.splitlines():
        if line == "":
            if actual_calories > min(top_3):
                top_3.remove(min(top_3))
                top_3.append(actual_calories)
            actual_calories = 0
        else:
            actual_calories += int(line)
    return sum(top_3)

if __name__ == '__main__':
    print("--- Day 1: Calorie Counting ---")
    with open("day1.txt", "r") as f:
        data = f.read()
        max_calories = first_part(data)
        print(f"The Elve carrying most calories has: {max_calories} calories")
        top_3 = second_part(data)
        print(f"The top 3 Elve carrying most calories have (in total): {top_3} calories")