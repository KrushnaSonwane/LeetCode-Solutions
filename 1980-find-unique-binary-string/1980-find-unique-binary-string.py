class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.res = ''
        def dfs(i, num):
            if self.res: return
            if i == len(nums):
                if num not in nums: 
                    self.res = num
                return 
            dfs(i+1, num + '0')
            dfs(i+1, num + '1')
        dfs(0, '')
        return self.res