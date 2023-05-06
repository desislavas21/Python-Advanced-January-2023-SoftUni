# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line,
# you will receive the matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.
# Input
# 3 4
# A B B D
# E B B B
# I J B B
# Output
# 2
# Input
# 2 2
# a b
# c d
# Output
# 0
rows, columns = list(map(int, input().split(" ")))
matrix = []
for _ in range(rows):
    data_per_row = input().split(" ")
    matrix.append(data_per_row)

identical_submatrix_counter = 0

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        submatrix = [
            [matrix[row_index][column_index], matrix[row_index][column_index + 1]],
            [matrix[row_index + 1][column_index], matrix[row_index + 1][column_index + 1]]]

        if submatrix[0][0] == submatrix[0][1] == submatrix[1][0] == submatrix[1][1]:
            identical_submatrix_counter += 1

print(identical_submatrix_counter)