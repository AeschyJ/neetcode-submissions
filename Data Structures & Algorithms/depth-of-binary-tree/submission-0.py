# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root, deep):
            l, r = 0, 0
            if root:
                deep += 1
                l = depth(root.left, deep)
                r = depth(root.right, deep)
            return max(deep, l, r)
        return depth(root, 0)