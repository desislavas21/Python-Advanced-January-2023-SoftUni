# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.
# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Output
# 15
n = int(input())
matrix = [[int(x) for x in input().split(" ")] for row in range(n)]
primary_diagonal = [matrix[index][index] for index in range(len(matrix))]
secondary_diagonal = [matrix[index][(len(matrix)-1) - index] for index in range(len(matrix))]
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
