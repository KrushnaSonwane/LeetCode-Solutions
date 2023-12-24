class Solution:
    def minOperations(self, s: str) -> int:
        def solve(last):
            res = 0
            for ch in s:
                if (last and ch == '1') or (not last and ch == '0'):
                    res += 1
                last = not last
            return res
        return min(solve(0), solve(1))