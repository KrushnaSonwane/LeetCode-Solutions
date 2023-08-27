class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = 0
        for i in [-1, 1]:
            sum_ = 0
            for m in moves:
                if m=='R': sum_ += 1
                elif m=='L': sum_ -= 1
                else: sum_ += i
            res = max(res, abs(sum_))
        return res