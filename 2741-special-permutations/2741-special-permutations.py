class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        hashT, MOD = {num: i for i, num in enumerate(nums)}, 10**9+7

        @lru_cache(None)
        def dfs(i, last, mask):
            if i == len(nums):
                return 1
            res = 0
            for num in nums:
                if mask[hashT[num]] == '0' and 0 in [last%num, num%last]:
                    A = [ch for ch in mask]
                    A[hashT[num]] = '1'
                    res += dfs(i+1, num, ''.join(A))
            res %= MOD
            return res

        res = 0
        mask = ['0' for _ in nums]
        for num in nums:
            mask[hashT[num]] = '1'
            res += dfs(1, num, ''.join(mask))
            res %= MOD
            mask[hashT[num]] = '0'
        return res