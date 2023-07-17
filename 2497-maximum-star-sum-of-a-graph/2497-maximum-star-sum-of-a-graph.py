class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        hashT = defaultdict(list)
        for a, b in edges:
            hashT[a].append(vals[b])
            hashT[b].append(vals[a])
        res = max(vals)
        for node in hashT:
            hashT[node].sort(reverse = True)
            sum_ = vals[node]
            for i in range(min(len(hashT[node]),k)):
                sum_ += hashT[node][i]
                res = max(res, sum_)
        return res