# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        if root:
            res, Q = [], [root]
            res.append(str(root.val))
            while Q:
                curr = Q.pop(0)
                if curr.left:
                    res.append(str(curr.left.val))
                    Q.append(curr.left)
                else:
                    res.append('#')
                if curr.right:
                    res.append(str(curr.right.val))
                    Q.append(curr.right)
                else:
                    res.append('#')
            return ' '.join(res)
        
        return ''

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return 
        res = data.split(" ")
        if res:
            root = TreeNode(int(res.pop(0)))
            Q = [root]
            while res:
                val = res.pop(0)
                curr = Q.pop(0)
                if val != '#':
                    curr.left = TreeNode(int(val))
                    Q.append(curr.left)
                val = res.pop(0)
                if val != '#':
                    curr.right = TreeNode(int(val))
                    Q.append(curr.right)
            return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans