class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums: return []
        first = last = int(nums[0])
        for num in nums:
            num = int(num)
            if num - last <= 1:
                last = num
            else:
                res.append(str(first) if last == first else str(first) + '->' + str(last))
                first = last = num
        res.append(str(first) if last == first else str(first) + '->' + str(last))
        return res