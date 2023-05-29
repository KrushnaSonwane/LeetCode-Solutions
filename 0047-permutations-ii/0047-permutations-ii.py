class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(currArray, hashT):
            if len(currArray) == len(nums):
                res.append(currArray.copy())
                return
            for num in hashT:
                if hashT[num] > 0:
                    hashT[num] -= 1
                    currArray.append(num)
                    dfs(currArray, hashT)
                    currArray.pop()
                    hashT[num] += 1
        dfs([], Counter(nums))
        return res