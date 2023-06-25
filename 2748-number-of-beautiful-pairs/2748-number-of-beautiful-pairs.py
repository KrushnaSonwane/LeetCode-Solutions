import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                num = str(nums[i])
                num2 = str(nums[j])
                if math.gcd(int(num[0]), int(num2[-1])) == 1: res += 1
        return res