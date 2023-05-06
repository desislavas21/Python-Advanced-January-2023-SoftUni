# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
# Input
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,10
# Output
# Longest intersection is [6, 7, 8, 9, 10] with length 5
# Input
# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11
# Output
# Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9

saver = []
for i in range(int(input())):
    first, second = input().split("-")
    first_1 = [int(x) for x in first.split(",")]
    second_1 = [int(x) for x in second.split(",")]
    first_2 = set(range(first_1[0], first_1[-1]+1))
    second_2 = set(range(second_1[0], second_1[-1]+1))
    union = first_2.intersection(second_2)
    saver.append(union)
maximum = ""
for item in saver:
    if len(item) > len(maximum):
        maximum = item
maximum = list(map(str, maximum))
print(f"Longest intersection is [{', '.join(maximum)}] with length {len(maximum)}")