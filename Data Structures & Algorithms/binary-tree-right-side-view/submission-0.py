# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        def travel(root, deep):
            if root:
                if len(a) < deep + 1:
                    a.append(root.val)
                travel(root.right, deep + 1)
                travel(root.left, deep + 1)
        travel(root, 0)
        return a
        