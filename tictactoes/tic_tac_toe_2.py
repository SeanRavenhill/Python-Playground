play = "_OOOO_X_X"

print("---------")
print("| " + play[0] + " " + play[1] + " " + play[2] + " |")
print("| " + play[3] + " " + play[4] + " " + play[5] + " |")
print("| " + play[6] + " " + play[7] + " " + play[8] + " |")
print("---------")

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
