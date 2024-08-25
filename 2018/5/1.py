class Node:
    def __init__(self, val, next = None, prev = None) -> None:
        self.next = next
        self.prev = prev
        self.val = val

class LinkedList:
    def __init__(self, lst) -> None:
        self.root = Node(None)
        self.length = len(lst)

        cur = self.root
        for i in range(len(lst)):
            cur.next = Node(lst[i], prev=cur)
            cur = cur.next
        
    def react(self):
        cur = self.root.next

        while cur.next:
            if cur.val and cur.val.lower() == cur.next.val.lower() and cur.val != cur.next.val:
                cur = cur.prev
                cur.next = cur.next.next.next
                cur.next.prev = cur
                self.length -= 2
            else:
                cur = cur.next


with open("data.txt") as f:
    polymer = LinkedList(f.readline().strip())

polymer.react()
print(polymer.length)