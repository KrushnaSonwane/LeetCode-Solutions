class Solution:
    def findBall(self, A: List[List[int]]) -> List[int]:
        m, n = len(A), len(A[0])
        res = [-1] * n
        for i in range(n):
            ans = i
            for j in range(m):
                if A[j][ans] == -1:
                    if ans-1 >= 0 and A[j][ans] == -1: ans -= 1
                    else: break
                if A[j][ans] == 1:
                    if ans+1 < n and A[j][ans+1] == 1: ans += 1
                    else: break
            else: res[i] = ans
        return res