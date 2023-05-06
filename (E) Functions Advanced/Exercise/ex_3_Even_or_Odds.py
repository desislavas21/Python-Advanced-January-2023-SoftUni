# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.
# Submit only your function in the judge system.

def even_odd(*args):
    *numbers, command = args
    if command == "even":
        return [x for x in numbers if x % 2 == 0]
    else:
        return [x for x in numbers if x % 2 != 0]


# Test Code
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
