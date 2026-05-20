# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.p = 0
        
        def travel(l, r):
            if l > r:
                return None
            
            val = preorder[self.p]
            root = TreeNode(val)
            self.p += 1
            
            mid = inorder_map[val]
            
            root.left = travel(l, mid - 1)
            root.right = travel(mid + 1, r)
            
            return root
            
        return travel(0, len(inorder) - 1)