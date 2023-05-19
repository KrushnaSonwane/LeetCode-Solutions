class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        res = []
        for i in range(n - 2):
            newArr = []
            for j in range(n - 2):
                max_ = 0
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        max_ = max(max_, grid[k][l])
                newArr.append(max_)
            res.append(newArr)
        return res