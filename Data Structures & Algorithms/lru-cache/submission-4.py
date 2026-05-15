
class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.map = {}
        self.head = Node(None)
        self.tail = Node(None, prev = self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.map:
            self.movetohead(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.movetohead(self.map[key])
            self.map[key].val = value
        else:
            if len(self.map) == self.c:
                p = self.map.pop(self.tail.prev.key)
                # print('pop',p.key)
                self.tail.prev, self.tail.prev.next = self.tail.prev.prev, self.tail
            self.map[key] = Node(key, value)
            self.movetohead(self.map[key])

    def movetohead(self, node):
        if node.next:
            node.next.prev, node.prev.next = node.prev, node.next
        node.next, node.prev = self.head.next, self.head
        self.head.next, node.next.prev = node, node
        # print("head", self.head.key, self.head.next.key, self.head.next.next.key)
