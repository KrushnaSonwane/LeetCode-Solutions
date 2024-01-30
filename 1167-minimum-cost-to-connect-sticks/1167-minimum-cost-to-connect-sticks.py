class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        A, res = [], 0
        for num in sticks:
            heappush(A, num)
        while len(A) > 1:
            a, b = heappop(A), heappop(A)
            res += a + b
            heappush(A, a+b)
        return res