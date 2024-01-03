class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res, last, curr = 0, 0, 0
        for a in bank:
            curr = a.count('1')
            if curr and last:
                res += curr * last
            if curr: last = curr
        return res