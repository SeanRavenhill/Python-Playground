init_cells = "X_X_O____"

cell = ["X" if c == "X" else "O" if c == "O" else " " for c in init_cells]

print(cell)

grid = [
    [cell[0], cell[1], cell[2]],
    [cell[3], cell[4], cell[5]],
    [cell[6], cell[7], cell[8]]
]

render_grid = ("---------\n"
               "| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |\n"
               "| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |\n"
               "| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |\n"
               "---------")

print(render_grid)

coordinates_states = {
    0: "This cell is occupied! Choose another one!",
    1: "You should enter numbers!",
    2: "Coordinates should be from 1 to 3!"
}

player_input = input("Enter the coordinates: ").split()
valid_coordinates = ["1", "2", "3"]
invalid_coordinates = ["0", "4", "5", "6", "7", "8", "9"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

not_numbers = False
not_coordinates = False
coordinates = []

for i in player_input:
    if i not in numbers:
        not_numbers = True
    elif i in invalid_coordinates:
        not_coordinates = True
    else:
        coordinates.append(int(i) - 1)


print(not_numbers)
print(not_coordinates)
print()
print(coordinates)
print(type(coordinates))
print()

cell_occupied = False

while len(coordinates) != 2:
    break
else:
    cell_occupied = grid[coordinates[0]][coordinates[1]] != " "

print(cell_occupied)

if cell_occupied is True:
    print()

'''
print(not_numbers)
print(not_coordinates)
print()
print(coordinates)
print(type(coordinates))
print()
'''
'''
# print(cell_occupied)


# cell_occupied = grid[play_cell[0]][play_cell[1]] != " "
# not_numbers = play_cell[0:] != "0123456789"

# print(play_cell[0], "and", play_cell[1])
# print("testing", grid[play_cell[0]][play_cell[1]])
# print(cell_occupied)
# print(not_numbers)

# if cell_occupied:
# print(coordinates_states.get(0))

'''
'''
game_states = {
    0: "Game not finished",
    1: "Draw",
    2: "X wins",
    3: "O wins",
    4: "Impossible",
}

win_combos = [[play[0], play[1], play[2]],
              [play[3], play[4], play[5]],
              [play[6], play[7], play[8]],
              [play[0], play[3], play[6]],
              [play[1], play[4], play[7]],
              [play[2], play[5], play[8]],
              [play[0], play[4], play[8]],
              [play[2], play[4], play[6]]]

x_moves = play.count("X")
o_moves = play.count("O")
is_full_board = x_moves + o_moves == 9
x_wins = len([c for c in win_combos if c.count("X") == 3])
o_wins = len([c for c in win_combos if c.count("O") == 3])

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
'''
