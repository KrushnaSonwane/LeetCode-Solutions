class Solution(object):
    def punishmentNumber(self, n):
        
        def check(i, sum_, s):
            if i == len(s):
                return sum_ == num
            ans = False
            for j in range(i, len(s)):
                ans = check(j + 1, sum_ + int(s[i: j + 1]), s) or ans
            return ans
            
        res = 0
        for num in range(1, n + 1):
            sNum = num * num
            if check(0, 0, str(sNum)):
                res += sNum
        return res