from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        A, res = SortedList(), inf
        for i in range(x, len(nums)):
            A.add(nums[i-x])
            ind = bisect.bisect(A, nums[i])
            if ind-1 < len(A):
                res = min(res, abs(A[ind-1]-nums[i]))
            if ind+1<len(A):
                res = min(res, abs(A[ind+1]-nums[i]))
            if ind < len(A):
                res = min(res, abs(A[ind]-nums[i]))
        return res