class Solution:
    def numberOfWays(self, S: str) -> int:
        A, sum_, count = [1], 0, 0
        if S.count('S') % 2 or S.count('S') == 0: return 0
        for ch in S:
            if ch == 'S':
                if sum_ == 2:
                    A.append(count+1)
                    count, sum_ = 0, 1
                else:
                    sum_ += 1
            else:
                if sum_ == 2: count += 1
                else: count = 0
        res, MOD = 1, 10**9+7
        for num in A:
            res = (res * num) % MOD
        return res