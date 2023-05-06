# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.
# Input
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# Output
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))
# Input
# (2 + 3) - (2 + 3)
# Output
# 2 + 3)
# (2 + 3)
data = list(input())
indexes = []
for i in range(len(data)):
    if data[i] == "(":
        indexes.append(i)
    if data[i] == ")":
        print("".join(data[indexes.pop():i+1]))