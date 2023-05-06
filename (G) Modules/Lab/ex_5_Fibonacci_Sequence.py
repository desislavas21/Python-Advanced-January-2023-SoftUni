from my_modules.fibonacci import *

operations = {
    "Create": create_sequence,
    "Locate": locate
}

command = input()
while command != "Stop":

    operation, *left = command.split()
    print(operations[operation](int(left[-1])))

    command = input()