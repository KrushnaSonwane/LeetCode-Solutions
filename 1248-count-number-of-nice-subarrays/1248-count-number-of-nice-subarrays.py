class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashT = defaultdict(int)
        hashT[0], count, res = 1, 0, 0
        for num in nums:
            if num % 2:
                count += 1
            res += hashT[k-count]
            hashT[-count] += 1
        return res