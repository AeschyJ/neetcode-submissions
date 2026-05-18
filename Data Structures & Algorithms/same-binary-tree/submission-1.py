# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            b = True
            if (p and q) and p.val == q.val:
                if (p.left and q.left) or (not p.left and not q.left):
                    b = isSame(p.left, q.left)
                    if not b:
                        return False
                else:
                    return False
                if (p.right and q.right) or (not p.right and not q.right):
                    b = isSame(p.right, q.right)
                    if not b:
                        return False
                else:
                    return False
            elif not p and not q:
                return True
            else:
                return False
            return True
        return isSame(p, q)