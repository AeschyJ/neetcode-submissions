# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.a = []
        def travel(root):
            if root:
                self.a.append(str(root.val))
            else:
                self.a.append("N")
                return
            travel(root.left)
            travel(root.right)
        travel(root)
        # return f"{self.d}/"+"/".join(self.a)
        return "/".join(self.a)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = iter(data.split("/"))
        def travel():
            c = next(arr)
            if c == "N":
                return
            else:
                root = TreeNode(int(c))
                root.left = travel()
                root.right = travel()
                return root
        return travel()


