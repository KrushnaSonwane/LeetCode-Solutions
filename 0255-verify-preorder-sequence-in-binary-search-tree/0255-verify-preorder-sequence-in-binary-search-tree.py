class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        max_, A = -inf, [preorder[0]]
        for num in preorder[1:]:
            while A and A[-1] < num:
                max_ = max(max_, A.pop())
            if num < max_: return False
            A.append(num)
        return True