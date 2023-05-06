# Write a program that reads a rectangular matrix's'
# dimensions and finds the 3x3 square with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# Output
# Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16
rows, columns = list(map(int, input().split(" ")))
matrix = []
for _ in range(rows):
    rows_data = list(map(int, input().split(" ")))
    matrix.append(rows_data)
maximum_submatrix = []
maximum_points = 0
for rows_index in range(rows - 2):
    for column_index in range(columns - 2):
        submatrix = [
            [matrix[rows_index][column_index], matrix[rows_index][column_index + 1], matrix[rows_index][column_index + 2]],
            [matrix[rows_index + 1][column_index], matrix[rows_index + 1][column_index + 1], matrix[rows_index + 1][column_index + 2]],
            [matrix[rows_index + 2][column_index], matrix[rows_index + 2][column_index + 1], matrix[rows_index + 2][column_index + 2]]
        ]
        total = sum(submatrix[0]) + sum(submatrix[1]) + sum(submatrix[2])
        if total > maximum_points:
            maximum_points = total
            maximum_submatrix = submatrix
print(f"Sum = {maximum_points}")
for row in maximum_submatrix:
    print(' '.join(str(x) for x in row))
