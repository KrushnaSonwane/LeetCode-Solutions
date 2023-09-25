class Solution:
    def maximumSumOfHeights(self, H: List[int]) -> int:
        def getPrefix(A):
            res, stack = [], []
            for i, num in enumerate(A):
                while stack and A[stack[-1]] > num:
                    stack.pop()
                if not stack:
                    res.append(num*(i+1))
                else:
                    res.append(res[stack[-1]] + num * (i - stack[-1]))
                stack.append(i)
            return res
        res = 0
        for i, (a, b) in enumerate(zip(getPrefix(H), getPrefix(H[::-1])[::-1])):
            res = max(res, a + b - H[i])
        return res