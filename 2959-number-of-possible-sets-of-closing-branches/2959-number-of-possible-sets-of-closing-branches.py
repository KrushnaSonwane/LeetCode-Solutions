class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        A = [[inf for _ in range(n)] for _ in range(n)]
        B = [0 for _ in range(n)]

        for i in range(n):
            A[i][i] = 0

        for a, b, w in roads:
            A[a][b] = min(A[a][b], w)
            A[b][a] = min(A[b][a], w)
        allList = []

        def solve(currLi):
            grid = [[inf for _ in range(n)] for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    grid[i][j] = A[i][j]

            for i in range(n):
                if currLi[i]:
                    for j in range(n):
                        if currLi[j]:
                            for k in range(n):
                                if currLi[k]:
                                    grid[j][k] = min(grid[j][k], grid[j][i] + grid[i][k])

            for i in range(n):
                if currLi[i]:
                    for j in range(n):
                        if currLi[j]:
                            if grid[i][j] > maxDistance: 
                                return 0
            return 1

        def dfs(i, nums, n):
            allList.append(nums.copy())
            for j in range(i, n):
                nums[j] = 1
                dfs(j+1, nums, n)
                nums[j] = 0
        dfs(0, B, n)
        res = 0
        for li in allList:
            res += solve(li)
        return res