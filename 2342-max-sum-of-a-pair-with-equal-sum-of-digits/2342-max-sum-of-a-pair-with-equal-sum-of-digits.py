from sortedcontainers import SortedList
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashT = defaultdict(SortedList)
        res = -1
        for num in nums:
            curr = num
            sum_ = 0
            while curr:
                sum_ += curr % 10
                curr //= 10
            hashT[sum_].add(num)
        for sum_ in hashT:
            if len(hashT[sum_]) > 1:
                res = max(res, hashT[sum_][-1] + hashT[sum_][-2])
        return res