class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def dfs(i, currS):
            if ''.join(currS) not in nums: return 1, currS
            if i == len(currS): return 0, []
            currS[i] = '1'
            f, ans = dfs(i+1, currS)
            if f: return f, ans
            currS[i]='0'
            return dfs(i+1, currS)
        return ''.join(dfs(0, ['0' for _ in nums])[1])