class Solution:
    def dietPlanPerformance(self, C: List[int], k: int, L: int, H: int) -> int:
        res, sum_ = 0, 0
        for i in range(len(C)):
            sum_ += C[i]
            if i + 1 >= k:
                if sum_ < L:
                    res -= 1
                if sum_ > H:
                    res += 1
                sum_ -= C[i-(k-1)]
        return res