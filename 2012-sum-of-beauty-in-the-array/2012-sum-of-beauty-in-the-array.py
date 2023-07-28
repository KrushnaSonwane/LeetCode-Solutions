class Solution:
    def sumOfBeauties(self, A: List[int]) -> int:
        Q, res, max_ = [], 0, A[0]
        for i, a in enumerate(A):
            heappush(Q, [a, i])
        for i in range(1, len(A)-1):
            while Q[0][1] <= i:
                heappop(Q)
            if max_ < A[i] < Q[0][0]: 
                res += 2
            elif A[i-1] < A[i] < A[i+1]: 
                res += 1
            max_=max(max_,A[i])
        return res