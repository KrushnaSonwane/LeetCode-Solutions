class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[0] == 1:
                break
            else:
                if nums[i] == 1:
                    ptr = i
                    while ptr != 0:
                        nums[ptr - 1], nums[ptr] = nums[ptr], nums[ptr - 1]
                        ptr -= 1
                        res += 1
                    break
        for i in range(n):
            if nums[-1] == n: break
            else:
                if nums[i] == n:
                    ptr = i
                    while nums[-1] != n:
                        nums[ptr + 1], nums[ptr] = nums[ptr], nums[ptr + 1]
                        ptr += 1
                        res += 1
                    break
        return res