class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if a + 2 == b + 1 == c: return [0, 0]
        max_ = ((b - a) + (c - b)) - 2
        if 2 in [b - a, c - b]:
            return [1, max_]
        if 1 in [b - a, c - b]: 
            return [1, max_]
        return [2, max_]