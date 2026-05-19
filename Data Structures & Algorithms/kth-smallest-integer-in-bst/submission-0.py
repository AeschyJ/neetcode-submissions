# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def mergearr(root, a):
            if not root:
                return
            mergearr(root.left, a)
            a.append(root.val)
            mergearr(root.right, a)
        mergearr(root, a)
        return a[k-1]