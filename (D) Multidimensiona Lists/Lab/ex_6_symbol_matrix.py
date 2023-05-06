# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,
# you will receive rows of the matrix.
# Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
# You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".
# Input
# 3
# ABC
# DEF
# X!@
# !
# Output
# (2, 1)
# Input
# 4
# asdd
# xczc
# qwee
# qefw
# 4
# Output
# 4 does not occur in the matrix
n = int(input())
matrix = []
for row in range(n):
    matrix.append([])
    data = list(input())
    for item in data:
        matrix[row].append(item)
symbol = input()
data = ""
for row in range(len(matrix)):
    current_row = matrix[row]
    if symbol in current_row:
        for column in range(len(current_row)):
            if current_row[column] == symbol:
                data = f"({row}, {column})"
                break
            else:
                continue
    else:
        continue
if data:
    print(data)
else:
    print(f"{symbol} does not occur in the matrix")

