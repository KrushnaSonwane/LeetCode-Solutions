# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # if k == 0: return
        hashT = {root: None}
        queue = [root]
        valNode = None
        while queue:
            node = queue.pop(0)
            if node.left:
                hashT[node.left] = node
                queue.append(node.left)
            if node.right:
                hashT[node.right] = node
                queue.append(node.right)
        queue = [target]
        taken = set()
        taken.add(target)
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if k == 0: res.append(node.val)
                if hashT[node] and hashT[node] not in taken:
                    taken.add(hashT[node])
                    queue.append(hashT[node])
                if node.left and node.left not in taken:
                    taken.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in taken:
                    taken.add(node.right)
                    queue.append(node.right)
            k -= 1
        return res