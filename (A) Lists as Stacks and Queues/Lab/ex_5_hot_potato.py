# Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid. Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the next kid. It continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a single space. On the second line, you will receive the nth toss (integer) in which a child leaves the game.
# Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in the format "Last is {kid}".
# Input
# Tracy Emily Daniel
# 2
# Output
# Removed Emily
# Removed Tracy
# Last is Daniel
# Input
# George Peter Michael William Thomas
# 10
# Output
# Removed Thomas
# Removed Peter
# Removed Michael
# Removed George
# Last is William
# Input
# George Peter Michael William Thomas
# 1
# Output
# Removed George
# Removed Peter
# Removed Michael
# Removed William
# Last is Thomas
from collections import deque

name_of_players = input().split(' ')
step_of_hot_potato = int(input())

players_deque = deque(name_of_players)
counter = 0

while len(players_deque) > 1:
    counter += 1
    current_name_of_player = players_deque.popleft()

    if counter == step_of_hot_potato:
        print(f'Removed {current_name_of_player}')
        counter = 0
    else:
        players_deque.append(current_name_of_player)

print(f'Last is {players_deque[0]}')