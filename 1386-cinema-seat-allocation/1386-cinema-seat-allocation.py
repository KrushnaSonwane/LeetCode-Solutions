class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = n * 2
        hashT = defaultdict(list)
        for row, seat in reservedSeats: hashT[row].append(seat)
        for row in hashT:
            if 2 in hashT[row] or 3 in hashT[row]:
                res -= 1
                if 8 in hashT[row] or 9 in hashT[row]:
                    for i in [4, 5, 6, 7]:
                        if i in hashT[row]:
                            res -= 1; break
                else:
                    if 6 in hashT[row] or 7 in hashT[row]:
                        res -= 1
            elif 8 in hashT[row] or 9 in hashT[row]:
                res -= 1
                if 2 in hashT[row] or 3 in hashT[row]:
                    for i in [4, 5, 6, 7]:
                        if i in hashT[row]:
                            res -= 1; break
                else:
                    if 4 in hashT[row] or 5 in hashT[row]:
                        res -= 1
            else:
                if 4 in hashT[row] or 5 in hashT[row]:
                    res -= 1
                if 6 in hashT[row] or 7 in hashT[row]:
                    res -= 1
        return res