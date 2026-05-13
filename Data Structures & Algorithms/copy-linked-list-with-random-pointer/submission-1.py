"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        s = []
        i = 0
        a = head
        while head is not None:
            n = Node(head.val, head.next, None)
            s.append((n, head.random))
            if i != 0:
                s[i-1][0].next = n
            i += 1
            head = head.next
        if s:
            b = s[0][0]
        while a is not None:
            nl = [x for x in s if x[1] == a]
            if nl:
                for n in nl:
                    n[0].random = b
            a = a.next
            b = b.next
        if s:
            return s[0][0]
        return
        