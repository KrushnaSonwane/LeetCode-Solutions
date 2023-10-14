class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        t = len(rolls) + n
        sum_ = mean * t - sum(rolls)
        res, rem = [], n - 1
        if n > sum_: return []
        for _ in range(n):
            if sum_ <= 0: return []
            res.append(min(sum_ - rem, 6))
            sum_ -= min(sum_ - rem, 6)
            rem -= 1
        return res if sum_ == 0 else []