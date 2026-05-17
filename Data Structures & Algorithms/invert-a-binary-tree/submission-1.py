# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(root, d):
            l, r = 0, 0
            if root.left:
                l = depth(root.left, d + 1)
            if root.right:
                r = depth(root.right, d + 1)
            return max(l, r, d)

        def switch(root, d):
            if d == 1:
                return
            elif d == 2:
                root.left, root.right = root.right, root.left
                return
            else:
                if root.left: switch(root.left, d-1)
                if root.right: switch(root.right, d-1)
                root.left, root.right = root.right, root.left

        d = 1
        r = root
        # if r: print(depth(r, 1))
        if r: switch(root, depth(r, 1))
        return root