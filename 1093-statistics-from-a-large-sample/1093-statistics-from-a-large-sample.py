class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        min_, max_, sum_, n, A, a, mode = inf, 0, 0, 0, [], 0, 0
        for i, num in enumerate(count):
            if num:
                min_ = min(min_, i) * 1.0
                max_ = max(max_, i) * 1.0
                sum_ += i * num
                n += num
                A.append([i, n])
                if a < num:
                    mode, a = i*1.0, num

        mean = sum_ / (n * 1.0)
        mid = n // 2

        def binarySearch(key):
            l, r, res = 0, len(A)-1, -1
            while r >= l:
                mid = (r + l) // 2
                if A[mid][1] >= key:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        
        if n % 2 == 0:
            i, j = binarySearch(n // 2), binarySearch(n // 2 + 1)
            sum_ = A[i][0] + A[j][0]
            median = sum_ / 2.0
        else:
            median = A[binarySearch(n // 2+1)][0] * 1.0
        return [min_, max_, mean, median, mode]