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
        d = {}
        def travel(n):
            if n in d:
                return d[n]
            copy = Node(n.val)
            d[n] = copy

            for nei in n.neighbors:
                if nei in d:
                    copy.neighbors.append(d[nei])
                else:
                    copy.neighbors.append(travel(nei))
            return copy
        return travel(node)