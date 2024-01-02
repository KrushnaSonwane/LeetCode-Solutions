class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res, hashT = [], Counter(nums)
        change = True
        while change:
            change, A = False, []
            for num in hashT:
                if hashT[num]:
                    A.append(num)
                    change, hashT[num] = True, hashT[num]-1
            if change:
                res.append(A)
        return res