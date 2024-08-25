class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class CyclicalLinkedList:
    def __init__(self, arr):
        self.curCup = Node(arr[0])
        self.maxValue = 0
        self.hashmap = {arr[0]: self.curCup}

        cur = self.curCup
        for val in arr[1:]:
            self.maxValue = max(self.maxValue, val)
            cur.next = Node(val)
            cur = cur.next
            self.hashmap[val] = cur
            
        cur.next = self.curCup

    def move(self):
        cupsPickedUp = self.curCup.next
        self.curCup.next = cupsPickedUp.next.next.next

        values = []
        cur = cupsPickedUp
        while cur != self.curCup.next:
            values.append(cur.val)
            cur = cur.next

        destinationCup = (self.curCup.val-2) % self.maxValue + 1
        while destinationCup in values:
            destinationCup = (destinationCup-2) % self.maxValue + 1
        
        tmp = self.hashmap[destinationCup].next
        self.hashmap[destinationCup].next = cupsPickedUp
        cupsPickedUp.next.next.next = tmp


        self.curCup = self.curCup.next

    def getResult(self):
        cur = self.curCup
        while True:
            if cur.val == 1:
                return cur.next.val * cur.next.next.val
            cur = cur.next

    def printCups(self):
        print(self.curCup.val, end=",")
        cur = self.curCup.next
        while cur != self.curCup:
            print(cur.val, end=",")
            cur = cur.next
        print("")

with open("data.txt") as f:
    cups = [int(x) for x in f.readline().strip()]

cups += list(range(10,1000001))
cups = CyclicalLinkedList(cups)

for i in range(10_000_000):
    if i % 100000 == 0:
        print(f"{i//100000}% done")
    cups.move()

print(cups.getResult())