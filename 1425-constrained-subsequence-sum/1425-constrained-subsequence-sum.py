class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        res, Q = A[0], [[-A[0], 0]]
        for i in range(1, len(A)):
            while i - Q[0][1] > k:
                heappop(Q)
            res = max(res, -Q[0][0])
            heappush(Q, [-(max(0, -Q[0][0]) + A[i]), i])
        return max(res, -heappop(Q)[0])