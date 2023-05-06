# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
# Present	    Magic needed
# Doll	        150
# Wooden train	250
# Teddy bear	300
# Bicycle 	    400
# You should take the last box with materials and the first magic level value to craft a toy. Their multiplication calculates the total magic level. If the result equals one of the levels described in the table above, you craft the present and remove both materials and magic value. Otherwise:
# •	If the product of the operation is a negative number, you should sum the values together, remove them both from their positions, and add the result to the materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle
# Input
# 10 -5 20 15 -30 10
# 40 60 10 4 10 0
# Output
# The presents are crafted! Merry Christmas!
# Materials left: 20, -5, 10
# Bicycle: 1
# Teddy bear: 2
# Input
# 30 5 15 60 0 30
# -15 10 5 -15 25
# Output
# No presents this Christmas!
# Materials left: 20, 30
# Doll: 1
# Teddy bear: 1
# Input
# 30 10
# 15 10 5 0 10
# Output
# No presents this Christmas!
# Magic left: 5, 0, 10
# Doll: 1
# Teddy bear: 1

from collections import deque
materials = [int(x) for x in input().split(" ")]
magic_level = deque(int(x) for x in input().split(" "))

points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

counts = {}
while materials and magic_level:
    material = materials.pop()
    mgc_level = magic_level.popleft()
    result = material * mgc_level

    if result in points.keys():
        if points[result] not in counts.keys():
            counts[points[result]] = 1
        else:
            counts[points[result]] += 1
        continue

    if result < 0:
        materials.append(material + mgc_level)
    elif result > 0:
        materials.append(material + 15)
    elif result == 0:
        if mgc_level != 0:
            magic_level.appendleft(mgc_level)
        elif material != 0:
            materials.append(material)
dolls_trains = "Doll" in counts.keys() and "Wooden train" in counts.keys()
teddy_and_bicycle = "Teddy bear" in counts.keys() and "Bicycle" in counts.keys()
if dolls_trains or teddy_and_bicycle:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
items = sorted(x for x in counts.keys())
final = {x: counts[x] for x in items}
for key, value in final.items():
    print(f"{key}: {value}")