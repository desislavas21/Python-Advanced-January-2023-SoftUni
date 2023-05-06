# You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
# A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end.
# The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.
#Input
# 5 6
# SoftUni
# Output
# SoftUn
# UtfoSi
# niSoft
# foSinU
# tUniSo
from collections import deque
rows, columns = list(map(int, input().split(" ")))
data = deque(input())
matrix = [deque() for row in range(rows)]

for row in range(len(matrix)):
    for column in range(columns):
        current_letter = data.popleft()
        if row % 2 == 0:
            matrix[row].append(current_letter)
        else:
            matrix[row].appendleft(current_letter)
        data.append(current_letter)

for row in matrix:
    print("".join(row))
