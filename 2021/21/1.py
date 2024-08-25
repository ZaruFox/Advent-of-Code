pos1 = 7
pos2 = 0
score1 = 0
score2 = 0
dice = 0
player1Turn = True

while score1 < 1000 and score2 < 1000:
    if player1Turn:
        pos1 = (pos1 + ((dice % 100) + 1) * 3 + 3) % 10
        score1 += pos1 + 1
    else:
        pos2 = (pos2 + ((dice % 100) + 1) * 3 + 3) % 10
        score2 += pos2 + 1

    player1Turn = not player1Turn
    dice += 3

print(dice * min(score1, score2))