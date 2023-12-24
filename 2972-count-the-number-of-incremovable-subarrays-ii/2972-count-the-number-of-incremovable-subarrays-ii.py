class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        last = -inf
        A = []
        for num in nums:
            if last < num:
                A.append(num)
            else:
                break
            last = num
        last = inf
        B = []
        for num in nums[::-1]:
            if last > num:
                B.append(num)
            else:
                break
            last = num
        n = len(nums)
        if nums == sorted(set(nums)):
            return n * (n+1) // 2
        B = B[::-1]
        res = 0
        for num in A:
            i = bisect_right(B, num)
            res += (len(B) - i) + 1
        return res + 1  + len(B)