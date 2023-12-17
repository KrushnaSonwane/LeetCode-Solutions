class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n, res = len(nums), inf
        mid = n // 2
        if n%2:
            s = [mid]
        else:
            s = [mid-1, mid]
        C = []
        for i in s:
            num = [ch for ch in str(nums[i])]
            if len(num)%2:
                l = len(num)//2
                r = l
            else:
                l, r = len(num)//2-1, len(num)//2
            for j in range(10):
                num[l], num[r] = str(j), str(j)
                C.append(int(''.join(num[:l]+num[l:r+1]+num[:l][::-1])))
        B = [0]
        for num in nums:
            B.append(B[-1]+num)
        B.pop(0)
        for pal in C:
            l, r = 0, len(nums)-1
            got = 0
            while r >= l:
                mid = (r + l) // 2
                if nums[mid] > pal:
                    r = mid - 1
                else:
                    got = mid
                    l = mid + 1
            left = abs((pal*(got+1)) - B[got])
            size = len(nums) - (got+1)
            right = abs((B[-1]-B[got]) - (pal * size))
            res = min(res, left+right)
        return res