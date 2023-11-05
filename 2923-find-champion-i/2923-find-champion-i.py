class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        hashT = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i != j and grid[i][j] == 1:
                    hashT[i] += 1
        max_ = max(hashT.values())
        for key in hashT:
            if hashT[key] == max_: return key
        return -1