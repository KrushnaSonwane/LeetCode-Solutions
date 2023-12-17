class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        
        def check(a, A, i, j):
            min_ = A[a] - A[i-1]
            max_ = A[j] - A[a]
            left = a - i + 1
            right = j - a
            return abs(min_ - nums[a] * left) + abs(max_ - nums[a]*right)
            
        def isValid(key, n, A):
            a, b = key // 2, key // 2 - 1 if key % 2 == 0 else key // 2
            i = 0
            for j in range(key-1, n):
                for sum_ in [check(a, A, i, j), check(b, A, i, j)]:
                    if sum_ <= k: 
                        return 1
                a, b, i = a + 1, b + 1, i + 1
            return 0
        
        A, n = [0], len(nums)
        nums.sort()
        for num in nums:
            A.append(A[-1]+num)
        A.pop(0)
        A.append(0)
        l, r, res = 1, n+1, 1
        while r >= l:
            mid = (r + l) // 2
            if isValid(mid, n, A):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res