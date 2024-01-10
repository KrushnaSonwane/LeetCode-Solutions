class Solution:
    def reachNumber(self, target: int) -> int:
        res, sum_ = 1, 1
        target = abs(target)
        while True:
            if sum_ >= target and (sum_ - target) % 2 == 0: 
                return res
            res += 1
            sum_ += res
        return -1