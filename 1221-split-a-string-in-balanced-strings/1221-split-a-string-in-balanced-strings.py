class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, res= 0, 0
        for ch in s:
            count += 1 if ch == 'L' else -1
            res += count == 0
        return res