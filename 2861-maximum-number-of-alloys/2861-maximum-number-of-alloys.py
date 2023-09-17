class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, C: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0
        def isValid(A, m):
            ans = 0
            for i, num in enumerate(A):
                if stock[i] >= m * num:
                    continue
                else:
                    ans += (m * num - stock[i]) * cost[i]
            return budget >= ans
            
        for A in C:
            l, r = 0, 10**9
            while r >= l:
                m = (r+l) // 2
                if isValid(A, m):
                    res = max(res, m)
                    l = m + 1
                else:
                    r = m - 1
        return res