class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = n * 2
        hashT = defaultdict(set)
        for row, seat in reservedSeats:
            if seat in [2, 3, 4, 5]: hashT[row].add(1)
            if seat in [4, 5, 6, 7]: hashT[row].add(2)
            if seat in [6, 7, 8, 9]: hashT[row].add(3)
        for row in hashT:
            res -= 2 if len(hashT[row]) == 3 else 1
        return res