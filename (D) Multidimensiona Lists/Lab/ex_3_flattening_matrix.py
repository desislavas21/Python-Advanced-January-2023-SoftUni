# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column separated with a comma and a space ", ".
# Input
# 2
# 1, 2, 3
# 4, 5, 6
# Output
# [1, 2, 3, 4, 5, 6]
# Input
# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
# Output
# [10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]

rows = int(input())
initial_matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
matrix = []
for sub in initial_matrix:
    for item in sub:
        matrix.append(item)
print(matrix)