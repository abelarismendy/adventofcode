"""
--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid.
The Elves explain that a previous expedition planted these trees as a reforestation effort.
Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden.
To do this, you need to count the number of trees that are visible from outside the grid when
looking directly along a row or column.

More details in the puzzle description: https://adventofcode.com/2022/day/8
"""

import math

def input_to_matrix(data):
    data = data.splitlines()
    matrix = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            row.append(int(data[i][j]))
        matrix.append(row)
    return matrix

def first_part(matrix):
    # count the number of trees that are visible by default (the ones on the edges)
    width = len(matrix[0])
    height = len(matrix)
    count = (width + height - 2) * 2

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            tree = matrix[i][j]
            x, y = i, j
            # Check if the current tree is visible horizontally to the right
            visibility = []
            while j < len(matrix[i])-1:
                j+=1
                if tree <= matrix[i][j]:
                    visibility.append('R')
                    break
            j = y
            # Check if the current tree is visible horizontally to the left
            while j > 0:
                j-=1
                if tree <= matrix[i][j]:
                    visibility.append('L')
                    break
            j = y
            # Check if the current tree is visible vertically to the top
            while i > 0:
                i-=1
                if tree <= matrix[i][j]:
                    visibility.append('T')
                    break
            i = x
            # Check if the current tree is visible vertically to the bottom
            while i < len(matrix) - 1:
                i+=1
                if tree <= matrix[i][j]:
                    visibility.append('B')
                    break
            i = x
            if len(visibility) < 4:
                # print("Tree at", i, j, "is visible")
                # print("Tree height:", tree)
                # print(visibility)
                count += 1
    return count

def second_part(matrix):
    max_score = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            tree = matrix[i][j]
            x, y = i, j
            # Check if the current tree is visible horizontally to the right
            visibility = [0,0,0,0]
            while j < len(matrix[i])-1:
                j+=1
                visibility[0]+=1
                if tree <= matrix[i][j]:
                    break
            j = y
            # Check if the current tree is visible horizontally to the left
            while j > 0:
                j-=1
                visibility[1]+=1
                if tree <= matrix[i][j]:
                    break
            j = y
            # Check if the current tree is visible vertically to the top
            while i > 0:
                i-=1
                visibility[2]+=1
                if tree <= matrix[i][j]:
                    break
            i = x
            # Check if the current tree is visible vertically to the bottom
            while i < len(matrix) - 1:
                i+=1
                visibility[3]+=1
                if tree <= matrix[i][j]:
                    break
            i = x
            score = math.prod(visibility)
            if score > max_score:
                max_score = score
    return max_score

if __name__ == "__main__":
    with open("input/day8.txt", "r") as f:
        data = f.read()
    data = input_to_matrix(data)
    print("--- Day 8: Treetop Tree House ---")
    print("First part:", first_part(data))
    print("Second part:", second_part(data))