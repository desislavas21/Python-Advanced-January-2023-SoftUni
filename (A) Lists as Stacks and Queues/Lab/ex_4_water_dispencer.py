# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".
# Input
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End
# Output
# Peter got water
# Amy got water
# 0 liters left
# Input
# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# Output
# Peter got water
# George got water
# Amy got water
# Alice must wait
# 2 liters left
from collections import deque
people = deque()
quantity = int(input())
start_command = "Start"
end_command = "End"
refill_command = "refill"
while True:
    data = input()
    if data == start_command:
        break
    people.append(data)
while True:
    data = input()
    if data == end_command:
        break
    elif refill_command in data:
        litters = int((data.split(" "))[1])
        quantity += litters
    else:
        if quantity >= int(data):
            quantity -= int(data)
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
print(f"{quantity} liters left")
