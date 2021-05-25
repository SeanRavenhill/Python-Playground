def print_board():
    print("---------")
    print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
    print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
    print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
    print("---------")


def make_move():
    marker = marker_switch(grid)
    coordinates = input("Enter the coordinates: ").split()
    if coordinates[0] not in numbers or coordinates[1] not in numbers:
        print(coordinates_states.get(0))
        make_move()
    elif coordinates[0] not in valid or coordinates[1] not in valid:
        print(coordinates_states.get(1))
        make_move()
    elif grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != " ":
        print(coordinates_states.get(2))
        make_move()
    else:
        grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = marker
        print_board()
        game_state()


def game_state():
    play = ""

    for item in grid:
        for character in item:
            play += character

    print("play string is:", play)

    x_moves = play.count("X")
    o_moves = play.count("O")
    is_full_board = x_moves + o_moves == 9
    x_wins = len([c for c in win_combos if c.count("X") == 3])
    o_wins = len([c for c in win_combos if c.count("O") == 3])

    print(x_wins)
    print(o_wins)
    print(win_combos)

    if x_wins and o_wins or max(x_moves, o_moves) - min(x_moves, o_moves) >= 2:
        print(game_states.get(4))
    elif not x_wins and not o_wins and is_full_board:
        print(game_states.get(1))
    elif x_wins:
        print(game_states.get(2))
    elif o_wins:
        print(game_states.get(3))
    else:
        print(game_states.get(0))
        make_move()


# used to change marker on players turn
def marker_switch(grid):
    marker = ""
    play = ""

    for item in grid:
        for character in item:
            play += character

    x_moves = play.count("X")
    o_moves = play.count("O")

    if x_moves == 0:
        marker = "X"
    elif x_moves <= o_moves:
        marker = "X"
    else:
        marker = "O"

    return marker


# Sets up initital empty grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

valid = ["1", "2", "3"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

coordinates_states = {
    0: "You should enter numbers!",
    1: "Coordinates should be from 1 to 3!",
    2: "This cell is occupied! Choose another one!"
}

game_states = {
    0: "Game not finished",
    1: "Draw",
    2: "X wins",
    3: "O wins",
    4: "Impossible",
}

win_combos = [[grid[0][0], grid[0][1], grid[0][2]],
              [grid[1][0], grid[1][1], grid[1][2]],
              [grid[2][0], grid[2][1], grid[2][2]],
              [grid[0][0], grid[1][0], grid[2][0]],
              [grid[0][1], grid[1][1], grid[2][1]],
              [grid[0][2], grid[1][2], grid[2][2]],
              [grid[0][0], grid[1][1], grid[2][2]],
              [grid[2][0], grid[1][1], grid[0][2]]]


# This part of the script actually lets the game run
print_board()
make_move()
