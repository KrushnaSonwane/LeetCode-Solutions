class Solution:
    def numberOfWays(self, S: str) -> int:
        sum_, count = 0, 0
        if S.count('S') % 2 or S.count('S') == 0: 
            return 0
        MOD, res = 10**9+7, 1
        for ch in S:
            if ch == 'S':
                if sum_ == 2:
                    res = (res * (count + 1)) % MOD
                    count, sum_ = 0, 1
                else:
                    sum_ += 1
            else:
                if sum_ == 2: 
                    count += 1
                else: 
                    count = 0
        return res