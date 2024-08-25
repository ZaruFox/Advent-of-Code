class Marble:
    def __init__(self, val, prev = None, next = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class MarbleGame:
    def __init__(self) -> None:
        self.cur = Marble(0)
        self.cur.next = self.cur
        self.cur.prev = self.cur

    def placeMarble(self, val):
        newMarble = Marble(val, self.cur.next, self.cur.next.next)
        self.cur.next.next.prev = newMarble
        self.cur.next.next = newMarble
        self.cur = newMarble

    def removeMarble(self):
        removed = self.cur
        for i in range(7):
            removed = removed.prev
        
        removed.next.prev = removed.prev
        removed.prev.next = removed.next
        self.cur = removed.next
        return removed.val
    

with open("data.txt") as f:
    data = f.readline().strip().split(" ")
    playerCount, marbleCount = int(data[0]), int(data[6])

playerScores = [0] * playerCount
marbleCount *= 100
game = MarbleGame()
for i in range(1, marbleCount+1):
    if i % 23 == 0:
        playerScores[(i-1) % playerCount] += i + game.removeMarble()
    else:
        game.placeMarble(i)

print(max(playerScores))