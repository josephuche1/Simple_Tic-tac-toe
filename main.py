# program for simple tic-tac-toe
import utilities as func
game = input()

func.print_game_state(game)

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

