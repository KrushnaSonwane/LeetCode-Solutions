class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def dfs(i, A):
            if ''.join(A) not in nums: return 1, A
            if i == len(A): return 0, []
            A[i] = '1'
            f, ans = dfs(i+1, A)
            if f: return f, ans
            A[i]='0'
            return dfs(i+1, A)
        return ''.join(dfs(0, ['0' for _ in nums])[1])