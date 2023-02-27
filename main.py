# program for simple tic-tac-toe

game_state = input()
start = 0
stop = 3
print("---------")
while stop <= len(game_state):
    row = game_state[start:stop]
    formatted_row = " ".join(row)
    print(f"| {formatted_row} |")
    start = stop
    stop = start + 3
print("---------")
