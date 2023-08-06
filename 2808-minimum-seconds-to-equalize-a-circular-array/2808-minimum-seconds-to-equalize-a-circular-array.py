class Solution:
    def minimumSeconds(self, A: List[int]) -> int:
        hashT = defaultdict(list)
        n = len(A)
        for i, val in enumerate(A):
            hashT[val].append(i)
        res = ceil((n-1)/2)
        for val in hashT:
            max_ = -inf
            for i in range(len(hashT[val])-1):
                if i == 0:
                    count = hashT[val][i] + (n-1-hashT[val][-1])
                    max_ = max(max_, ceil(count / 2))
                count = hashT[val][i+1] - hashT[val][i] - 1
                max_ = max(max_, ceil(count/2))
            if max_!=-inf:
                res = min(res, max_)
        return res