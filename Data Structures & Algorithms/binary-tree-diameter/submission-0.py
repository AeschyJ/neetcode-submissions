# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            l, r = 0, 0
            ldia, rdia = 0, 0
            if root.left:
                l, ldia = depth(root.left)
                l += 1
            if root.right:
                r, rdia = depth(root.right)
                r += 1
            dia = max(ldia, rdia, l + r)
            # print(root.val, ldia, rdia, dia)
            return max(l, r), dia
        d, dia = depth(root)
        # print(d, dia)
        return dia
        