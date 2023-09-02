class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        hashT, res, sum_ = defaultdict(int), 0, 0
        for i in range(len(nums)):
            sum_ += nums[i]
            hashT[nums[i]] += 1
            if i + 1 >= k:
                if len(hashT) >= m:
                    res = max(res, sum_)
                hashT[nums[i-k+1]] -= 1
                if hashT[nums[i-k+1]] == 0: del hashT[nums[i-k+1]]
                sum_ -= nums[i-k+1]
        return res