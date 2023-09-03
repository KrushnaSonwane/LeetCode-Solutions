class Solution:
    def minimumOperations(self, num: str) -> int:
        res = len(num)-num.count('0')
        for curr in ['00','25', '50', '75']:
            count, i = 0, 1
            for ch in num[::-1]:
                if i == -1: break
                count += curr[i] != ch
                i -= curr[i]==ch 
            if i == -1:
                res = min(res, count)
        return res