class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res, Q, n = [], [], len(nums)

        def solve(Q):
            B = []
            for _ in range(len(Q)):
                j, A = heappop(Q)
                res.append(A.pop(0))
                if A: heappush(B, [j, A])
            return B

        for i in range(n):
            heappush(Q, [-i-n, nums[i]])
            Q = solve(Q)
            
        while Q:
            Q = solve(Q)
        return res