# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
# Examples
# Input
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# Output
# Primary diagonal: 1, 5, 9. Sum: 15
# Secondary diagonal: 3, 5, 7. Sum: 15

matrix = [[x for x in input().split(", ")] for row in range(int(input()))]
main = [matrix[index][index] for index in range(len(matrix))]
secondary = [matrix[index][len(matrix) - index - 1] for index in range(len(matrix))]
print(f"Primary diagonal: {', '.join(main)}. Sum: {sum([int(x) for x in main])}")
print(f"Secondary diagonal: {', '.join(secondary)}. Sum: {sum([int(x) for x in secondary])}")
