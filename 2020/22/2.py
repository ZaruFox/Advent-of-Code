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

def combat(playersDeck):
    prevRounds = set()
    winner = -1
    while all(playersDeck):
        gameState = (tuple(playersDeck[0]), tuple(playersDeck[1]))
        if gameState in prevRounds:
            return 0, playersDeck
        prevRounds.add(gameState)

        if playersDeck[0][0] < len(playersDeck[0]) and playersDeck[1][0] < len(playersDeck[1]):
            winner, _ = combat([deque(list(deck)[1:deck[0]+1]) for deck in playersDeck])
        elif playersDeck[0][0] > playersDeck[1][0]:
            winner = 0
        else:
            winner = 1
            
        loser = 0 if winner else 1
        playersDeck[winner].append(playersDeck[winner].popleft())
        playersDeck[winner].append(playersDeck[loser].popleft())

    return winner, playersDeck

score = 0
winner, playersDeck = combat(playersDeck)
winningDeck = list(playersDeck[winner])[::-1]
for i in range(len(winningDeck)):
    score += (i+1) * winningDeck[i]
print(score)