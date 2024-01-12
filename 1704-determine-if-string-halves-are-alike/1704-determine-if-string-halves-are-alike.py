class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n, res  = len(s), 0
        for i, ch in enumerate(s):
            if ch.lower() in 'aeiou':
                if i >= n // 2:
                    res -= 1
                else:
                    res += 1
        return res == 0