# Write a program that reads a matrix from the console and performs certain operations with its elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.
#Input
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# Output
# 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6
# Input
# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# Output
# Invalid input!
# World Hello
# Hello World

def read_matrix(r, c):
    matrix = []
    for _ in range(r):
        data = input().split(" ")
        matrix.append(data)
    return matrix


def swap(row_1, col_1, row_2, col_2, matrix):
    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]


rows, columns = list(map(int, input().split(" ")))
matrix = read_matrix(rows, columns)
while True:
    data = input()
    if data == "END":
        break
    command = data.split(" ")
    if "swap" == command[0] and len(command) == 5:
        r_1 = int(command[1])
        c_1 = int(command[2])
        r_2 = int(command[3])
        c_2 = int(command[-1])
        if r_1 in range(rows) and r_2 in range(rows) and c_1 in range(columns) and c_2 in range(columns):
            swap(r_1, c_1, r_2, c_2, matrix)
            for row in matrix:
                print(" ".join(row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
