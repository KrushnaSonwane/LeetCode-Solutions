class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        B = [A[i]-A[i+1] for i in range(len(A)-1)]
        last = inf
        count, res = 0, 0
        for b in B:
            if b != last: count = 1
            else: count += 1
            last = b
            if count >= 2: res += count - 1
        return res