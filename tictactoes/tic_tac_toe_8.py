init_cells = input()

cell = ["X" if c == "X" else "O" if c == "O" else " " for c in init_cells]

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

valid = ["1", "2", "3"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

coordinates_states = {
    0: "You should enter numbers!",
    1: "Coordinates should be from 1 to 3!",
    2: "This cell is occupied! Choose another one!"
}


def make_move():
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
        grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
        print(grid)
        print("---------")
        print("| " + grid[0][0] + " " + grid[0][1] + " " + grid[0][2] + " |")
        print("| " + grid[1][0] + " " + grid[1][1] + " " + grid[1][2] + " |")
        print("| " + grid[2][0] + " " + grid[2][1] + " " + grid[2][2] + " |")
        print("---------")


make_move()
