# We think the process of making honey is amazing! Let's learn more about how bees make honey.
# Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load and pass the nectar to waiting bees so they can really start the honey-making process.
# You will receive 3 sequences:
# •	a sequence of integers, representing working bees
# •	a sequence of integers, representing nectar
# •	a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey waiting bees made with the collected nectar.
# Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last nectar:
# •	If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the hive to drop off the load (step two).
# •	If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with the next nectar's value until the bee collects enough nectar.
# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made. Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
# "{matched_bee} {symbol} {matched_nectar}"
# The result represents the honey that is made from the passed nectar. The calculation should always return the absolute value of the result. After the calculation, remove the bee, the nectar, and the symbol.
# Stop making honey when you are out of bees or nectar.
# Input
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
# Output
# Total honey made: 148
# Bees left: 99, 35, 0, 150
# Input
# 30
# 15 9 5 150 8
# * + + * -
# Output
# Total honey made: 4500
# Nectar left: 15, 9, 5

from collections import deque
working_bees = deque(int(x) for x in input().split(" "))
nectar = deque(int(x) for x in input().split(" "))
symbols = deque(input().split(" "))
honey = 0
while nectar and working_bees:
    current_bee = working_bees.popleft()
    curr_nectar = nectar.pop()
    if current_bee <= curr_nectar:
        symbol = symbols.popleft()
        if symbol == "+":
            honey += abs(current_bee + curr_nectar)
        elif symbol == "-":
            honey += abs(current_bee - curr_nectar)
        elif symbol == "*":
            honey += abs(current_bee * curr_nectar)
        elif symbol == "/":
            if curr_nectar != 0:
                honey += abs(current_bee / curr_nectar)
    else:
        working_bees.appendleft(current_bee)
        continue

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")