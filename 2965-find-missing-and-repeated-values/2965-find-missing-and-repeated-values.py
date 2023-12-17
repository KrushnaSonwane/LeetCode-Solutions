class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashT = defaultdict(int)
        for li in grid:
            for num in li:
                hashT[num] += 1
                if hashT[num] == 2:
                    a = num
        for i in range(1, len(grid)*len(grid)+1):
            if hashT[i] == 0:
                b = i
        return [a, b]