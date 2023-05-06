# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m,
# separated by a single space - representing the lengths of two separate sets. On the next n + m lines,
# you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set.
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}
# Input	    Output
# 4 3       3
# 1         5
# 3
# 5
# 7
# 3
# 4
# 5
# 5
# Input     Output
# 2 2       1
# 1
# 3
# 1
# 5

n, m = [int(x) for x in input().split(" ")]
numbers_n = set()
numbers_m = set()
for _ in range(n):
    number = int(input())
    numbers_n.add(number)
for _ in range(m):
    number = int(input())
    numbers_m.add(number)
result = numbers_n.intersection(numbers_m)
for item in result:
    print(item)