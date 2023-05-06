# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
# Output
# Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .
# Output
# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
# Output
# She did it! She went to the party.
# * * . 1 1 . .
# * . . . 6 . 5
# * * . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
size = int(input())
matrix = []
alice_row = 0
alice_column = 0
for row in range(size):
    row_data = input().split(" ")
    matrix.append(row_data)
    if "A" in row_data:
        alice_row = row
        alice_column = row_data.index("A")
make_it = False
tea_bags = 0
while True:
    if tea_bags >= 10:
        make_it = True
        break
    command = input()
    matrix[alice_row][alice_column] = "*"
    if command == "up":
        if alice_row - 1 in range(len(matrix)):
            alice_row -= 1
            if matrix[alice_row][alice_column] == "R":
                break
            elif matrix[alice_row][alice_column].isdigit():
                tea_bags += int(matrix[alice_row][alice_column])
            matrix[alice_row][alice_column] = "A"
        else:
            break
    elif command == "down":
        if alice_row + 1 in range(len(matrix)):
            alice_row += 1
            if matrix[alice_row][alice_column] == "R":
                break
            elif matrix[alice_row][alice_column].isdigit():
                tea_bags += int(matrix[alice_row][alice_column])
            matrix[alice_row][alice_column] = "A"
        else:
            break
    elif command == "right":
        if alice_column + 1 in range(len(matrix[alice_row])):
            alice_column += 1
            if matrix[alice_row][alice_column] == "R":
                break
            elif matrix[alice_row][alice_column].isdigit():
                tea_bags += int(matrix[alice_row][alice_column])
            matrix[alice_row][alice_column] = "A"
        else:
            break
    elif command == "left":
        if alice_column - 1 in range(len(matrix[alice_row])):
            alice_column -= 1
            if matrix[alice_row][alice_column] == "R":
                break
            elif matrix[alice_row][alice_column].isdigit():
                tea_bags += int(matrix[alice_row][alice_column])
            matrix[alice_row][alice_column] = "A"
        else:
            break
matrix[alice_row][alice_column] = "*"
if make_it:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)