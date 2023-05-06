# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console
# Examples
# Input	                Output
# I Love Python	        nohtyP evoL I
# Stacks and Queues	    seueuQ dna skcatS

message = list(input())
final = []

for i in range(len(message)):
    item = message.pop()
    final.append(item)
print("".join(final))