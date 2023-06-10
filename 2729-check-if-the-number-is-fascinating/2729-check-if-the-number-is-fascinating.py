class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(n * 2) + str(n * 3)
        if len(n) != 9: return 0
        for num in '123456789':
            if num not in n: return 0
        return 1