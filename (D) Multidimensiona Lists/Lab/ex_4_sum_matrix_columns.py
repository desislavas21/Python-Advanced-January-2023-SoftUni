# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space.
# Input
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# Output
# 12
# 10
# 19
# 20
# 8
# 7
# Input
# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# 12
# 15
# 18
rows, columns = list(map(int, input().split(", ")))
matrix = []
for row in range(rows):
    matrix.append([])
    data = list(map(int, input().split(" ")))
    for number in data:
        matrix[row].append(number)

for columns in range(columns):
    counter = 0
    for row in matrix:
        counter += row[columns]
    print(counter)

