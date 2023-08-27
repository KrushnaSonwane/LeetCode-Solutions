class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if target > sum(nums): return -1
        key = []
        while target:
            key.append(target%2)
            target //= 2
        count = [0 for _ in range(33)]
        for num in nums:
            s = bin(num)[::-1]
            for i in range(len(s)):
                count[i] += s[i] == '1'
        res = 0
        for i, num in enumerate(key):
            if not num:
                count[i+1] += count[i]//2
                count[i] = 0
            elif count[i] >= 1:
                count[i] -= 1
                count[i+1] += count[i] // 2
            else:
                curr = i
                while count[curr] == 0:
                    curr += 1
                res += curr - i
                count[curr] -= 1
                for j in range(curr-1, i-1, -1):
                    count[j] += 1 
        return res