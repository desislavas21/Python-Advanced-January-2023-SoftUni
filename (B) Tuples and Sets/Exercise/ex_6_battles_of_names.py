# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
# Input	        Output
# 4
# Pesho
# Stefan
# Stamat
# Gosho	        304, 128, 206, 511
# Input	        Output
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan	    733, 101

n = int(input())
odd, even = set(), set()
for index in range(1, n+1):
    name = list(input())
    result = int(sum([ord(x) for x in name]) / index)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)
sum_odd = sum(odd)
sum_even = sum(even)
diff = 0
if sum_odd == sum_even:
    diff = odd.union(even)
elif sum_odd > sum_even:
    diff = odd.difference(even)
elif sum_even > sum_odd:
    diff = odd.symmetric_difference(even)
print(*diff, sep=", ")