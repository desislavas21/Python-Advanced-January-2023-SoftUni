# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
# Input
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# Output
# 9 8
# 7 9
# 33
# Input
# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
# Output
# 12 13
# 16 17
# 58
rows, columns = list(map(int, input().split(", ")))
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

maximum = 0
greatest_sub = ''
for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        sub_matrix = [[matrix[row_index][column_index], matrix[row_index][column_index + 1]],
                      [matrix[row_index + 1][column_index], matrix[row_index+1][column_index+1]]]
        sum_sub_matrix = sum(sub_matrix[0]) + sum(sub_matrix[1])
        if sum_sub_matrix > maximum:
            maximum = sum_sub_matrix
            greatest_sub = sub_matrix
for row in greatest_sub:
    row_str = [str(x) for x in row]
    print(" ".join(row_str))
print(maximum)