class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        A, i = Counter(nums), 0
        count = 0
        while i < len(nums):
            hashT = {nums[i]}
            while len(hashT) > 0:
                A[nums[i]] -= 1
                hashT.add(nums[i])
                if A[nums[i]] == 0:
                    hashT.discard(nums[i])
                i += 1
            count += 1
        res, MOD, sum_ = 0, 10**9+7, 0
        for i in range(count):
            res = (sum_ + 1) % MOD
            sum_ += res
        return res