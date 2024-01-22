class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashT = Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in hashT:
                a = i
        for num in hashT:
            if hashT[num] == 2:
                b = num
        return [b, a]