import bisect 
class Solution(object):
    def maxEnvelopes(self, nums):
        nums.sort(key=lambda x: (x[0], -x[1]))
        res, last = [], 0
        for a, b in nums:
            if a != last:
                if not res or res[-1] < b:
                    res.append(b)
                else:
                    ind = bisect.bisect_left(res, b)
                    res[ind] = b
            else:
                ind = bisect.bisect_left(res, b)
                res[ind] = b
            last = a
        return  len(res)