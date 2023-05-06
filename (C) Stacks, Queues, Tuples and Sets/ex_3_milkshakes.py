# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to stop making chocolate milkshakes.
# Input
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# Output
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55
# Input
# -10, -2, -30, 10
# -5
# Output
# Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty
# Input
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# Output
# Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6
from collections import deque
chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))
count = 0

while True:
    if count >= 5 or not cups_of_milk or not chocolates:
        break
    current_chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()
    if current_milk <= 0 and current_chocolate <= 0:
        continue
    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    if current_milk == current_chocolate:
        count += 1
        continue
    else:
        cups_of_milk.append(current_milk)
        chocolates.append(current_chocolate - 5)
if count >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")
