def print_game_state(game):
    start = 0
    stop = 3
    print("---------")
    while stop <= len(game):
        row = game[start:stop]
        formatted_row = " ".join(row)
        print(f"| {formatted_row} |")
        start = stop
        stop = start + 3
    print("---------")


def is_finished(game):
    countx = 0
    counto = 0
    for i in game:
        if i == 'X':
            countx += 1
        elif i == 'O':
            counto += 1
    if countx == counto:
        if countx + counto <= len(game):
            return False
        elif countx + counto == len(game):
            return True
    return True


def is_draw(game):
    if is_finished(game) and not winner(game):
        return "Draw"
    return False


def win_vertical(game):
    start = 0
    stop = 7
    while stop <= len(game):
        countx = 0
        counto = 0
        for i in game[start:stop:3]:
            if i == 'X':
                countx += 1
            elif i == 'O':
                counto += 1
        if countx == 3:
            return "X wins"
        elif counto == 3:
            return "O wins"
        start += 1
        stop += 1
    return False


def win_horizontal(game):
    start = 0
    stop = 3
    while stop <= len(game):
        tracko = 0
        trackx = 0
        for i in game[start:stop]:
            if i == 'X':
                trackx += 1
            elif i == 'O':
                tracko += 1
        if trackx == 3:
            return "X wins"
        elif tracko == 3:
            return "O wins"
        start = stop
        stop += 3
    return False


def win_diagonal(game):
    start = 2
    stop = 7
    step = 2
    while stop <= len(game):
        countx = 0
        counto = 0
        for p in game[start:stop:step]:
            if p == "X":
                countx += 1
            elif p == "O":
                counto += 1
        if countx == 3:
            return "X wins"
        elif counto == 3:
            return "O wins"
        start -= 2
        step += 2
        stop += 2
    return False


def check_by_number(game):  # Checks impossibility based on number of X's and O's
    countx = 0
    counto = 0
    for i in game:
        if i == 'X':
            countx += 1
        elif i == 'O':
            counto += 1

    if countx - counto > 1 or countx - counto < -1:
        return True
    return False


def check_vertical(game):  # Checks impossibility vertically
    start = 0
    stop = 7
    tracker = []
    while stop <= len(game):
        countx = 0
        counto = 0
        for i in game[start:stop:3]:
            if i == 'X':
                countx += 1
            elif i == 'O':
                counto += 1
        if countx == 3 or counto == 3:
            tracker.append(1)
        else:
            tracker.append(0)
        start += 1
        stop += 1
    count = 0
    for track in tracker:
        if track == 1:
            count += 1
        if count > 1:
            return True
    return False


def check_horizontal(game):  # Checks impossibility horizontally
    start = 0
    stop = 3
    tracker = []
    while stop <= len(game):
        countx = 0
        counto = 0
        for i in game[start:stop]:
            if i == 'X':
                countx += 1
            elif i == 'O':
                counto += 1
        if countx == 3 or counto == 3:
            tracker.append(1)
        else:
            tracker.append(0)
        start = stop
        stop += 3
    count = 0
    for track in tracker:
        if track == 1:
            count += 1
        if count > 1:
            return True
    return False


def is_impossible(game):
    if check_vertical(game) or check_by_number(game) or check_horizontal(game):
        return "Impossible"
    else:
        return False


def winner(game):
    if not win_diagonal(game) or not win_vertical(game) or not win_horizontal(game):
        return False
    else:
        return True


def replace_item(game, coordinate1, coordinate2):  # replaces empty position in grid
    if game[coordinate1][coordinate2] == 'X' or game[coordinate1][coordinate2] == 'O':
        return False
    else:
        game[coordinate1][coordinate2] = 'X'
        return True

