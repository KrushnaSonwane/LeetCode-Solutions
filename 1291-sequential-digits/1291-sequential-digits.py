class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res= []
        for i in range(1, 10):
            num = 0
            for j in range(i, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)
        return sorted(res)