# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. On the following few lines,
# you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right. If you reach a trap while
# checking some of the directions, you should not consider the fields after the trap in this direction.
# For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
# Output
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87
# Input
# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
# Output
# down
# [6, 2]
# [7, 2]
# 113
n = int(input())
matrix, bunny_pos, best_positions = [], [], []
best_direction = ''
eggs_collected = float("-inf")
field_range = range(0, n)
paths = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for r in range(n):
    current_row = input().split()
    if "B" in current_row:
        bunny_pos.append(r)
        bunny_pos.append(current_row.index("B"))
    matrix.append(current_row)

for direction, coordinates in paths.items():
    matrix_copy = matrix.copy()
    bunny_pos_copy = bunny_pos.copy()
    current_positions = []
    eggs_current = 0

    while True:
        if bunny_pos_copy[0] + coordinates[0] in field_range \
                and bunny_pos_copy[1] + coordinates[1] in field_range \
                and matrix_copy[bunny_pos_copy[0] + coordinates[0]][bunny_pos_copy[1] + coordinates[1]] != "X":
            current_el = matrix_copy[bunny_pos_copy[0] + coordinates[0]][bunny_pos_copy[1] + coordinates[1]]
            eggs_current += int(current_el)
            bunny_pos_copy = [bunny_pos_copy[0] + coordinates[0], bunny_pos_copy[1] + coordinates[1]]
            current_positions.append(bunny_pos_copy)
        else:
            break

    if eggs_current > eggs_collected and current_positions:
        best_positions = current_positions
        eggs_collected = eggs_current
        best_direction = direction

print(best_direction)
[print(el) for el in best_positions]
print(eggs_collected)
