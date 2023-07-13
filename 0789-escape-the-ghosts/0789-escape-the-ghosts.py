class Solution:
    def escapeGhosts(self, G: List[List[int]], T: List[int]) -> bool:
        A = abs(abs(T[0])+abs(T[1]))
        for x, y in G:
            if abs(x-T[0]) + abs(y-T[1]) <= A: return 0
        return 1