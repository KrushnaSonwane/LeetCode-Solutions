class Solution:
    def isDecomposable(self, s: str) -> bool:
        last, count = s[0], 1
        res  = 0
        for num in s[1:]:
            if num == last:
                count += 1
            else:
                if count == 1: return False
                if count % 3 == 2:
                    res += 1
                elif count % 3 == 1: return False
                last, count = num, 1
        if count == 1: return False
        if count % 3 == 2:
            res += 1
        elif count % 3 == 1: return False
        return res == 1