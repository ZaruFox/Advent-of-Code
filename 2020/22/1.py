from collections import deque
playersDeck = [deque(), deque()]

with open("data.txt") as f:
    playerNumber = -1
    for line in f:
        if line == "\n":
            continue
            
        if line.startswith("Player"):
            playerNumber = int(line[7])-1
            continue
            
        playersDeck[playerNumber].append(int(line.strip()))

while all(playersDeck):
    if playersDeck[0][0] > playersDeck[1][0]:
        winner = 0
        loser = 1
    else:
        winner = 1
        loser = 0
        
    playersDeck[winner].append(playersDeck[winner].popleft())
    playersDeck[winner].append(playersDeck[loser].popleft())

score = 0
winningDeck = list(playersDeck[winner])[::-1]
for i in range(len(winningDeck)):
    score += (i+1) * winningDeck[i]
print(score)