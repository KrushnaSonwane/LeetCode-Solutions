class Solution:
    def findLongestChain(self, A: List[List[int]]) -> int:
        A.sort()
        res, last = 0, -1001
        for l, r in A:
            if l > last:
                last = r
                res += 1
            else:
                last = min(last, r)
        return res