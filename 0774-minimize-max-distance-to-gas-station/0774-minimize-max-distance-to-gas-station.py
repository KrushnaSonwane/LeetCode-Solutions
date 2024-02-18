class Solution:
    def minmaxGasDist(self, S: List[int], k: int) -> float:

        def isValid(size):
            last, count = S[0], 0
            i = 1
            while i < len(S):
                count += int((S[i]-S[i-1]) // size) 
                i += 1
            return count <= k            


        l, r = 0, 10**8
        res = 0.0
        while r - l > 0.000001:
            mid = (r + l) / 2
            if isValid(mid):
                res = mid
                r = mid
            else:
                l = mid
        return res