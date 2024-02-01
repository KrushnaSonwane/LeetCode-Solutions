class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1: return ["0","1","8"]
        res = []
        def dfs(i, j, nums):
            if j < i:
                res.append(''.join(nums))
                return
            A = [num for num in nums]
            if i < j:
                for a, b in [["0","0"], ["8","8"], ["1","1"], ["6", "9"], ["9", "6"]]:
                    if a == '0' and i == 0: continue
                    A[i], A[j] = a, b
                    dfs(i+1, j-1, A.copy())
            else:
                for a in ["0", "1", "8"]:
                    A[i] = a
                    dfs(i+1, j-1, A.copy())
        dfs(0, n-1, ['' for _ in range(n)])
        return res