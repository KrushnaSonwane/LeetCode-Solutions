class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0: pos.append(num)
            else: neg.append(num)
        ptr = 0
        i = 0
        while ptr < len(nums) // 2:
            nums[i] = pos[ptr]
            nums[i + 1] = neg[ptr]
            i += 2
            ptr += 1
        return nums