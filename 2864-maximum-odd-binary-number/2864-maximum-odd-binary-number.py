class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')
        ans = [0 for _ in s]
        for i in range(count-1):
            ans[i] = 1
        ans[-1] = 1
        return ''.join(str(ch) for ch in ans)
            