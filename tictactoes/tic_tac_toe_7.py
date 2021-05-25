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

cell_occupied = False

while len(coordinates) != 2:
    break
else:
    cell_occupied = grid[coordinates[0]][coordinates[1]] != " "

while cell_occupied is True:
    print(coordinates_states.get(0))
    player_input = input("Enter the coordinates: ").split()
    if cell_occupied is False:
        print(render_grid)
        break

print()
print("not_numbers is:", not_numbers)
print("not_coordinates is:", not_coordinates)
print()
print("coordinates are:", coordinates)
print(type(coordinates))
print()
print("Is the cell occupied:", cell_occupied)
