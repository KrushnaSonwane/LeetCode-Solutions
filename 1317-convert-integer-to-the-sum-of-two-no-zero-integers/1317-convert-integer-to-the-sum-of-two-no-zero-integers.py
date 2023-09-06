class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l, r = 1, n-1
        while r > l:
            if '0' not in str(l) and '0' not in str(r): 
                break
            l += 1
            r -= 1
        return [l, r]