class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = data.count(1)
        if k == 0: return 0
        res, count = inf, 0
        for i in range(len(data)):
            count += data[i]
            if i+1 >= k:
                res = min(res, k - count)
                count -= data[i-(k-1)]
        return res