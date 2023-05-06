# Create a recursive function called recursive_power() which should receive a number and a power. Using recursion,
# return the result of number ** power. Submit only the function in the judge system.
# Test Code	                        Output
# print(recursive_power(2, 10))	    1024
# print(recursive_power(10, 100))	10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def recursive_power(number, power):
    number = number * number
    recursive_power(number, power - 1)
    return number



print(recursive_power(2, 10))
print(recursive_power(10, 100))

