class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        hashT = Counter(nums)
        for num in range(min(hashT.values()), -1, -1):
            res = 0
            for count in hashT.values():
                mod = count // (num + 1)
                rem = count % (num + 1)
                if rem == 0: res += mod
                elif mod >= num - rem:
                    res += 1 + mod
                elif count % num == 0: 
                    res += count // num
                else: break
            else: 
                return res
        return -1