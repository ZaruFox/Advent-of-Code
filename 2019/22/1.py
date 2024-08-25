class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, length):
        self.root = Node(0, None)
        self.length = length

        cur = self.root
        for i in range(1, length):
            cur.next = Node(i, None)
            cur = cur.next

    def deal(self):
        cur = self.root.next
        prev = self.root
        self.root.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            cur, prev = tmp, cur

        self.root = prev

    def cut(self, n):
        cur = self.root

        if n > 0:
            cutIndex = n-1
        else:
            cutIndex = self.length+n-1

        for _ in range(cutIndex):
            cur = cur.next
        
        tmp = self.root
        self.root = cur.next
        cur.next = None

        cur = self.root
        while cur.next:
            cur = cur.next

        cur.next = tmp

    def increment(self, n):
        result = [None] * self.length
        
        cur = self.root
        for i in range(self.length):
            result[(i*n)%self.length] = cur.val
            cur = cur.next
        
        cur = self.root
        for value in result:
            assert value is not None
            cur.val = value
            cur = cur.next

    def getIndex(self, val):
        cur = self.root
        for i in range(self.length):
            if cur.val == val:
                return i
            cur = cur.next

        return -1

    def __str__(self):
        cur = self.root
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next

        return str(res)

stack = LinkedList(10007)
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        if line == "deal into new stack":
            stack.deal()
        elif line.startswith("cut "):
            stack.cut(int(line.lstrip("cut ")))
        elif line.startswith("deal with increment "):
            stack.increment(int(line.lstrip("deal with increment ")))
        else:
            raise Exception()

print(stack.getIndex(2019))