# program for simple tic-tac-toe
import utilities as func
game = input()
func.print_game_state(game)
start = 0
stop = 3
count = 0
games = []
while stop <= len(game):
    games.append([])
    for i in game[start:stop]:
        games[count].append(i)
    count += 1
    start = stop
    stop += 3


while True:
    try:
        coordinate1, coordinate2 = list(map(int, input().split()))
        if (coordinate1 in range(1,4)) and (coordinate2 in range(1,4)):
            if func.replace_item(games, coordinate1-1, coordinate2-1):
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")

    except ValueError:
        print("You should enter numbers!")
new_game =[]
for i in games:
    for j in i:
        new_game.append(j)

func.print_game_state("".join(new_game))
'''
if not func.is_impossible(game):
    if func.win_horizontal(game):
        print(func.win_horizontal(game))
    elif func.win_vertical(game):
        print(func.win_vertical(game))
    elif func.win_diagonal(game):
        print(func.win_diagonal(game))
    elif func.is_draw(game):
        print(func.is_draw(game))
    elif not func.is_finished(game):
        print("Game not finished.")

else:
    print(func.is_impossible(game))
'''