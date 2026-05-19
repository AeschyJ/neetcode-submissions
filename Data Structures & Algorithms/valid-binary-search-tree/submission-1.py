# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def travel(root, nodemin, nodemax, l):
            if not root:
                return True
            if l is None:
                return travel(root.left, -math.inf, root.val, True) and travel(root.right, root.val, math.inf, False)
            if nodemin < root.val < nodemax:
                return travel(root.left, nodemin, root.val, True) and travel(root.right, root.val, nodemax, False)
            else: return False
        return travel(root, 0, 0, None)
        
        # if not root:
        #     return True
        # if root.left:
        #     if root.left.val >= root.val:
        #         return False
        # if root.right:
        #     if root.right.val <= root.val:
        #         return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)  