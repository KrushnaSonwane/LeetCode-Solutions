class Solution:
    def isGood(self, nums: List[int]) -> bool:
        hashT = collections.Counter(nums)
        if len(set(nums)) != len(nums)-1: return 0
        for i in range(1, len(nums)):
            if i not in hashT: return 0
            if i == len(nums)-1:
                if hashT[i]!=2: return 0
            else:
                if hashT[i] != 1: return 0
        return 1