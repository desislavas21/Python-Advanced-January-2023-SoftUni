# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Test Code	                        Output
# print(operate("+", 1, 2, 3))	    6
# print(operate("*", 3, 4))	        12
def operate(*args):
    operation, *numbers = args
    if operation == "+":
        return sum(numbers)
    elif operation == "-":
        total = numbers[0]
        for number in numbers[1:]:
            total -= number
        return total
    elif operation == "*":
        total = numbers[0]
        for number in numbers[1:]:
            if number != 0:
                total *= number
            else:
                continue
        return total
    elif operation == "/":
        total = numbers[0]
        for number in numbers[1:]:
            if number != 0:
                total /= number
            else:
                continue
        return total

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
