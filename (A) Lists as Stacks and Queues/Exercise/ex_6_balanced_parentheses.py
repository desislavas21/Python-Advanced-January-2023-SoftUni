# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input	        Output
# # {[()]}	    YES
# {[(])}	    NO
# {{[[(())]]}}	YES
from collections import deque
data = deque(input())
open = deque()
while data:
    item_left = data.popleft()
    if item_left in "{[(":
        open.append(item_left)
    elif not open:
        print("NO")
        break
    else:
        if f"{open.pop()+item_left}" not in "[]{}()":
            print("NO")
            break
else:
    print("YES")
