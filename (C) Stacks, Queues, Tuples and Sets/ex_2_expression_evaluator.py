# Write a program that evaluates a string expression. You will be given that string expression on the first line in the form of numbers and operators separated with a single space from each other. Your job is to take that string expression and calculate the result after evaluating it.
# To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", the first time we meet an operator (*), we should take all the numbers we have so far (2, 4), apply that operation to them, and save the result (8). The next time we meet an operator (-), we again take all the numbers we have (8, 1, 3) and apply the operator to them in that order (8 - 1 - 3 = 4). In the end, we print the result.
# All the numbers will always be integers, and the possible operators are "*", "+", "-", "/". It is important to keep the order of the numbers (especially for "/" and "-" because the order matters). When having a division, you should round the result to the lower integer.
# Input	                                    Output
# 6 3 - 2 1 * 5 /                           1
# 2 2 - 1 *	                                0
# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *	    164

from collections import deque
data = deque(input().split(" "))
numbers = deque()

while data:
    current_item = data.popleft()
    if current_item in "*+-/":
        result = int(numbers.popleft())
        while numbers:
            if current_item == "+":
                result += int(numbers.popleft())
            elif current_item == "-":
                result -= int(numbers.popleft())
            elif current_item == "*":
                result *= int(numbers.popleft())
            elif current_item == "/":
                result /= int(numbers.popleft())
                result = int(result)
        numbers.appendleft(result)
    else:
        numbers.append(current_item)

print(numbers[0])