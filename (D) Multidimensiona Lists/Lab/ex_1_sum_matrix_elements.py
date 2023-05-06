# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ".
# Input
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# Output
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

rows, columns = list(map(int, input().split(", ")))

matrix = []

for i in range(rows):
    matrix.append([])
    rows_data = list(map(int, input().split(", ")))
    for item in rows_data:
        matrix[i].append(item)
total = sum([sum(i) for i in matrix])
print(total)
print(matrix)