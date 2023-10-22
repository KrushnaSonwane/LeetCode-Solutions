class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        Q, min_, res = [], nums[0], inf
        for i, val in enumerate(nums):
            heappush(Q, [val, i])
        for i in range(1, len(nums)-1):
            while Q[0][-1] <= i:
                heappop(Q)
            if min_ < nums[i] > Q[0][0]:
                res = min(res, min_+nums[i]+Q[0][0])
            min_ = min(nums[i], min_)
        return -1 if res == inf else res