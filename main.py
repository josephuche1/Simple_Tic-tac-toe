# program for simple tic-tac-toe
import utilities as func
game = "         "  # initial game state
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

player = 1

# loop to collect coordinates from players till the game ends
while True:
    try:
        coordinate1, coordinate2 = list(map(int, input().split()))  # checking if coordinates are within game range
        if (coordinate1 in range(1, 4)) and (coordinate2 in range(1, 4)):
            if func.replace_item(games, coordinate1-1, coordinate2-1, player):
                new_game = []
                for i in games:
                    for j in i:
                        new_game.append(j)

                func.print_game_state("".join(new_game))
                game = "".join(new_game)  # changing game state

                # changing between player 1 and 2
                if player == 1:
                    player += 1
                elif player == 2:
                    player -= 1

                # Analyzing game condition and correctness to get winner
                if not func.is_impossible(game):
                    if not func.is_finished(game):
                        pass
                    elif func.win_horizontal(game):
                        print(func.win_horizontal(game))
                        break
                    elif func.win_vertical(game):
                        print(func.win_vertical(game))
                        break
                    elif func.win_diagonal(game):
                        print(func.win_diagonal(game))
                        break

                    elif func.is_draw(game):
                        print(func.is_draw(game))
                        break

                else:
                    print(func.is_impossible(game))

            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")

    except ValueError:  # Prints if exception is encountered
        print("You should enter numbers!")

