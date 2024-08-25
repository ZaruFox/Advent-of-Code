import math

class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.next = next
        self.prev = prev
        self.val = val

class LinkedList:
    def __init__(self, lst, removedLetter) -> None:
        self.root = Node(None)
        self.length = len(lst)

        cur = self.root
        for i in range(len(lst)):
            if lst[i].lower() == removedLetter:
                self.length -= 1
                continue

            cur.next = Node(lst[i], prev=cur)
            cur = cur.next
        
    def react(self):
        cur = self.root.next

        while cur.next:
            if cur.val and cur.val.lower() == cur.next.val.lower() and cur.val != cur.next.val:
                cur = cur.prev
                cur.next = cur.next.next.next
                self.length -= 2

                if not cur.next:
                    break
                cur.next.prev = cur
            else:
                cur = cur.next


with open("data.txt") as f:
    basePolymer = list(f.readline().strip())

res = math.inf
for removed in "abcdefghijklmnopqrstuvwxyz":
    newPolymer = LinkedList(basePolymer, removed)
    newPolymer.react()
    res = min(newPolymer.length, res)

print(res)