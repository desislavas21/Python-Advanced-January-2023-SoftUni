#Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for
# each column - N numbers, separated by a single space.
# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Output
# 4
# Input
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# 15
size = int(input())
matrix = []
for row in range(size):
    matrix.append([])
    numbers = list(map(int, input().split(" ")))
    for number in numbers:
        matrix[row].append(number)

counter = 0

for row in range(len(matrix)):
    counter += (matrix[row])[row]
print(counter)