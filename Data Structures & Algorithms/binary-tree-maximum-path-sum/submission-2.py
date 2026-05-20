# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def travel(root):
            if not root:
                return 0
            l = travel(root.left)
            if l < 0: l = 0
            r = travel(root.right)
            if r < 0: r = 0
            if l + r + root.val > self.m:
                self.m = l + r + root.val
            return max(l, r, 0) + root.val
        self.m = -math.inf
        return max(travel(root), self.m)