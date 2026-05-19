# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.a = 0
        def travel(root, maxnode):
            if root:
                if maxnode <= root.val:
                    self.a += 1
                    maxnode = root.val
                travel(root.left, maxnode)
                travel(root.right, maxnode)
        travel(root, -math.inf)
        return self.a