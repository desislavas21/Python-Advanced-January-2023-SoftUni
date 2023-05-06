# Write a program that reads a matrix from the console and changes its values. On the first line, you
# will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a
# single space. You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
# indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
# Input
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# Output
# 6 2 3
# 4 3 6
# 7 8 9
# Input
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# Output
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101
rows = int(input())
matrix = [[] for row in range(rows)]
for row in range(rows):
    data_row = list(map(int, input().split(" ")))
    for x in data_row:
        matrix[row].append(x)


def add(example_matrix, ex_row, ex_col, ex_value):
    example_matrix[ex_row][ex_col] += ex_value
    return example_matrix


def subtract(example_matrix, ex_row, ex_col, ex_value):
    example_matrix[ex_row][ex_col] -= ex_value
    return example_matrix


while True:
    command = input()
    if command == "END":
        break
    data = command.split(" ")
    action = data[0]
    row, column, value = [int(x) for x in data[1:]]
    if row in range(len(matrix)) and column in range(len(matrix[row])):
        if action == "Add":
            matrix = add(matrix, row, column, value)
        elif action == "Subtract":
            matrix = subtract(matrix, row, column, value)
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row, sep=" ")
