# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.res = []
        def dfs(root):
            if not root: return 
            if len(self.res) < k:
                heappush(self.res, (-abs(float(root.val)-target), -root.val))
            else:
                a, b = abs(float(root.val)-target), root.val
                x, y = heappop(self.res)
                y = -y
                x = -x
                if a < x:
                    heappush(self.res, (-a, -b))
                elif a == x:
                    heappush(self.res, (-x, -min(y, b)))
                else:
                    heappush(self.res, (-x, -y))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return [abs(y) for _, y in self.res]