# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = []
        def travel(root, deep, a):
            if root:
                if len(a) < deep + 1:
                    a.append([])
                a[deep].append(root.val)
                travel(root.left, deep + 1, a)
                travel(root.right, deep + 1, a)
        travel(root, 0, a)
        return a
            
        