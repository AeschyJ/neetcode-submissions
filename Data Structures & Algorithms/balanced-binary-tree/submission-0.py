# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            l, r = 0, 0
            if root:
                if root.left:
                    l = depth(root.left)
                    if l is not False: l += 1
                if root.right:
                    r = depth(root.right)
                    if r is not False: r += 1
            if l is False or r is False:
                return False
            if abs(l - r) > 1:
                return False
            return max(l, r)
        a = depth(root)
        if type(a) is int:
            return True
        return False