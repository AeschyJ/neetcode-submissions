"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {node: Node(node.val)}
        
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            for nei in curr.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    queue.append(nei)
                
                cloned[curr].neighbors.append(cloned[nei])
                
        return cloned[node]