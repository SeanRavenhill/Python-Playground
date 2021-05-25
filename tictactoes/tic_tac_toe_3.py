cells = input("Enter cells: ")

c = list(cells)

print("---------")
print(f"| {c[0]} {c[1]} {c[2]} |")
print(f"| {c[3]} {c[4]} {c[5]} |")
print(f"| {c[6]} {c[7]} {c[8]} |")
print("---------")

line1 = [c[0], c[1], c[2]]
line2 = [c[3], c[4], c[5]]
line3 = [c[6], c[7], c[8]]
st1 = [c[0], c[3], c[6]]
st2 = [c[1], c[4], c[7]]
st3 = [c[2], c[5], c[8]]
d1 = [c[0], c[4], c[8]]
d2 = [c[6], c[4], c[2]]
grid = [line1, line2, line3, st1, st2, st3, d1, d2]

if ['X', 'X', 'X'] in grid:
    if ['O', 'O', 'O'] in grid:
        print('Impossible')
    else:
        print('X wins')
elif ['O', 'O', 'O'] in grid:
    print('O wins')
elif (c.count('X') - c.count('O')) not in (0, 1):
    print('Impossible')
elif "_" in c:
    print('Game not finished')
else:
    print("Draw")
