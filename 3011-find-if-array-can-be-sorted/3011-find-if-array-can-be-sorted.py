class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def getCount(num):
            if num == 1: return 1
            if num % 2:
                return 1 + getCount(num // 2)
            return getCount(num // 2)
        A = []
        last = -inf
        temp = []
        for num in nums:
            count = getCount(num)
            if count == last:
                temp.append(num)
            else:
                last = count
                A.append(sorted(temp))
                temp = [num]
        A.append(sorted(temp))
        B = []
        for a in A:
            for num in a:
                B.append(num)
        return B == sorted(B)