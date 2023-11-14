class Solution:
    def minOperations(self, A: List[int], B: List[int]) -> int:
        def solve(A, B):
            res = 0
            for a, b in zip(A, B):
                if A[-1] >= a and B[-1] >= b: 
                    continue
                elif A[-1] >= b and B[-1] >= a:
                    res += 1
                else:
                    return inf
            return res
        res = solve(A, B)
        A[-1], B[-1] = B[-1], A[-1]
        res = min(res, solve(A, B) + 1)
        if res == inf: return -1
        return res