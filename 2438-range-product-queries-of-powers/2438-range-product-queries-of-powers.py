class Solution(object):
    def productQueries(self, n, q):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        curr = 1
        P = []
        while curr * 2 <= 10**10:
            P.append(curr)
            curr *= 2
        num = n
        A = []
        while num:
            while P[-1] > num:
                P.pop()
            while num >= P[-1]:
                A.append(P[-1])
                num -= P[-1]
        A = A[::-1]
        mod = 10**9+7
        res = []
        for l, r in q:
            ans = 1
            for i in range(l, r+1):
                ans *= A[i]
            res.append(ans%mod)
        return res