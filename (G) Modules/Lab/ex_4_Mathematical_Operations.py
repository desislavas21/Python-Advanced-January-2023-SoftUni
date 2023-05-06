from my_modules.math_operations import *

data = input().split()
first_number, sign, second_number = float(data[0]), data[1], int(data[-1])

operations = {
    "/": divide,
    "*": multiply,
    "-": subtract,
    "+": add,
    "^": raise_numbers
}

print(operations[sign](first_number, second_number))