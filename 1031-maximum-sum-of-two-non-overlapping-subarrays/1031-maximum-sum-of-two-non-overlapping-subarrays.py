class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], aa: int, bb: int) -> int:
        def solve(a, b):
            res, sum1, sum2 = 0, 0, 0
            sum1 = sum(A[:a-1])
            for i in range(a-1, len(A)):
                sum1 += A[i]
                sum2 = sum(A[i+1:i+b])
                for j in range(i+b, len(A)):
                    sum2+=A[j]
                    res=max(res,sum1+sum2)
                    sum2-=A[j-b+1]
                sum1 -= A[i-a+1]
            return res
        return max(solve(aa, bb),solve(bb,aa))