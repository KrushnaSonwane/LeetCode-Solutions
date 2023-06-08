class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid[0])
        for arr in grid:
            l, r = 0, n - 1
            while r >= l:
                mid = (r + l) // 2
                if arr[mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            res += n - (mid + 1) if arr[mid] >= 0 else n - mid
        return res