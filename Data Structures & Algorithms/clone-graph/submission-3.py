"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        a = Node(node.val)
        d = {a.val: (a, set())}
        def travel(curr):
            if curr.val not in d:
                t = Node(curr.val)
                d[t.val] = (t, set())
                for n in curr.neighbors:
                    if n.val in d and n.val not in d[t.val][1]:
                        d[n.val][0].neighbors.append(t)
                        d[n.val][1].add(t.val)
                        t.neighbors.append(d[n.val][0])
                        d[t.val][1].add(n.val)
                    else:
                        travel(n)
                print(t.val, [x.val for x in t.neighbors])
        for n in node.neighbors:
            travel(n)
        print(a.val, [x.val for x in a.neighbors])
        return a