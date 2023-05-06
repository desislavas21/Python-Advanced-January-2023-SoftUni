# First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
# Input
# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
# Output
# True
# 1, 2, 3, 4, 5, 6
# 1, 2, 3
# Input
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
# Output
# False
# 2, 3, 4, 5, 6, 9
# 6
sequence_1 = set(map(int, input().split(" ")))
sequence_2 = set(map(int, input().split(" ")))
for _ in range(int(input())):
    data = input()
    data_1 = data.split(" ")
    numbers = []
    for item in data_1:
        if item.isdigit():
            numbers.append(int(item))
    if "Add First" in data:
        for numb in numbers:
            sequence_1.add(numb)
    elif "Add Second" in data:
        for numb in numbers:
            sequence_2.add(numb)
    elif "Remove First" in data:
        for numb in numbers:
            if numb in sequence_1:
                sequence_1.remove(numb)
    elif "Remove Second" in data:
        for numb in numbers:
            if numb in sequence_2:
                sequence_2.remove(numb)
    elif "Check Subset" in data:
        if sequence_1.issubset(sequence_2) or sequence_2.issubset(sequence_1):
            print(True)
        else:
            print(False)
print(*sorted(sequence_1), sep=", ")
print(*sorted(sequence_2), sep=", ")