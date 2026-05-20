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
        self.d = 0
        def travel(root, d):
            if root:
                d += 1
                if self.d < d: self.d = d
                self.a.append(str(root.val))
            else:
                self.a.append("N")
                return
            travel(root.left, d + 1)
            travel(root.right, d + 1)
        travel(root, 0)
        # return f"{self.d}/"+"/".join(self.a)
        return "/".join(self.a)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("/")
        print(arr)
        self.root = None
        self.i = 0
        def travel(i):
            if arr[i] == "N":
                root = None
                self.i += 1
                return
            else:
                root = TreeNode(int(arr[i]))
                self.i += 1
                root.left = travel(self.i)
                root.right = travel(self.i)
                self.root = root
                return root
        travel(0)
        return self.root


