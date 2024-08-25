import itertools
from collections import Counter

class Hand:
    def __init__(self, cards, bid):
        for x, y in (("A", "E"),
                     ("T", "A"), 
                     ("J", "B"), 
                     ("Q", "C"), 
                     ("K", "D")):
            cards = cards.replace(x, y)

        self.cards = cards
        self.bid = int(bid)
        self.counter = Counter(cards)

    def getType(self):
        hashmap = {-4:0, -2:1, -1:2, 0:3, 1:4, 2:5, 4:6}
        uniqueCards = len(self.counter.keys())
        return hashmap[max(self.counter.values())-uniqueCards]
        

hands = []
with open("data.txt") as f:
    for line in f:
        hands.append(Hand(*line.strip().split()))

handsByValue = [[] for i in range(7)]
for currentHand in hands:
    handsByValue[currentHand.getType()].append(currentHand)

for i in range(7):
    handsByValue[i].sort(key=lambda x:x.cards)

multiplier = 1
result = 0
for currentHand in itertools.chain(*handsByValue):
    result += currentHand.bid * multiplier
    multiplier += 1

print(result)
