# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.root = None
        self.i = 0
        self.l = len(preorder)
        def travel(p, q, root):
            if self.i == self.l: return
            if p:
                if not self.root:
                    self.root = TreeNode(p[0])
                    self.i += 1
                    root = self.root
                print(p[0], q.index(p[0]))
                if q.index(p[0]) > 0:
                    root.left = TreeNode(p[1])
                    self.i += 1
                    travel(p[1:q.index(p[0])+1], q[0:q.index(p[0])], root.left)
                if q.index(p[0]) < len(p) - 1:
                    root.right = TreeNode(p[q.index(p[0])+1])
                    self.i += 1
                    travel(p[q.index(p[0])+1:], q[q.index(p[0])+1:], root.right)
            return
        travel(preorder, inorder, None)
        return self.root