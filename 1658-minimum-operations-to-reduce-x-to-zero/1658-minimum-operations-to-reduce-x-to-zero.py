class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x: return -1
        hashT, sum_, res = defaultdict(int), 0, inf
        for i, num in enumerate(nums):
            sum_ += num
            if sum_ == x: res = i+1
            hashT[sum_] = i
        sum_, hashT[0] = 0, -1
        for i in range(len(nums)-1, -1, -1):
            sum_ += nums[i]
            remain = x - sum_
            if remain in hashT:
                res = min(res, len(nums)-i+hashT[remain] + 1)
        return -1 if res == inf else res