# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns
# like the one in the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter:
# o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
# 4 6
# Output
# aaa aba aca ada aea afa
# bbb bcb bdb beb bfb bgb
# ccc cdc cec cfc cgc chc
# ddd ded dfd dgd dhd did
# Input
# 3 2
# Output
# aaa aba
# bbb bcb
# ccc cdc
from string import ascii_lowercase
rows, columns = list(map(int, input().split(" ")))
letters = list(ascii_lowercase)
matrix = []
for row in range(rows):

    column_l = []

    for c in range(columns):
        column = letters[row] + letters[c+row] + letters[row]
        column_l.append(column)

    matrix.append(column_l)
    print(' '.join(column_l))