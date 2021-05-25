play = "_OOOO_X_X"

print("---------")
print("| " + play[0] + " " + play[1] + " " + play[2] + " |")
print("| " + play[3] + " " + play[4] + " " + play[5] + " |")
print("| " + play[6] + " " + play[7] + " " + play[8] + " |")
print("---------")

plays = [x for x in play]

if play[0] == play[1] and play[1] == play[2]:  # Vert Top check
    if play[3] == play[4] and play[4] == play[5]:  # Vert Mid cross check
        print("Impossible")
    elif play[6] == play[7] and play[7] == play[8]:  # Vert Low cross check
        print("Impossible")
    else:
        print(play[0], "wins")
elif play[3] == play[4] and play[4] == play[5]:  # Vert Mid check
    if play[0] == play[1] and play[1] == play[2]:  # Vert Top cross check
        print("Impossible")
    elif play[6] == play[7] and play[7] == play[8]:  # Vert Low cross check
        print("Impossible")
    else:
        print(play[3], "wins")
elif play[6] == play[7] and play[7] == play[8]:  # Vert Low check
    if play[0] == play[1] and play[1] == play[2]:  # Vert Top cross check
        print("Impossible")
    if play[3] == play[4] and play[4] == play[5]:  # Vert Mid cross check
        print("Impossible")
    else:
        print(play[6], "wins")
elif play[0] == play[3] and play[3] == play[6]:  # Hori Left check
    if play[1] == play[4] and play[4] == play[7]:  # Hori Mid cross check
        print("Impossible")
    elif play[2] == play[5] and play[5] == play[8]:  # Hori Right cross check
        print("Impossible")
    else:
        print(play[0], "wins")
elif play[1] == play[4] and play[4] == play[7]:  # Hori Mid check
    if play[0] == play[3] and play[3] == play[6]:  # Hori Left cross check
        print("Impossible")
    elif play[2] == play[5] and play[5] == play[8]:  # Hori Right cross check
        print("Impossible")
    else:
        print(play[1], "wins")
elif play[2] == play[5] and play[5] == play[8]:  # Hori Right check
    if play[0] == play[3] and play[3] == play[6]:  # Hori Left cross check
        print("Impossible")
    elif play[1] == play[4] and play[4] == play[7]:  # Hori Mid cross check
        print("Impossible")
    else:
        print(play[2], "wins")
elif play[0] == play[4] and play[4] == play[8]:  # Diag Down Left Right Check
    print(play[0], "wins")
elif play[6] == play[4] and play[4] == play[2]:  # Diag Up Left Right Check
    print(play[6], "wins")
elif abs(plays.count("X") - plays.count("O")) >= 2:
    print("Impossible")
elif "_" in plays[0:7] or " " in plays[0:7]:
    print("Game not finished")
else:
    print("Draw")
