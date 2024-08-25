import itertools
from collections import Counter, defaultdict

class Hand:
    def __init__(self, cards, bid):
        for x, y in (("A", "E"),
                     ("T", "A"), 
                     ("J", "0"), 
                     ("Q", "C"), 
                     ("K", "D")):
            cards = cards.replace(x, y)

        self.cards = cards
        self.bid = int(bid)
        self.counter = defaultdict(int)
        numberOfJokers = 0
        biggest = None

        for card in cards:
            if card == "0":
                numberOfJokers += 1
                continue

            self.counter[card] += 1
            if biggest == None or self.counter[card] > self.counter[biggest]:
                biggest = card

        self.counter[biggest] += numberOfJokers

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
