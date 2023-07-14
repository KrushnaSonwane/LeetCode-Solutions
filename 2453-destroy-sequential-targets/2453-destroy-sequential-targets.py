class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        hashT = defaultdict(list)
        max_, res = 0, inf
        for num in nums:
            hashT[num % space].append(num)
            max_ = max(max_, len(hashT[num%space]))
        for key in hashT:
            if len(hashT[key]) == max_: res = min(res, hashT[key][0])
        return res