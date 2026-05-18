# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            if root.val != sub.val:
                return False
            return isSame(root.left, sub.left) and isSame(root.right, sub.right)
        def travel(root, sub):
            if not root:
                return False
            return isSame(root, sub) or travel(root.left, sub) or travel(root.right, sub)
        return travel(root, subRoot)