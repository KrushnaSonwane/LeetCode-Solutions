class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        A = sorted([[len(W), W] for W in words])
        hashT, res = {}, 1
        for _, w in A:
            count = 1
            for i in range(len(w)):
                curr = w[:i] + w[i+1:]
                if curr in hashT:
                    res = max(res, hashT[curr] + 1)
                    count = max(count, hashT[curr] + 1)
            hashT[w] = count
        return res